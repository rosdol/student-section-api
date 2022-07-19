from rest_framework import serializers
from .models import Student, Section, Membership


class StudentSerialize(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id',
            'name',
            'sections'
        )


class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = (
            'student',
            'section',
            'date_joined',
        )

class SectionSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    class Meta:
        model = Section
        # fields = '__all__'
        fields = (
            'id',
            'name',
            'students',
        )
        depth = 1


    def get_students(self, obj):
        subject_memberships = Membership.objects.filter(section_id=obj.id).values_list('student__id', 'student__name', 'date_joined')
        responde = []
        if subject_memberships:
            for membership in subject_memberships:
                id, name, date_joined = membership
                responde.append({'id': id, 'name': name, 'date_joined': date_joined})
        print(subject_memberships[0] if subject_memberships else None)
        return responde
