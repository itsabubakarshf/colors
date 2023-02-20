import cv2
import pandas as pd
from django.shortcuts import render
from .forms import ImageUploadForm
import numpy as np
from django.conf import settings
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})

@csrf_exempt
def color(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = cv2.imdecode(np.fromstring(request.FILES['image'].read(), np.uint8), cv2.IMREAD_COLOR)
            img = cv2.resize(img, (720, 720))
            r, g, b = img[img.shape[0]//2, img.shape[1]//2]
            r = int(r)
            g = int(g)
            b = int(b)
            color = {'color': f"{r}-{g}-{b}"}
            return JsonResponse(color)
        else:
            error = {'error': 'Invalid form data'}
            return JsonResponse(error, status=400)
    else:
        error = {'error': 'Invalid request method'}
        return JsonResponse(error, status=400)
