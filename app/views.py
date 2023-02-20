import cv2
import pandas as pd
from django.shortcuts import render
from .forms import ImageUploadForm
import numpy as np
from django.conf import settings
import os
from django.http import JsonResponse

def color(request):
    print("request=> ",request)
    if request.method == 'POST':
        for item in request:
            print("item=> ",item)
        print("request.POST=> ",request.POST)
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = cv2.imdecode(np.fromstring(request.FILES['image'].read(), np.uint8), cv2.IMREAD_COLOR)
            img = cv2.resize(img, (720, 720))
            r, g, b = img[img.shape[0]//2, img.shape[1]//2]
            r = int(r)
            g = int(g)
            b = int(b)
            # csv_path=os.path.join(settings.STATIC_ROOT, 'colors.csv')
            # csv = pd.read_csv(csv_path, names=['color', 'color_name', 'hex', 'R', 'G', 'B'], header=None)
            # minimum = 10000
            # for i in range(len(csv)):
            #     distance = abs(r - int(csv.loc[i, 'R'])) + abs(g - int(csv.loc[i, 'G'])) + abs(b - int(csv.loc[i, 'B']))
            #     if distance <= minimum:
            #         minimum = distance
            #         colorname = csv.loc[i, 'color_name']
            color=str(r)+"-"+str(g)+"-"+str(b)
            return JsonResponse({'color': color})
    else:
        form = ImageUploadForm()
    return render(request, 'index.html', {'form': form})
