from django import forms

from CarDealerShip.wishlist.models import PhotoComment


class PhotoCommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                    'placeholder': 'Add comment...'
                },
            ),
        }


class SearchPhotosForm(forms.Form):
    car_model = forms.CharField(
        max_length=50,
        required=False,
    )
