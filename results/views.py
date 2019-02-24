from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Result
from django.utils import timezone
from PIL import Image

import numpy as np
import cv2

# Create your views here.

@login_required
def main(request):
    results = Result.objects # this has to be improved to only show results of that user
    return render(request, 'results/main.html', {'results': results})


@login_required
def check(request):
    # this is where you will run the opencv code
    if request.method == 'POST':
        if request.POST['title'] and request.POST['medium'] and request.POST['compound'] and request.FILES['image']:
            result = Result()
            result.title = request.POST['title']
            result.medium = request.POST['medium']
            result.compound = request.POST['compound']
            result.detail = request.POST['detail'] 
            result.image = request.FILES['image']
            img = Image.open(request.FILES['image'])
            result.pub_date = timezone.datetime.now()
            result.uploader = request.user
            result.outputval = opencv(img)
            result.save()
            return redirect('/result/'+str(result.id))
        else:
            return render(request, 'results/check.html', {'error': 'Please fill in all fields'})
    else:
        return render(request, 'results/check.html')


@login_required
def result(request, result_id):
    result = get_object_or_404(Result, pk=result_id)
    return render(request, 'results/result.html', {'result': result})

def opencv():
    image = cv2.imread(result.image.url)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    values = (" the height is %s , width is %s and number of channels is %s" % (height, width, channels)) 
    return values