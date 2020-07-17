from rest_framework import serializers
from ..models import Log


class LogSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField('get_email_from_author')

    class Meta:
        model = Log
        fields = ['id', 'title', 'description', 'level', 'event', 'origin', 'email', 'ambient', 'archived', 'created_at',]
        read_only_fields = ('archived', 'created_at', 'id', )

    def get_email_from_author(self, log):
        email = log.user.email
        return email


class LogSerializerWithFullAccess(serializers.ModelSerializer):
    email = serializers.SerializerMethodField('get_email_from_author')

    class Meta:
        model = Log
        fields = ['id', 'title', 'description', 'level', 'event', 'origin', 'email', 'ambient', 'archived', 'created_at']
        read_only_fields = ('created_at', 'id')

    def get_email_from_author(self, log):
        email = log.user.email
        return email