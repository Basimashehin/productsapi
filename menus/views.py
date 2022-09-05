from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from menus.models import menu_items


class AddView(APIView):
    def get(self,request,*args,**kwargs):
        all_item=menu_items
        if "category" in request.query_params:
            ct=request.query_params.get("category")
            all_item=[item for item in menu_items if item["category"]==ct]
        if "limit" in request.query_params:
            lmt=int(request.query_params.get("limit"))
            all_item=all_item[:lmt]
        return Response(data=all_item)
    def post(self,request,*args,**kwargs):
        data=request.data
        menu_items.append(data)
        return Response(data=data)

class PostDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        item=[item for item in menu_items if item["code"]==id].pop()
        return Response(data=item)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        item=[item for item in menu_items if item["code"]==id].pop()
        item.update(request.data)
        return Response(data=item)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        item=[item for item in menu_items if item["code"]==id].pop()
        menu_items.remove(item)
        return Response(data=item)



