from django.contrib import admin

from .models import (
    Certification, ContactMessage, Education, Experience, Language, Profile,
    Project, Skill, SkillCategory,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["full_name", "title", "available"]

    def has_add_permission(self, request):
        return not Profile.objects.exists()


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "order"]
    list_editable = ["order"]
    inlines = [SkillInline]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["role", "company", "start", "end", "order"]
    list_editable = ["order"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "period", "featured", "order"]
    list_editable = ["featured", "order"]
    prepopulated_fields = {"slug": ["title"]}


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["degree", "school", "period", "order"]
    list_editable = ["order"]


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ["name", "issuer", "order"]
    list_editable = ["order"]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "order"]
    list_editable = ["order"]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "created_at", "is_read"]
    list_filter = ["is_read"]
    list_editable = ["is_read"]
    search_fields = ["name", "email", "message"]
    readonly_fields = ["name", "email", "subject", "message", "created_at"]
