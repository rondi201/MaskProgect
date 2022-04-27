import torch

from torchvision import transforms

from model.yolo import Yolo
from tools.image_tools import image_load
from webapp.models import Images, BoxWithoutMask


def predict_to_db_image(image_id):
    image_object = Images.objects.get(pk=image_id)
    image_path = image_object.image.path
    image = image_load(image_path)
    image = transforms.ToTensor()(image)

    model = Yolo()
    boxes = model.get_boxes(image)

    for box in boxes:
        x, y, w, h = box
        BoxWithoutMask.objects.create(x=x, y=y, width=w, height=h, source_image=image_object)

