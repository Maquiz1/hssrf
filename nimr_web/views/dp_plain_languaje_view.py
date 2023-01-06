from django.views.generic import TemplateView


class DPPlainLanguageView(TemplateView):
    template_name = f"nimr_web/bootstrap/dp_plain_language.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context