from rest_framework import serializers

from astronauts.models import Astronaut


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Astronaut
        fields = '__all__'
