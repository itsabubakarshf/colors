import cv2
import pandas as pd
from django.shortcuts import render
from .forms import ImageForm
import numpy as np
from django.conf import settings
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
import base64
from app.models import ImageModel

def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})
@csrf_exempt
def color(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
            image_data = base64.b64decode(data)
            if not image_data:
                error = {'error': 'Empty input image data'}
                return JsonResponse(error, status=400)
            img = cv2.imdecode(np.fromstring(image_data, np.uint8), cv2.IMREAD_COLOR)
            if img is None:
                error = {'error': 'Failed to decode input image'}
                return JsonResponse(error, status=400)
            r, g, b = img[img.shape[0]//2, img.shape[1]//2]
            r = int(r)
            g = int(g)
            b = int(b)
            color = {'color': f"{r}-{g}-{b}"}
            return JsonResponse(color)
        else:
            error = {'error': form.errors}
            return JsonResponse(error, status=400)
    else:
        error = {'error': 'Invalid request method'}
        return JsonResponse(error, status=400)