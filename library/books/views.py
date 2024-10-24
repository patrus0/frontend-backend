from rest_framework.generics import CreateAPIView

from .serializers import *


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookSerializer
