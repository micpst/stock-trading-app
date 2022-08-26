from __future__ import annotations

from typing import Any
from uuid import uuid4

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models import CharField, EmailField, UUIDField
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    use_in_migrations = True

    def create(self, **kwargs: Any) -> User:
        return self.create_user(**kwargs)

    def create_user(self, email: str, password: str, **extra_fields: Any) -> User:
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: str, **extra_fields: Any) -> User:
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Custom user model.
    """

    username = None
    email = EmailField(_("email address"), unique=True)
    first_name = CharField(_("first name"), max_length=150)
    last_name = CharField(_("last name"), max_length=150)
    public_id = UUIDField(default=uuid4, unique=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = (
        "first_name",
        "last_name",
    )

    class Meta:
        db_table = "tbl_user"
