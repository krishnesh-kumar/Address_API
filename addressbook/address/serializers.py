from dataclasses import fields
from address.models import address_model
from rest_framework import serializers


class add_ser(serializers.ModelSerializer):
    class Meta:
        model=address_model
        fields=['id_add','addre']
        
    
    def create(self,validate_data):
        return address_model.objects.create(**validate_data)

class add_update(serializers.ModelSerializer):
    class Meta:
        model=address_model
        fields=['addre']

    def update(self, instance, validated_data):
        instance.addre = validated_data.get('addre', instance.addre)
        instance.save()
        return instance
