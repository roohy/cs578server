__author__ = 'roohy'


from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.forms import widgets
from .models import Status,USER
class UserSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url",'username','email','groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','name')

class StatusSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    text = serializers.CharField()
    info = serializers.CharField(max_length=100, required=False, allow_blank=True)
    user = serializers.IntegerField()
    def create(self, validated_data):
        return Status.objects.create(**validated_data)
    def update(self, instance,validated_data):
        instance.text = validated_data.get('text',instance.text)
        instance.info = validated_data.get('info',instance.info)
        instance.user = validated_data.get('user',instance.user)
        instance.save()
        return instance
class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    uid = serializers.IntegerField()
    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return USER.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.uid = validated_data.get('uid',instance.uid)
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance

