from rest_framework import serializers
from productsapi.models import Products,Review,Carts
from django.contrib.auth.models import User
class ProductSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    p_name=serializers.CharField()
    category=serializers.CharField()
    price=serializers.IntegerField()
    rating=serializers.FloatField()
    def validate(self,data):
        price=data.get("price")
        if(price<0):
            raise serializers.ValidationError("InvalidPrice")
        return data
class ProductModelSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    average_rating=serializers.CharField(read_only=True)
    review_count=serializers.CharField(read_only=True)
    class Meta:
        model=Products
        # fields=["id","p_name","category","price","rating"]
        fields=["id",
                "p_name",
                "category",
                "price",
                "average_rating",
                "review_count"]


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username",
                "first_name",
                "last_name",
                "email",
                "password"
                ]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)




class ReviewSerializer(serializers.ModelSerializer):
    author=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    class Meta:
        model=Review
        fields="__all__"
    def create(self, validated_data):
        author=self.context.get("author")
        product=self.context.get("product")
        return Review.objects.create(**validated_data,author=author,product=product)

class CartsModelSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    date=serializers.DateField(read_only=True)
    status=serializers.CharField(read_only=True)
    class Meta:
        model=Carts
        fields="__all__"

    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Carts.objects.create(**validated_data,user=user,product=product)






























































