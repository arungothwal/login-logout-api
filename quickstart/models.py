import jwt
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


from django.contrib.auth.base_user import BaseUserManager
from rest_framework_jwt.utils import jwt_payload_handler

from tutorial import settings


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(_('active'), default=True)
    is_active = models.BooleanField(_('active'), default=True)
    salary = models.FloatField(_('salary'), max_length=100, blank=True, default=0.0)
    Address=models.CharField(max_length=30,blank=True)
    dob=models.DateField(max_length=10,blank=True,null=True)
    phone_no=models.IntegerField(blank=True,null=True)
 #   friend=models.ManyToManyField('MyUser', blank=None, null=True, default=None)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name


    def create_jwt(self):
        """Function for creating JWT for Authentication Purpose"""
        payload = jwt_payload_handler(self)
        token = jwt.encode(payload, settings.SECRET_KEY)
        auth_token = token.decode('unicode_escape')
        return auth_token

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Friend(models.Model):
    REQUEST_STATUS = (
        ("APPROVE", "APPROVE"),
        ("REJECT", "REJECT"),
        ("PENDING", "PENDING"),
    )
    created = models.DateTimeField(auto_now_add=True, editable=False,blank=True,null=True)
    user_to = models.ForeignKey(MyUser, related_name="friendship_creator_set",on_delete=models.CASCADE)
    user_from = models.ForeignKey(MyUser, related_name="friend_set",on_delete=models.CASCADE,blank=True,null=True)
    request_status = models.CharField(max_length = 20, choices = REQUEST_STATUS, default = 'PENDING')

    def __str__(self):
        return str(self.user_from) + ' - ' + str(self.user_to)



