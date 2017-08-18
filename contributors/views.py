from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from contributors.models import Contributor
from contributors.serializers import ContributorSerializer


@api_view(['GET'])
def get_contributors(request):
    if request.method == 'GET':
        contributors = Contributor.objects.all()
        serializer = ContributorSerializer(contributors, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)

