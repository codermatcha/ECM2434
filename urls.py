from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings

# Test homepage
def home(request):
    return HttpResponse("Hello, Django is running!")

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin Panel
    path('', home),  # Homepage at '/'
    path('', include('bingo.urls')),  # Includes all API routes from the 'bingo' app
]

# Debug Toolbar (Only if settings.DEBUG is True)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
