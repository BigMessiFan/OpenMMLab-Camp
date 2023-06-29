# 需要修改的关键配置
num_classes = 30
dataset_type = "CustomDataset"
batch_size = 8
max_epochs = 20
seed_num = 2023
data_root = ""
img_dir = ""
train_ann_file = "./data/fruit30_train/train.txt"
val_ann_file = "./data/fruit30_train/val.txt"
test_ann_file = "./data/fruit30_train/val.txt"
ckpt_path = "./resnet50_b16x8_cifar100_20210528-67b58a1b.pth"
work_dir = "./exps"
cls_names = ("榴莲", "葡萄-红", "哈密瓜", "香蕉", "黄瓜", "梨", "胡萝卜", "西瓜", "杨梅", "苹果-青", "车厘子", "脐橙", "苦瓜", "山竹", "圣女果", "石榴", "火龙果", "柚子", "菠萝", "葡萄-白", "苹果-红", "芒果", "柠檬", "猕猴桃", "砂糖橘", "西红柿", "荔枝", "草莓", "桂圆", "椰子")
ckpt_interval = 1
save_best = "auto"
save_last = True
max_keep_ckpts = 2


model = dict(
    type="ImageClassifier",
    backbone=dict(
        type="ResNet_CIFAR",
        depth=50,
        num_stages=4,
        out_indices=(3, ),
        style="pytorch"),
    neck=dict(type="GlobalAveragePooling"),
    head=dict(
        type="LinearClsHead",
        num_classes=num_classes,
        in_channels=2048,
        loss=dict(type="CrossEntropyLoss", loss_weight=1.0)),
    # 加入初始化配置
    init_cfg=dict(type="Pretrained", checkpoint=ckpt_path)
)
data_preprocessor = dict(
    num_classes=num_classes,
    mean=[129.304, 124.07, 112.434],
    std=[68.17, 65.392, 70.418],
    to_rgb=False)
# train_pipeline = [
#     dict(type='LoadImageFromFile'),
#     dict(type="RandomCrop", crop_size=32, padding=4),
#     dict(type="RandomFlip", prob=0.5, direction="horizontal"),
#     dict(type="PackInputs")
# ]
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='RandomResizedCrop', scale=224),
    dict(type='RandomFlip', prob=0.5, direction='horizontal'),
    dict(type='PackInputs')
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='ResizeEdge', scale=256, edge='short'),
    dict(type='CenterCrop', crop_size=224),
    dict(type='PackInputs')
]
train_dataloader = dict(
    batch_size=batch_size,
    num_workers=2,
    dataset=dict(
        type=dataset_type,
        ann_file=train_ann_file,
        data_root=data_root,
        data_prefix=dict(img_path=img_dir),
        with_label=True,
        metainfo={"classes": cls_names},
        pipeline=train_pipeline),
    sampler=dict(type="DefaultSampler", shuffle=True))
val_dataloader = dict(
    batch_size=batch_size,
    num_workers=2,
    dataset=dict(
        type=dataset_type,
        ann_file=val_ann_file,
        data_root=data_root,
        data_prefix=dict(img_path=img_dir),
        with_label=True,
        metainfo={"classes": cls_names},
        pipeline=test_pipeline),
    sampler=dict(type="DefaultSampler", shuffle=False))
val_evaluator = dict(type="Accuracy", topk=(1, 5))

test_dataloader = dict(
    batch_size=batch_size,
    num_workers=2,
    dataset=dict(
        type=dataset_type,
        ann_file=test_ann_file,
        data_root=data_root,
        data_prefix=dict(img_path=img_dir),
        with_label=True,
        metainfo={"classes": cls_names},
        pipeline=test_pipeline),
    sampler=dict(type="DefaultSampler", shuffle=False))
test_evaluator = val_evaluator

optim_wrapper = dict(
    optimizer=dict(type="SGD", lr=0.1*batch_size/128, momentum=0.9, weight_decay=0.0005))
param_scheduler = dict(
    type="MultiStepLR", by_epoch=True, milestones=[int(max_epochs*0.3), int(max_epochs*0.6), int(max_epochs*0.8)], gamma=0.2)
train_cfg = dict(by_epoch=True, max_epochs=max_epochs, val_interval=1)
val_cfg = dict()
test_cfg = dict()
# auto_scale_lr = dict(base_batch_size=128)
default_scope = "mmpretrain"
default_hooks = dict(
    timer=dict(type="IterTimerHook"),
    logger=dict(type="LoggerHook", interval=10),
    param_scheduler=dict(type="ParamSchedulerHook"),
    checkpoint=dict(type="CheckpointHook", interval=ckpt_interval, save_best=save_best, save_last=save_last, max_keep_ckpts=max_keep_ckpts),
    sampler_seed=dict(type="DistSamplerSeedHook"),
    visualization=dict(type="VisualizationHook", enable=False))
env_cfg = dict(
    cudnn_benchmark=False,
    mp_cfg=dict(mp_start_method="fork", opencv_num_threads=0),
    dist_cfg=dict(backend="nccl"))
# vis_backends = [dict(type="LocalVisBackend")]
# visualizer = dict(
#     type="UniversalVisualizer", vis_backends=[dict(type="LocalVisBackend")])
log_level = "INFO"
load_from = None
resume = False
randomness = dict(seed=seed_num, deterministic=False)