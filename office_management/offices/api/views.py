from datetime import datetime

from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from django.forms import model_to_dict

from offices.models import Office, Room, Employee
from .serializer import OfficeSerializer, RoomSerializer, EmployeeSerializer


class OfficeViewSet(viewsets.ModelViewSet):
    # queryset = Office.objects.all()
    serializer_class = OfficeSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Office.objects.all()[:3]

        return Office.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def rooms(self, request, pk=None):
        rooms = Room.objects.get(pk=pk)
        return Response({'rooms': rooms.number})


# class OfficeAPIList(generics.ListCreateAPIView):
#     queryset = Office.objects.all()
#     serializer_class = OfficeSerializer
#
#
# class OfficeAPIUpdate(generics.UpdateAPIView):
#     queryset = Office.objects.all()
#     serializer_class = OfficeSerializer
#
#
# class OfficeAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Office.objects.all()
#     serializer_class = OfficeSerializer


# class OfficeAPIView(APIView):
#     def get(self, request):
#         offices = Office.objects.all()
#         return Response({"offices": OfficeSerializer(offices, many=True).data})
#
#     def post(self, request):
#         serializer = OfficeSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"post": serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed!'})
#
#         try:
#             instance = Office.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists!'})
#
#         serializer = OfficeSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method DELETE not defined!'})
#
#         try:
#             instance = Office.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists!'})
#
#         instance.delete()
#         return Response({'status': 'No content!'})


class RoomAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class EmployeeAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
