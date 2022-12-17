from django.contrib.auth import get_user_model
from django.core import exceptions, validators
from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()


def validate_min_length(value):
    if len(value) < 2:
        raise exceptions.ValidationError("The username must be a minimum of 2 chars")


def year_validator(value):
    if value < 1980 or value > 2049:
        raise exceptions.ValidationError("Year must be between 1980 and 2049")


class Car(models.Model):
    SPORTS_CAR = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    CAR_TYPES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    type = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        choices=CAR_TYPES,
    )
    model = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(
            validators.MinLengthValidator(2),
        ),
    )
    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            year_validator,
        ),
    )
    imageURL = models.URLField(
        max_length=300,
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(1),
        )
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return slugify(f'{self.model}-{self.id}')

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        self.name = slugify(f'{self.model}-{self.id}')

        if not self.slug:
            self.slug = slugify(f'{self.model}-{self.id}')

        return super().save(*args, **kwargs)



