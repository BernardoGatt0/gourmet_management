from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):

        if not username:
            raise ValueError('O usuário deve ser preenchido')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Usuário', max_length=30, unique=True)
    name = models.CharField('Nome', max_length=255)
    date = models.DateField('Data de Nascimento', blank=True, null=True)
    is_active = models.BooleanField('Está ativo?', default=True)
    is_staff = models.BooleanField('É staff?', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
