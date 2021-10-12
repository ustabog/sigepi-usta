from rest_framework import serializers
from .models import *

class PermisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = mod
        fields = '__all__'

class FuncionSerializer(serializers.ModelSerializer):
    class Meta:
        model = func_app
        fields = '__all__'

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = app_mod
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = rol
        fields = '__all__'
