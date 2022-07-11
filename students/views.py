from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics, viewsets, filters
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from .models import Student, Section, Membership
from .serializers import StudentSerialize, SectionSerializer, MembershipSerialize
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly


class StudentAPIList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialize
    permission_classes = (IsAuthenticatedOrReadOnly, )


class StudentAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialize
    permission_classes = (IsAuthenticatedOrReadOnly, )


class StudentAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialize
    permission_classes = (IsAdminOrReadOnly, )


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerialize


# class MembershipTest(GenericAPIView, CreateModelMixin, DestroyModelMixin):
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         sections = [section.name for section in Section.objects.all()]
#         for section in sections:
#             print(Student.objects.filter(sections__name=section))
#         return Response(sections)
