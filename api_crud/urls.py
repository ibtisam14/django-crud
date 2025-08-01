
from django.contrib import admin
from .swagger import schema_view
from django.urls import include, path

# urls
urlpatterns = [ 
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # 👈 Swagger at root
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]