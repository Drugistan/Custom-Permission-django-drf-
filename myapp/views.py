from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework import status
from .serializers import UserSerializers
from .models import CustomUser
from rest_framework.response import Response
from .permission import UserCustomPermission, ExpiredObjectSuperuserOnly

# Create your views here.


class StudentView(APIView):
    permission_classes = [ExpiredObjectSuperuserOnly & UserCustomPermission]
    def get(self, request):
        instance = CustomUser.objects.all()
        serializer_intance = UserSerializers(instance, many=True)
        if serializer_intance:
            self.check_object_permissions(request, instance)
            return Response(serializer_intance.data, status=status.HTTP_200_OK)
        else:
            return Response({
                "Response" : "Something is Wrong"
            }, status=status.HTTP_400_BAD_REQUEST)