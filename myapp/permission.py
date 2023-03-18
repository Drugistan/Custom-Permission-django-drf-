from rest_framework.permissions import BasePermission, SAFE_METHODS
from datetime import datetime, timedelta
from django.utils import timezone


""" 
        In has_object_permission Check is username is same which user login into application and check is_superuser 
"""

class UserCustomPermission(BasePermission):

    def has_permission(self, request, view):          
        if request.user.is_authenticated:
            return True
        
    
    def has_object_permission(self, request, view, obj):

        username = None
        for user in obj:
            if str(user.username) == str(request.user):
                username = user.username 

        if str(username) == str(request.user):
            return True
        else:
            if request.method in SAFE_METHODS and request.user.is_superuser:
                return True
        return False
    

""" if created object save more then 5 minutes then they don't have permission to access application"""

class ExpiredObjectSuperuserOnly(BaseException):

    message = "This User is expired."

    def has_permission(self, request, view):
 
        if request.user.is_authenticated:
            return True

    def check_object_is_expired(self, request , obj):
        created = None
        expired = timezone.make_aware(datetime.now() - timedelta(minutes=5))
        for user in obj:
            if str(user.username) == str(request.user):
                created = user.created_at
        return created < expired
    
    def has_object_permission(self, request, view, obj):

        if self.check_object_is_expired(request, obj) and not request.user.is_superuser:
            return False
        
        else:
            return True