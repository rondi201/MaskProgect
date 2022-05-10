from base64 import b64encode
from cv2 import imread, cvtColor, resize
from cv2 import COLOR_BGR2RGB
from io import BytesIO
from PIL import Image


def pil_image_from_numpy(numpy_img):
    img = Image.fromarray(numpy_img, 'RGB')
    return img


def pil_image_to_data_uri(pil_img):
    data = BytesIO()
    pil_img.save(data, "PNG")
    data64 = b64encode(data.getvalue())
    return u'data:img/png;base64,' + data64.decode('utf-8')


def image_to_uri(numpy_img):
    pil_img = pil_image_from_numpy(numpy_img)
    uri_img = pil_image_to_data_uri(pil_img)
    return uri_img


def image_crop(img, box, box_extension: float = 0.0):
    # xywh to xyxy
    xl, xr = box[0], box[0] + box[2]
    yt, yd = box[1], box[1] + box[3]
    # add margin
    y_margin, x_margin = (xr-xl) * box_extension, (yd-yt) * box_extension
    xl, xr = int(xl - x_margin), int(xr + x_margin)
    yt, yd = int(yt - y_margin), int(yd + y_margin)
    # correcting out of image edge
    if xl < 0: xl = 0
    if xr > img.shape[1]: xr = img.shape[1]
    if yt < 0: yt = 0
    if yd > img.shape[0]: yd = img.shape[0]

    return img[yt:yd, xl:xr]


def image_load(image_path):
    image = imread(image_path)
    image = cvtColor(image, COLOR_BGR2RGB)
    return image


def image_resize(image, output_size):
    """
    Rescale the image in a sample to a given size.

    Args:
        output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
    """
    h, w = image.shape[:2]
    if isinstance(output_size, int):
        if h > w:
            new_h, new_w = output_size * h / w, output_size
        else:
            new_h, new_w = output_size, output_size * w / h
    else:
        new_h, new_w = output_size

    new_h, new_w = int(new_h), int(new_w)
    image = resize(image, (new_w, new_h))
    return image
