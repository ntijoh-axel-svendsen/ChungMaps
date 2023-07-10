from django.http import Http404

from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from .permissions import IsMapScannerOrReadOnly

from MapExplorer.models import MinecraftBlock
from .serializers import MinecraftBlockSerializer

from django.contrib.auth.models import User
from .serializers import UserSerializer


class MinecraftBlockList(ListCreateAPIView):
    serializer_class = MinecraftBlockSerializer
    permission_classes = [IsMapScannerOrReadOnly]

    def get_queryset(self):
        dimension = self.kwargs.get('dimension', None)
        return MinecraftBlock.objects.all() if dimension is None else MinecraftBlock.objects.filter(dimension=dimension)

    def perform_create(self, serializer):
        serializer.save(lastModifiedBy=self.request.user)


class MinecraftBlockDetail(RetrieveUpdateAPIView):
    serializer_class = MinecraftBlockSerializer
    permission_classes = [IsMapScannerOrReadOnly]

    def get_object(self):
        pk = self.kwargs.get('pk', None)
        dimension = self.kwargs.get('dimension', None)
        x = self.kwargs.get('x', None)
        y = self.kwargs.get('y', None)
        z = self.kwargs.get('z', None)

        try:
            return MinecraftBlock.objects.get(pk=pk)
        except MinecraftBlock.DoesNotExist:
            try:
                return MinecraftBlock.objects.get(dimension=dimension, x=x, y=y, z=z)
            except MinecraftBlock.DoesNotExist:
                raise Http404

    def perform_update(self, serializer):
        serializer.save(lastModifiedBy=self.request.user)


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
