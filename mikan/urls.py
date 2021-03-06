"""mikan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from rest_framework.routers import DefaultRouter
import members.views
import work.views

router = DefaultRouter()
router.register("members",
                members.views.MemberViewSet,
                basename="member")
router.register("teams",
                members.views.TeamViewSet,
                basename="team")
router.register("activities",
                work.views.ActivityViewSet,
                basename="activity")
router.register("workplaces",
                work.views.WorkplaceViewSet,
                basename="workplace")
router.register("works",
                work.views.WorkViewSet,
                basename="work")
router.register("workplans",
                work.views.WorkPlanViewSet,
                basename="workplan")

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin', admin.site.urls),
    url(r'^auth/', include('authentication.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^register/', include('registration.urls')),
    url(r'^recover/', include('recover.urls')),
    url(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT
    }),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^api-auth/', include('rest_framework.urls')),
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]
