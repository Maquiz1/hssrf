from django.views.generic import TemplateView


class DPScientificServicesView(TemplateView):
    template_name = f"nimr_web/bootstrap/dp_scientific_services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context