from django.views.generic import TemplateView


class EditProofView(TemplateView):
    template_name = f"nimr_web/bootstrap/edit_proof.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context