from rest_framework.permissions import BasePermission
from django.conf import settings


class HasAPIKey(BasePermission):
    def has_permission(self, request, view):
        api_key = request.headers.get("Y-API-KEY")
        return api_key == settings.API_KEY
