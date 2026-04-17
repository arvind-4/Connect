"""Models for the accounts app."""

from __future__ import annotations

import uuid
from typing import Any

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)
from django.db import models


class MyAccountManager(BaseUserManager):
    """Account manager."""

    def create_user(self, email: str, password: str | None = None) -> Account:
        """Create a user."""
        if not email:
            msg = "Users must have an Emaill address"
            raise ValueError(msg)
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str | None = None) -> Account:
        """Create a superuser."""
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    """Account model."""

    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True
    )
    email = models.EmailField(max_length=60, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = MyAccountManager()

    def __str__(self) -> str:
        """Return a string representation of the account."""
        return f"{self.email} | {self.id}"

    def has_perm(self, *_args: tuple[Any, ...], **_kwargs: dict[str, Any]) -> bool:
        """Has permission."""
        return self.is_admin

    def has_module_perms(
        self, *_args: tuple[Any, ...], **_kwargs: dict[str, Any]
    ) -> bool:
        """Has module permissions."""
        return True
