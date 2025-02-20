from rest_framework import serializers
from .models import Property
import os

class PropertySerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True
    )

    image_urls = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = [
            'id', 'propertyName', 'availableFor', 'totalPrice', 'perSqFeetPrice',
            'propertyType', 'bedroom', 'bathroom', 'parking', 'area', 'year',
            'address', 'details', 'images', 'image_urls'
        ]

    def create(self, validated_data):
        images = validated_data.pop('images')

        property_instance = Property.objects.create(**validated_data)

        # Create folder based on ID
        image_folder = property_instance.get_image_folder_path()
        os.makedirs(image_folder, exist_ok=True)

        # Save images in the folder
        for image in images:
            image_path = os.path.join(image_folder, image.name)
            
            with open(image_path, 'wb+') as dest:
                for chunk in image.chunks():
                    dest.write(chunk)

        return property_instance
    
    #  for images
    def get_image_urls(self, obj):
        """Fetches URLs of images stored in the folder named after the property ID."""
        image_folder = obj.get_image_folder_path()
        if os.path.exists(image_folder):
            # List all files in the folder
            return [
                f"{self.context['request'].build_absolute_uri('/media/property_images/')}{obj.id}/{file_name}"
                for file_name in os.listdir(image_folder)
                if os.path.isfile(os.path.join(image_folder, file_name))
            ]
        return []
