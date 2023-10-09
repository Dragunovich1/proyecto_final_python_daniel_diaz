from django.contrib import admin
from django.urls import path, include
from members.views import UserRegisterView, UserEditView, PasswordsChangeView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appfierros.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('<int:uid>/password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
