from rest_framework import serializers


from test17.models import Visit



class VisitSerializer(serializers.ModelSerializer):


    class Meta:
        model = Visit
        fields = (
            'id',
            'created_at',
            'updated_at',
            'outlet'

        )

class VisitCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Visit
        fields = (
            'id',
            'created_at',
            'updated_at',
            'outlet'

        )




class VisitUpdateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Visit
        fields = (
            'id',
            'created_at',
            'updated_at',
            'outlet'

        )

