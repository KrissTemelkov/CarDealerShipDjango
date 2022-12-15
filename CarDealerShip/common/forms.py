from django import forms

from CarDealerShip.common.models import Car


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarEditForm(CarCreateForm):
    pass


class CarDeleteForm(CarCreateForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }),
            'model': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }),
            'year': forms.NumberInput(
                attrs={
                    'readonly': 'readonly',
                }),
            'imageURL': forms.URLInput(
                attrs={
                    'readonly': 'readonly',
                }),
            'price': forms.NumberInput(
                attrs={
                    'readonly': 'readonly',
                }),
        }

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance