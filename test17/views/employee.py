from django.http import Http404
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from collections import Counter
from itertools import groupby
from rest_framework import generics

from test17.filters import EmployeeFilter
from test17.models import Employee
from test17.serializers import EmployeeSerializer, EmployeeCreateSerializer, EmployeeUpdateSerializer, EmployeeDeleteSerializer


class EmployeeViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = EmployeeSerializer
    permissions_classes = [IsAuthenticated]
    queryset = Employee.objects.all()



    def get_serializer_class(self):
        serializer_class = EmployeeCreateSerializer

        if self.action == 'create':
            serializer_class = EmployeeCreateSerializer
        elif self.action == 'update_attachments':
            serializer_class = EmployeeUpdateSerializer
        elif self.action == 'delete_attachments':
            serializer_class = EmployeeDeleteSerializer
        elif self.action == 'list':
            serializer_class = EmployeeSerializer
        return serializer_class


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer_data = self.serializer_class(instance).data
        return Response(data=serializer_data, status=status.HTTP_201_CREATED)


    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def update_attachments(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.update_attachments()
        serializer.save()
        return Response(serializer.data)


    def get_cars(self):
        owner = self.request.user

        try:
            instance = Employee.objects.filter(owner=owner)
            return instance
        except:
            raise Http404


    def get_object(self):
        id = self.kwargs['pk']
        try:
            instance = self.queryset.get(id=id)
            return instance
        except:
            raise Http404


    def delete_attachments(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.delete_attachments()
        return Response(data={'detail': 'all deleted'},
                        status=status.HTTP_204_NO_CONTENT)


class AnaliticViewSet(generics.ListAPIView):

    queryset = Employee.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filterset_class = EmployeeFilter
    filterset_fields = ['name', ]
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, ]



