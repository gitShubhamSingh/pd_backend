from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . import models

from . import serializers

class LoginGenericsAPI(generics.GenericAPIView):
    serializer_class = serializers.AdminSerializers

    def post(self, request, *args, **kwargs):
      
        serializer = self.get_serializer(data=request.data)
  
        if serializer.is_valid(raise_exception=True):
            try:
                email=serializer.validated_data['email']
                password=serializer.validated_data['password']
          
                if models.AdminModel.objects.using('user_db').filter(email=email,password=password).exists():
                    admin_user = models.AdminModel.objects.using('user_db').get(
                        email=email,
                        password=password
                    )
                    if admin_user:
                        return Response({
                            "status":status.HTTP_200_OK,
                            "email":admin_user.email,
                            "message":"You are ready for Full access"
                        })
                    else:
                        return Response({
                            "status":status.HTTP_401_UNAUTHORIZED,
                            "message":"Serializer is not valid"
                        })
                else:
                    return Response({
                            "status":status.HTTP_401_UNAUTHORIZED,
                            "message":"User Not Exist"
                        })
            except Exception as e:
                return Response({
                    "status":status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message":str(e)
                })
        else:
            return Response({
                "status":status.HTTP_401_UNAUTHORIZED,
                "message":"Serializer is not valid"
            })
