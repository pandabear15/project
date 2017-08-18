from rest_framework import serializers
from contributors.models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ('id', 'created', 'name', 'val1', 'val2', 'val3', 'books', 'class_of')

