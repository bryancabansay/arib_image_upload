# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from base64 import b64decode
from django.views.decorators.csrf import csrf_exempt

def index(request):
  return render(request, 'test_app/index.html')

@csrf_exempt
def upload_image(request):
  image_data = b64decode(request.POST.get("image_data", ""))
  filename = 'image_test.jpeg'
  fh = open(filename, "wb")
  fh.write(image_data)
  fh.close()
  return HttpResponse("Hello There!")