from address.serializers import add_ser,add_update
from address.models import address_model
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
# Create your views here.

class add_address(APIView):
    def post(self,request,format=None):
        serializer=add_ser(data=request.data)
        if serializer.is_valid(raise_exception=True):
            addr=serializer.save()
            return Response({'uuid':addr.id_add},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class get_address(APIView):
    def get(self,request,format=None):
        address_data=address_model.objects.all()
        sr=add_ser(address_data,many=True)
        return JsonResponse(sr.data,safe=False)

class update_address(APIView):
    def put(self,request,id,format=None):
        try:
            add_data=address_model.objects.get(id_add=id)
            updated_data=add_update(add_data,data=request.data,partial=True)
            if updated_data.is_valid(raise_exception=True):
                updated_data.save()
                return Response({id:"Updated"},status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'Error':updated_data.errors})
        except:
            return Response({id:"data does't exist"},status=status.HTTP_404_NOT_FOUND)

class delete_address(APIView):
    def delete(self,request,id,format=None):
        try:
            add_data=address_model.objects.get(id_add=id)
            add_data.delete()
            return Response({id:"deleted"},status=status.HTTP_202_ACCEPTED)
        except:       
            return Response({id:"data does't exist"},status=status.HTTP_404_NOT_FOUND)