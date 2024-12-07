from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Patient(AbstractUser):
    is_a_patient = models.BooleanField(default=True, blank=True)
    is_staff = models.BooleanField(default=False, blank=True)
    is_superuser = models.BooleanField(default=False, blank=True)

    groups = models.ManyToManyField(
        'auth.Group', related_name='patients_group', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='patient_permissions', blank=True
    )

    def save(self, *args, **kwargs):
        self.username = self.first_name
        super(Patient, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
