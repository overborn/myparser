from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myparser.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'charts.views.index', name='index'),
    url(r'^index/', 'charts.views.index', name='index'),
    url(r'^charts/', 'charts.views.charts', name='charts'),
    url(r'^delete/', 'charts.views.delete_entries', name='delete'),
)
