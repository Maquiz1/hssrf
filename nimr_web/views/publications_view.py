from django.conf import settings
from django.views.generic.list import ListView
from nimr_web.models import Publication


class PublicationView(ListView):
    template_name = f"nimr_web/bootstrap/publications.html"

    model = Publication
    paginate_by = settings.NIMR_PAGINATION

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
