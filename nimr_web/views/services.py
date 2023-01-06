from django.views.generic import TemplateView


class ResearchProjectView(TemplateView):
    template_name = f"nimr_web/bootstrap/services/research_project.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MonitoringEvaluationView(TemplateView):
    template_name = f"nimr_web/bootstrap/services/monitor_evaluation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EditingProofView(TemplateView):
    template_name = f"nimr_web/bootstrap/services/edit_proof.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PolicyAdvocacyView(TemplateView):
    template_name = f"nimr_web/bootstrap/services/policy_advocacy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ScientificSupportiveView(TemplateView):
    template_name = f"nimr_web/bootstrap/services/scientific_supportive.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



