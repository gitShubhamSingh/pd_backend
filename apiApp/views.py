from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PropertySerializer
from .models import Property
import os
import shutil


class PropertyCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):
        
        serializer = PropertySerializer(data=request.data)
       
        if serializer.is_valid():
            property_instance = serializer.save()
            return Response({
                "id": property_instance.id,
                "message": "Property created successfully!"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AllPropertyAPIView(APIView):

    def get(self, request, *args, **kwargs):


        property_id = kwargs.get('id', None)
        
        if property_id:
            # Fetch the property with the specific ID
            try:
                property_instance = Property.objects.get(id=property_id)
                serializer = PropertySerializer(property_instance, context={"request": request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Property.DoesNotExist:
                return Response({"error": "Property not found"}, status=status.HTTP_404_NOT_FOUND)
        

        properties = Property.objects.all()  # Fetch all property instances from the database
        serializer = PropertySerializer(properties, many=True, context={"request": request})  # Serialize the queryset
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return the serialized data
    

    def delete(self, request, *args, **kwargs):
        property_id = kwargs.get('id', None)

        if property_id:
            try:
                property_instance = Property.objects.get(id=property_id)
                
                # Get the directory path
                image_folder = property_instance.get_image_folder_path()
                
                # Delete the directory and its contents
                if os.path.exists(image_folder) and os.path.isdir(image_folder):
                    shutil.rmtree(image_folder)  # Deletes the folder and its contents
                
                # Delete the property instance from the database
                property_instance.delete()
                
                return Response(
                        {"message": "Property deleted successfully."},
                        status=status.HTTP_204_NO_CONTENT
                    )

            except Property.DoesNotExist:
                return Response({"error":"Property not found"}, status=status.HTTP_404_NOT_FOUND)
        