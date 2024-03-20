"""portfolio_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from homepage.views import home, about_me


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about_me/', about_me, name='about'),
    path('projects/', include('projects.urls')),
]

# --> Para que Django sirva los archivos estáticos en modo DEBUG
urlpatterns += static(
    settings.MEDIA_URL,                 # URL de los archivos estáticos
    document_root=settings.MEDIA_ROOT   # Ruta de los archivos estáticos
)