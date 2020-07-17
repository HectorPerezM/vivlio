"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import url

# external
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Vivlio API",
      default_version='v1',
      description="Vivlio API",
   ),
   public=True,
)


urlpatterns = [
    url(r'^admin/', include('loginas.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('users.urls'), name='users'),
    url(r'^api/', include('books.urls'), name='books'),
    url(r'^api/', include('library.urls'), name='library'),
    url(r'^api/', include('tags.urls'), name='tags'),
    url('api/books/', include('books.urls_es', namespace='books')),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^doc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]
