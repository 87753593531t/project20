from django.http import Http404
from rest_framework import status, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


from test17.models import Outlet
from test17.serializers import OutletSerializer, OutletCreateSerializer, OutletUpdateSerializer, OutletDeleteSerializer
from test17.filters import OutletFilter


class OutletViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = OutletSerializer
    permissions_classes = [IsAuthenticated]
    queryset = Outlet.objects.all()

    def get_serializer_class(self):
        serializer_class = OutletCreateSerializer

        if self.action == 'create':
            serializer_class = OutletCreateSerializer
        elif self.action == 'update_attachments':
            serializer_class = OutletUpdateSerializer
        elif self.action == 'delete_attachments':
            serializer_class = OutletDeleteSerializer
        elif self.action == 'list':
            serializer_class = OutletSerializer
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
            instance = Outlet.objects.filter(owner=owner)
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


class SearchViewSet(generics.ListAPIView):

    queryset = Outlet.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filterset_class = OutletFilter
    filterset_fields = ['title', ]
    serializer_class = OutletSerializer
    permission_classes = [IsAuthenticated, ]