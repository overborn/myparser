from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myparser.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'charts.views.index', name='index'),
    url(r'^index/', 'charts.views.index', name='index'),
    url(r'^charts/', 'charts.views.charts', name='charts'),
    url(r'^delete/', 'charts.views.delete_entries', name='delete'),
    url(r'^build_chart/', 'charts.views.build_chart', name='build_chart'),
)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += patterns('',
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     )
