from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework import response, status

from authentication.models import Client, Manager
from authentication.permissions import IsOwner, IsOwnerOrPost, IsOwnerOrReadOnly
from authentication.serializers import UserSerializer, ClientSerializer, ManagerSerializer


class UserAPIView(GenericAPIView):

    permission_classes = (IsOwnerOrPost,)
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user
        serializer = self.serializer_class(user)

        return response.Response({'user': serializer.data})

    def put(self, request):
        user = request.user
        serializer = self.serializer_class(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManagerAPIView(RetrieveUpdateAPIView):

    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    lookup_field = 'pk'


class ClientAPIView(GenericAPIView):

    permission_classes = (IsOwner,)
    serializer_class = ClientSerializer

    def get_object(self, id):
        try:
            return Client.objects.get(user_id=id)

        except Client.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        client = self.get_object(request.user.id)
        serializer = self.serializer_class(client)

        return response.Response({'client': serializer.data})

    def put(self, request):
        client = self.get_object(request.user.id)
        serializer = self.serializer_class(client, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
