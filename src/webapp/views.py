from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from datetime import datetime

# Create your views here.
from model.predict import predict_to_db_image
from tools.image_tools import image_load, image_cut, image_resize, image_to_uri
from webapp.models import Images, BoxWithoutMask


def startpage(request):
    return render(request, 'webapp/startpage.html')


def file_upload(request):
    if request.method == "POST":
        my_file = request.FILES.get('file')

        dt_now = datetime.now()
        my_file.name = dt_now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"

        obj = Images.objects.create(image=my_file)

        predict_to_db_image(obj.pk)

        return HttpResponse('')

    return JsonResponse({'post': 'false'})


def resultpage(request):
    boxes = BoxWithoutMask.objects.all()
    display_images = []
    for box in boxes:
        box_shape = (box.x, box.y, box.width, box.height)
        image_path = box.source_image.image.url
        image = image_load(image_path)
        image = image_cut(image, box_shape)
        image = image_resize(image, 256)
        image = image_to_uri(image)
        display_images.append(image)
    return render(request, 'webapp/resultpage.html', {'images': display_images})
