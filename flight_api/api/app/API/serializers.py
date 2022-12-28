from rest_framework import serializers
from app.models import Detail

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = '__all__'