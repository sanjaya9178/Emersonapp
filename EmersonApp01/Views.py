from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Item_details
from .serializers import User_Item
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.

def itemview(request):
    item_max=Item_details.objects.get(id=1)
    serializer=User_Item(item_max)
    # json_data=JSONRenderer.render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)
