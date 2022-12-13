from enum import Enum

from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models

from CarDealerShip.core.validators import validate_only_letters


class ChoicesEnumMixin:

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do Not Show'


class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 3
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 3
    MAX_LEN_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )
