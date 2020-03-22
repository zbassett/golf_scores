from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'holes', views.HoleViewSet)
router.register(r'tees', views.TeeViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'rounds', views.RoundViewSet)
router.register(r'scores', views.ScoreViewSet)

router.register(r'event_scores', views.EventScoreViewSet, basename='event_score')
# event_score_list = views.EventScoreViewSet.as_view({
#     'get': 'list'
# })

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path(r'swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/event_score/<int:event_pk>', event_score_list, name='event_score'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
