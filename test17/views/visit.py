from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


from test17.models import Visit
from test17.serializers import VisitSerializer, VisitCreateSerializer, VisitUpdateSerializer
from test17.filters import VisitFilter


class VisitViewSet(ModelViewSet):
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated]
    queryset = Visit.objects.all()

    def get_serializer_class(self):
        serializer_class = VisitSerializer

        if self.action == 'create':
            serializer_class = VisitCreateSerializer
        elif self.action == 'update':
            serializer_class = VisitUpdateSerializer

        return serializer_class


class OutletAnaliticViewSet(generics.ListAPIView):

    queryset = Visit.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filterset_class = VisitFilter
    filterset_fields = ['outlet', ]
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated, ]