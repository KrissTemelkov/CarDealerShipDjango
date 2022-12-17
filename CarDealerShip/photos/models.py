from django.db import models
from django.core import validators
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from CarDealerShip.common.models import Car

UserModel = get_user_model()


class Photos(models.Model):
    MIN_DESCRIPTION_LENGTH = 5

    caption = models.TextField(
        null=True,
        blank=True,
        max_length=100,
        validators=(
            validators.MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
    )

    name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    tagged_cars = models.ManyToManyField(
        Car,
        blank=True,

    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    imageURL = models.URLField(
        max_length=300,
        null=False,
        blank=False,
    )

    publication_date = models.DateField(
        # Automatically sets current date on `save` (update or create)
        auto_now=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        cars_names = []
        for car in self.tagged_cars.all():
            cars_names.append(car.name)
        self.name = slugify(f'{" ".join(cars_names)}, date-{self.user}')

        return super().save(*args, **kwargs)
