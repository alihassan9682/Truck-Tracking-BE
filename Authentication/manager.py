from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import post_save
class User_manager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)
    
    def authenticate(self, email=None, password=None, **kwargs):
        try:
            user = self.get(email=email)
            if user.check_password(password):
                return user
        except self.model.DoesNotExist:
            return None    