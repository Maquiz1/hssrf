from django.views.generic import TemplateView


class WhoWeAreView(TemplateView):
    template_name = f"nimr_web/bootstrap/about/who_we_are.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class WhatWeDoView(TemplateView):
    template_name = f"nimr_web/bootstrap/about/what_we_do.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class OurTeamView(TemplateView):
    template_name = f"nimr_web/bootstrap/about/team.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class OurPartnersView(TemplateView):
    template_name = f"nimr_web/bootstrap/about/partners.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
