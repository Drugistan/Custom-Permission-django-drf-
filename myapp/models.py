from django.db import models
from django.contrib.auth.models import AbstractUser


"""
    I am using this blog to learn Abstract User

    https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html blog

  """

# Create your models here.

class Role(models.Model):
    STUDENT = 1
    TEACHER = 2
    SECRETARY = 3
    SUPERVISOR = 4
    ADMIN = 5
    ROLE_CHOICES = (
        (STUDENT, 'student'),
        (TEACHER, 'teacher'),
        (SECRETARY, 'secretary'),
        (SUPERVISOR, 'supervisor'),
        (ADMIN, 'admin'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
      return self.get_id_display()



class CustomUser(AbstractUser):
    roles = models.OneToOneField(Role, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)




