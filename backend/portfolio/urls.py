from django.urls import path

from . import views

urlpatterns = [
    path("resume/", views.ResumeView.as_view(), name="resume"),
    path("projects/", views.ProjectListView.as_view(), name="project-list"),
    path("projects/<slug:slug>/", views.ProjectDetailView.as_view(), name="project-detail"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]
