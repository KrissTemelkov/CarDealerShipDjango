from django import forms

from CarDealerShip.wishlist.models import PhotoWish, PhotoComment
from CarDealerShip.photos.models import Photos


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photos
        exclude = ('publication_date', 'user')


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photos
        exclude = ('publication_date', 'photo', 'user')


class PhotoDeleteForm(PhotoBaseForm):

    class Meta:

        model = Photos
        fields = '__all__'
        exclude = ('publication_date', 'user')
        widgets = {
            'caption': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }),
            'imageURL': forms.URLInput(
                attrs={
                    'readonly': 'readonly',
                }),

        }

    def save(self, commit=True):
        if commit:
            self.instance.tagged_cars.clear()  # many-to-many

            Photos.objects.all() \
                .first().tagged_cars.clear()
            PhotoWish.objects.filter(photo_id=self.instance.id) \
                .delete()  # one-to-many
            PhotoComment.objects.filter(photo_id=self.instance.id) \
                .delete()  # one-to-many
            self.instance.delete()

        return self.instance
