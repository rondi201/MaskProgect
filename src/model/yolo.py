

class Yolo:
    _instance = None

    def __init__(self):
        pass
        # Make yolo model
        # self.model = torch.hub.load('../yolov5', 'yolov5s', source='local', classes=2, autoshape=True, pretrained=True)

    def __new__(cls, *args, **kwargs):
        if not Yolo._instance:
            Yolo._instance = super(Yolo, cls).__new__(cls, *args, **kwargs)
        return Yolo._instance

    def get_boxes(self, image):
        # Some code for find boxes #
        # ...

        boxes = [(0, 0, 100, 150), (50, 50, 100, 150)]
        return boxes


