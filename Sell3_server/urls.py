from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from Sell3_server import settings

# Uncomment the next two lines to enable the admin:
from django.contrib.auth.views import login, logout
from sell3.views import default, default2
from weixin.views import handleRequest


admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', default),
                       url(r'^main$', default2),
                       url(r'^oa/', include('sell3.urls')),
                       url(r'^shimingweixin/', handleRequest),
                       # url(r'^$', 'Sell3_server.views.home', name='home'),
                       # url(r'^Sell3_server/', include('Sell3_server.foo.urls')),
                       (r'^accounts/login/$', login, {'template_name': 'login.html'}),
                       (r'^accounts/logout/$', logout, {'template_name': 'logout.html'}),
                       (r'^accounts/profile/$', default),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
)
