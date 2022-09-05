from rest_framework import serializers
from dishesapi.models import Dishes
from django.contrib.auth.models import User
class DishSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    price=serializers.IntegerField()
    category=serializers.CharField()
    rating=serializers.FloatField()
    def validate(self,data):
        price=data.get("price")
        if price<0:
            raise serializers.ValidationError("Invalid Price")
        return data

class DishModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dishes
        fields="__all__"


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username",
                "password",
                "first_name",
                "last_name",
                "email"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)