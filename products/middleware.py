from django.utils.deprecation import MiddlewareMixin
from .models import UserProfile

class ProductMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            profile, created = UserProfile.objects.get_or_create(user=request.user)
            request.user.userprofile = profile