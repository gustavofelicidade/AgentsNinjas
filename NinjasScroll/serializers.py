from rest_framework import serializers

class NinjaScrollSerializer(serializers.Serializer):
    mensagem = serializers.CharField()
