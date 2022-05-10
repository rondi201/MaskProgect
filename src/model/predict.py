import torch

from torchvision import transforms

from model.yolo import Yolo
from tools.image_tools import image_load
from webapp.models import Images, BoxWithoutMask


def predict_to_db_image(image_id):
    image_object = Images.objects.get(pk=image_id)
    image_path = image_object.image.path

    model = Yolo()
    # Predict boxes for current image
    boxes = model.get_boxes(image_path)[0]
    # Convert predict to numpy and int
    boxes = boxes.numpy().astype(int)

    for box in boxes:
        # Check if class is "without_mask"
        if box[5] != 0:
            continue
        # Get xyxy coordinates
        xl, yt, xr, yd = box[:4]
        # Convert xyxy to xywh
        x, y, w, h = xl, yt, xr-xl, yd-yt
        BoxWithoutMask.objects.create(x=x, y=y, width=w, height=h, source_image=image_object)

