from rest_framework import generics, viewsets
from .models import Student, Section, Membership
from .serializers import StudentSerialize, SectionSerializer, MembershipSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly, IsStudentOrReadOnly
from django.db.models import Prefetch


class StudentAPIList(generics.ListCreateAPIView):
    serializer_class = StudentSerialize
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_queryset(self):
        queryset = Student.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset


class StudentAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialize
    permission_classes = (IsStudentOrReadOnly, )


class StudentAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialize
    permission_classes = (IsAdminOrReadOnly, )


class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    def get_queryset(self):
        queryset = Section.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    
    serializer_class = MembershipSerializer
