import torch
from models.common import AutoShape


class Yolo:
    _instance = None
    path_weights = "../data/weights/best.pt"  # path to model weights 'path/to/best.pt'

    def __init__(self) -> object:
        pass
        # Make yolo model
        self.model = None
        self.__model_load()

    def __new__(cls, *args, **kwargs) -> object:
        if not Yolo._instance:
            Yolo._instance = super(Yolo, cls).__new__(cls, *args, **kwargs)
        return Yolo._instance

    def __model_load(self, autoshape=True) -> None:
        try:
            model = torch.load(self.path_weights)['model']  # load model
            model = model.float()  # weight to float
            if autoshape:
                model = AutoShape(model)  # for file/URI/PIL/cv2/np inputs and NMS
        except Exception as e:
            s = f'{e}. Check if the file exists and if the "model" is present in the file'
            raise Exception(s) from e

        self.model = model

    def get_boxes(self, image):
        # Image inputs are:
        #   file:       imgs = 'data/images/zidane.jpg'  # str or PosixPath
        #   URI:             = 'https://ultralytics.com/images/zidane.jpg'
        #   OpenCV:          = cv2.imread('image.jpg')[:,:,::-1]  # HWC BGR to RGB x(640,1280,3)
        #   PIL:             = Image.open('image.jpg') or ImageGrab.grab()  # HWC x(640,1280,3)
        #   numpy:           = np.zeros((640,1280,3))  # HWC
        #   torch:           = torch.zeros(16,3,320,640)  # BCHW (scaled to size=640, 0-1 values)
        #   multiple:        = [Image.open('image1.jpg'), Image.open('image2.jpg'), ...]  # list of images
        predict = self.model(image)
        boxes = predict.xyxy
        return boxes
