import user_agents
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path, re_path
from rest_framework import permissions, routers
# from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

swagger_info = openapi.Info(
    title="UploadJson API",
    default_version='v1',
    description="""The `swagger-ui` view can be found [here](/cached/swagger).
The `ReDoc` view can be found [here](/cached/redoc).
The swagger YAML document can be found [here](/cached/swagger.yaml)."""
)

SchemaView = get_schema_view(
    validators=['ssv', 'flex'],
    public=True,
    permission_classes=(permissions.AllowAny,)
)

def root_redirect(request):
    user_agent_string = request.META.get('HTTP_USER_AGENT', '')
    user_agent = user_agents.parse(user_agent_string)

    if user_agent.is_mobile:
        schema_view = 'cschema-redoc'
    else:
        schema_view = 'cschema-swagger-ui'

    return redirect(schema_view, permanent=True)


from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('login/', include('login.urls')),
    path('file_upload/', include('filesUpload.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns = [
    re_path(r'^swagger(?P<format>.json|.yaml)$', SchemaView.without_ui(cache_timeout=0),
            name='schema-json'),
    path('swagger/', SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', SchemaView.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('redoc-old/', SchemaView.with_ui('redoc-old', cache_timeout=0), name='schema-redoc-old'),

    re_path(r'^cached/swagger(?P<format>.json|.yaml)$', SchemaView.without_ui(cache_timeout=None),
            name='cschema-json'),
    path('cached/swagger/', SchemaView.with_ui('swagger', cache_timeout=None), name='cschema-swagger-ui'),
    path('cached/redoc/', SchemaView.with_ui('redoc', cache_timeout=None), name='cschema-redoc'),

    path('', root_redirect),
    path('api/v1/', include(urlpatterns)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

