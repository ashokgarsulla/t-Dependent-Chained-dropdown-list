from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Address, City, District,State
from .forms import AddressForm
from django.shortcuts import render

class AddressCreateView(CreateView):
    model = Address
    form_class = AddressForm
    success_url = reverse_lazy('home')

class AddressListView(ListView):
    model = Address
    form_class = AddressForm
    context_object_name = 'addresses'

def load_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'address/state_dropdown_list_options.html', {'states': states})

def load_districts(request):
    district_id = request.GET.get('state')
    districts = District.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'address/district_dropdown_list_options.html', {'districts': districts})
def load_cities(request):
    city_id = request.GET.get('district')
    cities = City.objects.filter(city_id=city_id).order_by('name')
    return render(request, 'address/city_dropdown_list_options.html', {'cities': cities})