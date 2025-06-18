from rest_framework.throttling import SimpleRateThrottle


class APIKeyRateThrottle(SimpleRateThrottle):
    scope = "apikey"

    def get_cache_key(self, request, view):
        api_key = request.headers.get("X-API-KEY")
        if not api_key:
            return None
        return self.cache_format % {"scope": self.scope, "ident": api_key}
