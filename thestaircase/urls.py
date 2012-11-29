from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',  # View prefix

    url(r'^$',
        TemplateView.as_view(template_name='core/index.html'),
        name='home'),
    url(r'^about/$',
        TemplateView.as_view(template_name='core/about.html'),
        name='about'),
    url(r'^admin/', include(admin.site.urls)),
)
