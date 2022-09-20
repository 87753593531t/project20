from django.urls import path, re_path
from rest_framework.routers import DefaultRouter


from test17.views import EmployeeViewSet, OutletViewSet, VisitViewSet, AnaliticViewSet, SearchViewSet, OutletAnaliticViewSet


router = DefaultRouter()
router.register('employee', EmployeeViewSet)
router.register('outlet', OutletViewSet)
router.register('visit', VisitViewSet)
# router.register('analitic', AnaliticViewSet)

urlpatterns = [
    path('update_attachments/', EmployeeViewSet.as_view({'put': 'list'})),
    path('delete_attachments/', EmployeeViewSet.as_view({'delete': 'delete_attachments'})),
    path('analitic/', AnaliticViewSet.as_view()),
    path('outlets/', SearchViewSet.as_view()),
    path('visits/', OutletAnaliticViewSet.as_view())
    # path('outlets/', OutletViewSet.as_view())
    # re_path(r'^students/(?P<id>[0-9]+)/$', EmployeeViewSet.as_view({'put': 'list'}))
]+router.urls