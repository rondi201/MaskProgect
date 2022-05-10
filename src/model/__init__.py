import sys
sys.path.append("../yolov5")
from model.yolo import Yolo
sys.path.remove("../yolov5")

# Yolo initialization
Yolo()