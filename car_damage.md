### Secondary research
Car damage detection
1.	Use pretrained vgg16 to classify car damaged or not, dented or not. https://medium.com/analytics-vidhya/car-damage-classification-using-deep-learning-d29fa1e9a520
2.	Transfer learning with custom dataset. Images of whole cars and damaged cars. Dataset: https://www.kaggle.com/anujms/car-damage-detection
3.	Use yolo to localize damaged areas. https://github.com/robingenz/object-detection-yolov3-google-colab
4.	Create custom dataset for yolo with 3 classes: smash, dent, scratch
5.	Image annotation tool: https://github.com/tzutalin/labelImg
6.	Paper 1: https://www.researchgate.net/publication/342675878_Car_Damage_Detection_and_Classification
7.	Paper 2: Research on Vehicle Parts Defect Detection Based on Deep Learning Wang Liquna , Wu Jianshengb , Wu Dingjinc   (vgg16 with a inception v3 module)

LPDR with yolo
1.	https://github.com/bhadreshpsavani/CarPartsDetectionChallenge
2.	https://github.com/ThorPham/License-plate-detection
3.	https://towardsdatascience.com/how-to-detect-license-plates-with-python-and-yolo-8842aa6d25f7
4.	https://github.com/ankitbarai507/Indian-Vehicle-License-Plate-Detection
5.	https://github.com/pragatiunna/License-Plate-Number-Detection (important)
6.	Darknet: https://github.com/pjreddie/darknet
7.	Scaled yolo: https://github.com/WongKinYiu/ScaledYOLOv4

LPDR
Detection: detect the license plate from images of vehicles.
1.	Good to have, bbox ,  images of various vehicles, vehicle type, 1,280 × 720 pixels quality.
2.	Dset: https://paperswithcode.com/dataset/rodosol-alpr
3.	Roughly 3k number plates. Requires 6hrs of work
4.	Dset: https://paperswithcode.com/dataset/ufpr-alpr   (4,500  high res image, 150 cars, annotated)
5.	Good paper (mark rcnn): https://arxiv.org/ftp/arxiv/papers/1910/1910.01853.pdf
6.	Use yolo for detection: https://github.com/ThorPham/License-plate-detection
7.	Craft obj detector model (trained on syndata and vgg 16 backend, training code not found): https://github.com/clovaai/CRAFT-pytorch

Recognition: take cropped image of plate and recognise characters
1.	LPRNet : https://github.com/sirius-ai/LPRNet_Pytorch/blob/master/train_LPRNet.py
2.	SSIG dataset: https://paperswithcode.com/dataset/ssig-segplate
3.	AOLP dataset: https://paperswithcode.com/dataset/aolp
4.	ALPR repo: https://github.com/sergiomsilva/alpr-unconstrained

