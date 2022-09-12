from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from productsapi.models import Products,Review,Carts
from productsapi.serializer import ProductSerializer,ProductModelSerializer,UserModelSerializer,ReviewSerializer,CartsModelSerializer
from rest_framework import status
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import authentication,permissions
from rest_framework.decorators import action
# Create your views here.

class ProductsView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Products.objects.all()
        serializer=ProductSerializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            Products.objects.create(**serializer.validated_data)
            # Products.objects.create(p_name=request.data.get("p_name"),
            #                         category=request.data.get("category"),
            #                         price=request.data.get("price"),
            #                         rating=request.data.get("rating"))
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Products.objects.get(id=id)
        serializer=ProductSerializer(qs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Products.objects.get(id=id)
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            # instance.update(**serializer.validated_data)
            instance.p_name=serializer.validated_data.get("p_name")
            instance.category=serializer.validated_data.get("category")
            instance.price=serializer.validated_data.get("price")
            instance.rating=serializer.validated_data.get("rating")
            instance.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Products.objects.get(id=id)
        serializer=ProductSerializer(instance)
        instance.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)


class ProductModelView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Products.objects.all()
        if "category" in request.query_params:
            qs=qs.filter(category=request.query_params.get("category"))
        if "price_gt" in request.query_params:
            qs=qs.filter(price__gte=request.query_params.get("price_gt"))
        serializer=ProductModelSerializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductDetailsModelView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Products.objects.get(id=id)
        serializer=ProductModelSerializer(instance)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def put(self,request,*args,**kwargs):
        id = kwargs.get("id")
        object = Products.objects.get(id=id)
        serializer=ProductModelSerializer(data=request.data,instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        id = kwargs.get("id")
        instance = Products.objects.get(id=id)
        serializer = ProductModelSerializer(instance)
        instance.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)

class ProductViewSetView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Products.objects.all()
        serializer=ProductModelSerializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def create(self,request,*args,**kwargs):
        serializer=ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        instance=Products.objects.get(id=id)
        serializer=ProductModelSerializer(instance)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        object=Products.objects.get(id=id)
        serializer=ProductModelSerializer(instance=object,data=request.data,)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        instance = Products.objects.get(id=id)
        serializer = ProductModelSerializer(instance)
        instance.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)
class ProductModelViewSetView(ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset = Products.objects.all()
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    @action(methods=["get"],detail=True)
    def get_reviews(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        product=Products.objects.get(id=id)
        reviews=product.review_set.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)
    # @action(methods=["post"],detail=True)
    # def post_reviews(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     product=Products.objects.get(id=id)
    #     author=request.user
    #     review=request.data.get("review")
    #     rating=request.data.get("rating")
    #     qs=Review.objects.create(author=author,
    #                              product=product,
    #                              review=review,
    #                              rating=rating
    #                              )
    #     serializer=ReviewSerializer(qs)
    #     return Response(data=serializer.data)

    @action(methods=["post"],detail=True)
    def post_review(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        product = Products.objects.get(id=id)
        author=request.user
        serializer=ReviewSerializer(data=request.data,context={"author":author,"product":product})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    @action(methods=["post"],detail=True)
    def add_to_cart(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        product=Products.objects.get(id=id)
        user=request.user
        serializer=CartsModelSerializer(data=request.data,context={"user":user,"product":product})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

from  django.contrib.auth.models import User
class UserModelViewSetView(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()



class CartsView(ModelViewSet):
    serializer_class = CartsModelSerializer
    queryset = Carts.objects.all()
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=Carts.objects.filter(user=request.user)
        serializer=CartsModelSerializer(qs,many=True)
        return Response(data=serializer.data)
    def create(self, request, *args, **kwargs):
        return Response(data={"msg":"no access"})


