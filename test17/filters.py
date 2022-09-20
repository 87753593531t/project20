from django_filters import rest_framework as filters

from test17.models import Employee, Outlet, Visit


class EmployeeFilter(filters.FilterSet):
    name_from = filters.CharFilter(field_name='name', lookup_expr='gte')
    name_to = filters.CharFilter(field_name='name', lookup_expr='lte')

    class Meta:
        model = Employee
        fields = ('name_from', 'name_to')


class OutletFilter(filters.FilterSet):
    title_from = filters.CharFilter(field_name='title', lookup_expr='gte')
    title_to = filters.CharFilter(field_name='title', lookup_expr='lte')

    class Meta:
        model = Outlet
        fields = ('title_from', 'title_to')


class VisitFilter(filters.FilterSet):
    outlet_from = filters.CharFilter(field_name='outlet', lookup_expr='gte')
    outlet_to = filters.CharFilter(field_name='outlet', lookup_expr='lte')

    class Meta:
        model = Visit
        fields = ('outlet_from', 'outlet_to')

