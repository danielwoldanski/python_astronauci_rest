from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, View

from astronauts.forms import AstronautForm
from astronauts.models import Astronaut


class AstronautView(TemplateView):
    template_name = 'astronauts/view.html'

    def get_context_data(self, **kwargs):
        return {
            'astronauts': Astronaut.objects.all()
        }


class ContactAddForm(TemplateView):
    template_name = 'astronauts/form.html'

    def get_context_data(self, **kwargs):
        form = AstronautForm()
        return locals()


class AstronautAddFail(TemplateView):
    template_name = 'astronauts/fail.html'


class AstronautAddSuccess(TemplateView):
    template_name = 'astronauts/success.html'


class AstronautAddView(View):
    def get(self, request):
        return HttpResponseRedirect(reverse('astronaut-add-fail'))

    def post(self, request):
        form = AstronautForm(request.POST)

        if not form.is_valid():
            return HttpResponseRedirect(reverse('astronaut-add-fail'))

        Astronaut.objects.create(
            first_name=form.cleaned_data.get('first_name'),
            last_name=form.cleaned_data.get('last_name'),
        )

        return HttpResponseRedirect(reverse('astronaut-add-success'))
