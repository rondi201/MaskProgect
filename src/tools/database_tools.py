import os

from webapp.models import BoxWithoutMask, Images


def delete_all_box_with_images():
    # Get all boxes
    boxes = BoxWithoutMask.objects.all()
    # Get linked images
    images_id = set([])
    for box in boxes:
        id = box.source_image.id
        images_id.add(id)
    # Delete boxes
    boxes.delete()
    # Delete linked images
    for id in images_id:
        delete_image(id)

def delete_image(id: int):
    # Get row image
    image = Images.objects.get(id=id)
    # Delete image file
    image_path = image.image.path
    if os.path.isfile(image_path):
        os.remove(image_path)
    # Delete from database
    image.delete()

def delete_all_image():
    images = Images.objects.all()
    # Delete images file
    for image in images:
        image_path = image.image.path
        if os.path.isfile(image_path):
            os.remove(image_path)
    # Delete from database
    images.delete()
