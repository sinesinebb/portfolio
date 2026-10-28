from rest_framework import serializers

from .models import (
    Certification, ContactMessage, Education, Experience, Language, Profile,
    Project, Skill, SkillCategory,
)


def split_lines(text):
    return [line.strip() for line in text.splitlines() if line.strip()]


def split_commas(text):
    return [item.strip() for item in text.split(",") if item.strip()]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ["id"]


class SkillSerializer(serializers.ModelSerializer):
    level_label = serializers.CharField(source="get_level_display", read_only=True)

    class Meta:
        model = Skill
        fields = ["name", "level", "level_label"]


class SkillCategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = SkillCategory
        fields = ["name", "icon", "skills"]


class ExperienceSerializer(serializers.ModelSerializer):
    highlights = serializers.SerializerMethodField()
    tech = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = ["id", "role", "company", "start", "end", "highlights", "tech"]

    def get_highlights(self, obj):
        return split_lines(obj.highlights)

    def get_tech(self, obj):
        return split_commas(obj.tech)


class ProjectSerializer(serializers.ModelSerializer):
    highlights = serializers.SerializerMethodField()
    tech = serializers.SerializerMethodField()

    class Meta:
        model = Project
        exclude = ["order"]

    def get_highlights(self, obj):
        return split_lines(obj.highlights)

    def get_tech(self, obj):
        return split_commas(obj.tech)


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ["order"]


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        exclude = ["order"]


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        exclude = ["order"]


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
