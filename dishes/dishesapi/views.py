from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from dishesapi.models import Dishes
from dishesapi.serializer import DishSerializer,DishModelSerializer,UserModelSerializer
from rest_framework import status
from rest_framework.viewsets import ViewSet,ModelViewSet
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
class DishesView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        serializer=DishSerializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=DishSerializer(data=request.data)
        if serializer.is_valid():
            Dishes.objects.create(**serializer.validated_data)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DishesDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Dishes.objects.get(id=id)
        serializer=DishSerializer(instance)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Dishes.objects.get(id=id)
        serializer=DishSerializer(data=request.data)
        if serializer.is_valid():
            instance.name=serializer.validated_data.get("name")
            instance.category=serializer.validated_data.get("category")
            instance.price=serializer.validated_data.get("price")
            instance.rating=serializer.validated_data.get("rating")
            instance.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Dishes.objects.get(id=id)
        serializer=DishSerializer(instance)
        instance.delete()
        return Response({"msg","deleted"},status=status.HTTP_204_NO_CONTENT)




class DishModelView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        if "category" in request.query_params:
            qs=qs.filter(category=request.query_params.get("category"))
        serializer=DishModelSerializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        serializer=DishModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DishDetailModelView(APIView):
    def get(self, request, *args, **kwargs):
        id=kwargs.get("id")
        instance=Dishes.objects.get(id=id)
        serializer=DishModelSerializer(instance)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        id=kwargs.get("id")
        object=Dishes.objects.get(id=id)
        serializer=DishModelSerializer(data=request.data,instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        id = kwargs.get("id")
        object = Dishes.objects.get(id=id)
        object.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)

class DishViewSetView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs = Dishes.objects.all()
        if "category" in request.query_params:
            qs = qs.filter(category=request.query_params.get("category"))
        serializer = DishModelSerializer(qs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = DishModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve (self, request, *args, **kwargs):
        id = kwargs.get("pk")
        instance = Dishes.objects.get(id=id)
        serializer = DishModelSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        object = Dishes.objects.get(id=id)
        serializer = DishModelSerializer(data=request.data, instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        object = Dishes.objects.get(id=id)
        object.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_204_NO_CONTENT)

class DishModelViewSetView(ModelViewSet):
    serializer_class = DishModelSerializer
    queryset = Dishes.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class UserModelViewSetView(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()



