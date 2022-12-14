"""HotelMenu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from menus import views as hotelview
from productsapi.views import ProductsView,ProductDetailView,ProductModelView,ProductDetailsModelView,ProductViewSetView,ProductModelViewSetView,UserModelViewSetView,CartsView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
router=DefaultRouter()
router.register("api/v3/products",ProductViewSetView,basename="products")
router.register("api/v4/products",ProductModelViewSetView,basename="products")
router.register("products/signup",UserModelViewSetView,basename="products")
router.register("api/user/carts",CartsView,basename="carts")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotelmenu/add/',hotelview.AddView.as_view()),
    path('hotelmenu/add/<int:id>', hotelview.PostDetailView.as_view()),
    path('myg/products/', ProductsView.as_view()),
    path('myg/products/<int:id>',ProductDetailView.as_view()),
    path('api/v2/myg/products/', ProductModelView.as_view()),
    path('api/v2/myg/products/<int:id>', ProductDetailsModelView.as_view()),
    # path('api/v4/token',obtain_auth_token)
    path('api/v4/token',TokenObtainPairView.as_view()),
    path('api/v4/token/refresh',TokenRefreshView.as_view()),
]+router.urls
