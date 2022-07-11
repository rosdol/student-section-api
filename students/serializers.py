from rest_framework import serializers
from .models import Student, Section, Membership


class StudentSerialize(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        depth = 1


class MembershipSerialize(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'
        depth = 1
        

# class MembershipSerializer(serializers.Serializer):
#     student = serializers.PrimaryKeyRelatedField()
#     section = serializers.PrimaryKeyRelatedField()
#     date_joined = models.DateField(default=datetime.date.today)
    

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        students = MembershipSerialize()

        fields = (
            'id',
            'name',
            'students',
        )
        depth = 1
