"""
@coding: utf-8
@Auther: Tante
@Filename: mergeModel.py
@CreateTime: 2023/11/12 21:15
"""
# 集成算法
import torch
from torch import nn
from yolov5.models.common import Conv
from yolov5.utils.downloads import attempt_download


class Ensemble(nn.ModuleList):
    # Ensemble of models
    def __init__(self):
        super().__init__()

    def forward(self, x, augment=False, profile=False, visualize=False):
        y = []
        # 集成模型为多个模型时, 在每一层forward运算时, 都要运行多个模型在该层的结果append进y中
        for module in self:
            y.append(module(x, augment, profile, visualize)[0])
        # y = torch.stack(y).max(0)[0]  # 求多个模型结果的最大值 max ensemble
        # y = torch.stack(y).mean(0)    # 求多个模型结果的均值   mean ensemble
        y = torch.cat(y, 1)             # 将多个模型结果concat在一起, 后面做做nms等于翻了一倍的pred nms ensemble
        return y, None  # inference, train output


def attempt_load(weights, map_location=None, inplace=True, fuse=True):
    from yolov5.models.yolo import Detect, Model

    # Loads an ensemble of models weights=[a,b,c] or a single model weights=[a] or weights=a
    model = Ensemble()

    # weights如果是单路径, 则使用单个模型; 如果是list多路径, 则使用集成模型(多模型)
    for w in weights if isinstance(weights, list) else [weights]:
        # 这里map_location参数可以指定加载设备, 或者实现设备间的转化，eg：cuda1->cuda0 / cuda->cpu
        ckpt = torch.load(attempt_download(w), map_location=map_location)  # load
        if fuse:
            # 参数重结构化
            model.append(ckpt['ema' if ckpt.get('ema') else 'model'].float().fuse().eval())  # FP32 model
        else:
            model.append(ckpt['ema' if ckpt.get('ema') else 'model'].float().eval())  # without layer fuse

    # Compatibility updates(关于版本兼容的设置)
    for m in model.modules():
        if type(m) in [nn.Hardswish, nn.LeakyReLU, nn.ReLU, nn.ReLU6, nn.SiLU, Detect, Model]:
            m.inplace = inplace  # pytorch 1.7.0 compatibility
            if type(m) is Detect:
                if not isinstance(m.anchor_grid, list):  # new Detect Layer compatibility
                    delattr(m, 'anchor_grid')  # delattr(x, 'y') is equivalent to `del x.y'
                    setattr(m, 'anchor_grid', [torch.zeros(1)] * m.nl)  # setattr(x, 'y', v) is equivalent to `x.y = v'
        elif type(m) is Conv:
            m._non_persistent_buffers_set = set()  # pytorch 1.6.0 compatibility

    # 单模型设置
    if len(model) == 1:
        return model[-1]  # return model

    # 集成模型设置
    else:
        print(f'Ensemble created with {weights}\n')
        # 给每个模型一个name属性
        for k in ['names']:
            setattr(model, k, getattr(model[-1], k))  # getattr(x, 'y') is equivalent to x.y
        # 给每个模型分配stride属性
        model.stride = model[torch.argmax(torch.tensor([m.stride.max() for m in model])).int()].stride  # max stride
        return model  # return ensemble
