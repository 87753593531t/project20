from rest_framework import serializers


from test17.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'phone'
        )


class EmployeeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'phone',

        )


class EmployeeUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'phone',

        )

    def update_attachments(self):
        request = self.context['request']
        attachments = request.data['attachments']
        queryset = Employee.objects.all()
        for attachment_data in attachments:
            instance = queryset.get(pk=attachment_data['id'])
            instance.update()


class EmployeeDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'phone',

        )

    def delete_attachments(self):
        request = self.context['request']
        attachments = request.data['attachments']
        queryset = Employee.objects.all()
        for attachment_data in attachments:
            instance = queryset.get(pk=attachment_data['id'])
            instance.delete()