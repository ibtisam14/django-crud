
from django.contrib import admin
from django.urls import include, path
from api_crud.swagger import swagger_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # app routes
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/movies/', include('movies.urls')),
]
# swagger urls
urlpatterns += swagger_urlpatterns