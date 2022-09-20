from rest_framework import serializers
from rest_framework.validators import ValidationError

from test17.models import Employee, Outlet
from test17.serializers import EmployeeSerializer, EmployeeCreateSerializer

class OutletSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Outlet
        fields = (
            'id',
            'title',
            'employee'
        )


class OutletCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Outlet
        fields = (
            'id',
            'title',
            'employee'
        )
        read_only_fields = ('id', )




class OutletUpdateSerializer(serializers.ModelSerializer):
    employee = EmployeeCreateSerializer()

    class Meta:
        model = Outlet
        fields =(
            'id',
            'title',
            'employee'
        )
        read_only_fields = ('id', )

    def validate(self, attrs):

        if 'employee' in attrs:
            new_employee_data = attrs['employee']
            if 'name' not in new_employee_data.keys() and \
                    'phone' not in new_employee_data.keys():
                raise ValidationError('Something wrong with cat field info!')

            employee = Employee.objects.filter(id=self.context['id']).first()
            if employee:
                attrs['employee'] = employee
                attrs['new_employee_data'] = dict(new_employee_data)

        return attrs

    def update(self, instance, validated_data):
        employee = Employee.objects.filter(id=self.context['id']).first
        if 'new_employee_data' in validated_data.keys():
            new_employee_data = self.validated_data['new_employee_data']
            updated_employee = EmployeeCreateSerializer(employee)
            updated_employee.update(employee, new_employee_data)
            del validated_data['employee']
        return super().update(instance, validated_data)


class OutletDeleteSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Outlet
        fields =(
            'id',
            'title',
            'employee'
        )
        read_only_fields = ('id', )

    def delete_attachments(self):
        request = self.context['request']
        attachments = request.data['attachments']
        queryset = Outlet.objects.all()
        for attachment_data in attachments:
            instance = queryset.get(pk=attachment_data['id'])
            instance.delete()