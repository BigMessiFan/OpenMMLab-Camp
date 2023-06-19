## OpenMMLab实战训练营第二期

### 第一次作业

- 作业要求：[https://github.com/open-mmlab/OpenMMLabCamp/issues/93](https://github.com/open-mmlab/OpenMMLabCamp/issues/93)

### 第二次作业

- 作业要求：[https://github.com/open-mmlab/OpenMMLabCamp/issues/108](https://github.com/open-mmlab/OpenMMLabCamp/issues/108)
- 训练、测试、结果分析等全流程代码：[https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMPreTrain%20Tutorial/homework.ipynb](https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMPreTrain%20Tutorial/homework.ipynb)
- 配置文件：[https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMPreTrain%20Tutorial/resnet50_finetune.py](https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMPreTrain%20Tutorial/resnet50_finetune.py)
- 模型权重：[https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMPreTrain%20Tutorial/exps/epoch_20.pth](https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMPreTrain%20Tutorial/exps/epoch_20.pth)
- 使用resnet50_b16x8_cifar100模型，经过20个epoch微调之后，在验证集上的评估结果为：
<img src="https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMPreTrain%20Tutorial/eval_res.png" width=100%/>

### 第三次作业

- 作业要求：[https://github.com/open-mmlab/OpenMMLabCamp/issues/126](https://github.com/open-mmlab/OpenMMLabCamp/issues/126)
- 训练、测试、结果分析等全流程代码：[https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMDetection%20Tutorial/homework.ipynb](https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMDetection%20Tutorial/homework.ipynb)
- 配置文件：[https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMDetection%20Tutorial/custom_config_rtmdet.py](https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMDetection%20Tutorial/custom_config_rtmdet.py)
- 模型权重：[https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMDetection%20Tutorial/exps/rtmdet/best_coco/bbox_mAP_epoch_30.pth](https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMDetection%20Tutorial/exps/rtmdet/best_coco/bbox_mAP_epoch_30.pth)
- 使用rtmdet-tiny模型，经过40个epoch训练后，最优的模型权重在验证集上的评估结果为：
<img src="https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMDetection%20Tutorial/training_logs.png" width=100%/>

### 第四次作业

- 作业要求：[https://github.com/open-mmlab/OpenMMLabCamp/issues/393](https://github.com/open-mmlab/OpenMMLabCamp/issues/393)
- 训练、测试、结果分析等全流程代码：[https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMSegmentation%20Tutorial/homework.ipynb](https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMSegmentation%20Tutorial/homework.ipynb)
- 配置文件：[https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMSegmentation%20Tutorial/custom_config_pspnet_r50.py](https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMSegmentation%20Tutorial/custom_config_pspnet_r50.py)
- 模型权重：[https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMSegmentation%20Tutorial/exps/best_mIoU_iter_370.pth](https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMSegmentation%20Tutorial/exps/best_mIoU_iter_370.pth)
- 使用pspnet模型，经过400次迭代训练后，最优的模型权重在验证集上的评估结果为：
<img src="https://github.com/BigMessiFan/OpenMMLab-Camp/blob/main/MMSegmentation%20Tutorial/training_logs.png" width=80%/>
