from django import forms
from .models import State, Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('country', 'state', 'district','city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['state'].queryset = State.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['state'].queryset = self.instance.country.state_set.order_by('name')