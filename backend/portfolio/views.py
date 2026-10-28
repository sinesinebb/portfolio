from django.conf import settings
from django.core.mail import send_mail
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers as s
from .models import (
    Certification, Education, Experience, Language, Profile, Project, SkillCategory,
)


class ResumeView(APIView):
    """Renvoie l'ensemble du CV en une seule requête."""

    def get(self, request):
        profile = Profile.objects.first()
        ctx = {"request": request}
        return Response({
            "profile": s.ProfileSerializer(profile, context=ctx).data if profile else None,
            "skills": s.SkillCategorySerializer(
                SkillCategory.objects.prefetch_related("skills"), many=True
            ).data,
            "experiences": s.ExperienceSerializer(Experience.objects.all(), many=True).data,
            "projects": s.ProjectSerializer(Project.objects.all(), many=True, context=ctx).data,
            "education": s.EducationSerializer(Education.objects.all(), many=True).data,
            "certifications": s.CertificationSerializer(Certification.objects.all(), many=True).data,
            "languages": s.LanguageSerializer(Language.objects.all(), many=True).data,
        })


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = s.ProjectSerializer


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = s.ProjectSerializer
    lookup_field = "slug"


class ContactView(generics.CreateAPIView):
    serializer_class = s.ContactMessageSerializer
    throttle_scope = "contact"

    def perform_create(self, serializer):
        msg = serializer.save()
        send_mail(
            subject=f"[Portfolio] {msg.subject or 'Nouveau message'} — {msg.name}",
            message=f"De : {msg.name} <{msg.email}>\n\n{msg.message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_NOTIFY_EMAIL],
            fail_silently=True,
        )

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({"detail": "Message envoyé, merci !"}, status=status.HTTP_201_CREATED)
