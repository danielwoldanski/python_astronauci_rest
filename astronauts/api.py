from rest_framework.decorators import action
from rest_framework.response import Response

from astronauts.models import Astronaut
from astronauts.serializers import PersonSerializer
from rest_framework import generics, viewsets, renderers


class AstronautList(generics.ListCreateAPIView):
    queryset = Astronaut.objects.all()
    serializer_class = PersonSerializer


class AstronautDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Astronaut.objects.all()
    serializer_class = PersonSerializer


class AstronautViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Astronaut.objects.all()
    serializer_class = PersonSerializer

