from django.conf import settings
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from .views import (
    OurPartnersView, OurTeamView, WhatWeDoView, WhoWeAreView, AboutView, ContactView, View, ContactView,
    ProfileView, DPFinanceView,
    DPHritdView, DPLabView, DPResearchView, DPPmuView, DPMonitoringView, TeamView, PublicationView,)
from .views.kilosa_view import KilosaView

from .views.services import ResearchProjectView, PolicyAdvocacyView, MonitoringEvaluationView,\
    EditingProofView, ScientificSupportiveView

admin.site.site_header = settings.NIMR_MUHIMBILI

app_name = "nimr_web"

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('who_we_are/', WhoWeAreView.as_view(), name='who_we_are'),
    path('what_we_do/', WhatWeDoView.as_view(), name='what_we_do'),
    path('our_team/', OurTeamView.as_view(), name='our_team'),
    path('our_partners/', OurPartnersView.as_view(), name='our_partners'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('profile/<staff>', ProfileView.as_view(), name='profile'),
    path('team/', TeamView.as_view(), name='team'),
    path('department/finance', DPFinanceView.as_view(), name='finance'),
    path('department/hritd', DPHritdView.as_view(), name='hritd'),
    path('department/lab', DPLabView.as_view(), name='lab'),
    path('department/monitoring', DPMonitoringView.as_view(), name='monitoring'),
    path('department/pmu', DPPmuView.as_view(), name='pmu'),
    path('department/research', DPResearchView.as_view(), name='research'),
    path('department/language', DPResearchView.as_view(), name='language'),
    path('department/scientific', DPResearchView.as_view(), name='scientific'),
    path('department/transcription', DPResearchView.as_view(), name='transcription'),
    path('department/data', DPResearchView.as_view(), name='data'),
    path('department/publication_support', DPResearchView.as_view(), name='publication_support'),
    path('publications/', PublicationView.as_view(), name='publications'),
    path('publications/<page>', PublicationView.as_view(), name='publications'),
    path('kilosa/', KilosaView.as_view(), name='kilosa'),
    path('services1/', ResearchProjectView.as_view(), name='services1'),
    path('services4/', PolicyAdvocacyView.as_view(), name='services4'),
    path('services2/', MonitoringEvaluationView.as_view(), name='services2'),
    path('services3/', EditingProofView.as_view(), name='services3'),
    path('services5/', ScientificSupportiveView.as_view(), name='services5'),
    path('', View.as_view(), name='home'),
]

urlpatterns += static(settings.NEWS_URL, document_root=settings.NEWS_ROOT)
