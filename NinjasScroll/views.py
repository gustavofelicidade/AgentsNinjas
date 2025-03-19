from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NinjaScrollSerializer

class NinjaScrollView(APIView):
    def get(self, request):
        data = {'mensagem': 'Bem-vindo ao Ninja Scroll!'}
        serializer = NinjaScrollSerializer(data)
        return Response(serializer.data)
