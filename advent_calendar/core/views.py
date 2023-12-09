from django.views.generic import ListView
from .models import Day


class IndexView(ListView):
    model = Day
    template_name = 'core/index.html'
    context_object_name = 'days'
