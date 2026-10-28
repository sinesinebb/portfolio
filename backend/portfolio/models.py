from django.db import models


class Ordered(models.Model):
    order = models.PositiveIntegerField("ordre", default=0)

    class Meta:
        abstract = True
        ordering = ["order"]


class Profile(models.Model):
    """Informations générales (une seule instance)."""

    full_name = models.CharField("nom complet", max_length=120)
    title = models.CharField("titre", max_length=200)
    tagline = models.CharField("accroche", max_length=255, blank=True)
    bio = models.TextField("présentation")
    location = models.CharField("localisation", max_length=120, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField("téléphone", max_length=40, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    avatar = models.ImageField(upload_to="profile/", blank=True)
    cv_file = models.FileField("CV (PDF)", upload_to="cv/", blank=True)
    available = models.BooleanField("disponible", default=True)

    class Meta:
        verbose_name = "profil"

    def __str__(self):
        return self.full_name


class SkillCategory(Ordered):
    name = models.CharField("nom", max_length=100)
    icon = models.CharField("icône", max_length=50, blank=True, help_text="Nom d'icône (ex. brain, code, database, network)")

    class Meta(Ordered.Meta):
        verbose_name = "catégorie de compétences"
        verbose_name_plural = "catégories de compétences"

    def __str__(self):
        return self.name


class Skill(Ordered):
    class Level(models.TextChoices):
        ADVANCED = "advanced", "Avancé"
        GOOD = "good", "Bon"
        BASIC = "basic", "Notions"

    category = models.ForeignKey(SkillCategory, related_name="skills", on_delete=models.CASCADE)
    name = models.CharField("nom", max_length=100)
    level = models.CharField("niveau", max_length=10, choices=Level.choices, default=Level.GOOD)

    class Meta(Ordered.Meta):
        verbose_name = "compétence"

    def __str__(self):
        return self.name


class Experience(Ordered):
    role = models.CharField("poste", max_length=150)
    company = models.CharField("structure", max_length=200)
    start = models.CharField("début", max_length=40)
    end = models.CharField("fin", max_length=40, blank=True)
    highlights = models.TextField("missions", help_text="Une mission par ligne")
    tech = models.CharField("technologies", max_length=255, blank=True, help_text="Séparées par des virgules")

    class Meta(Ordered.Meta):
        verbose_name = "expérience"

    def __str__(self):
        return f"{self.role} — {self.company}"


class Project(Ordered):
    title = models.CharField("titre", max_length=150)
    slug = models.SlugField(unique=True)
    subtitle = models.CharField("sous-titre", max_length=255, blank=True)
    period = models.CharField("période", max_length=100, blank=True)
    summary = models.TextField("résumé")
    description = models.TextField("description détaillée", blank=True)
    highlights = models.TextField("points clés", blank=True, help_text="Un point par ligne")
    metrics = models.JSONField("métriques", default=list, blank=True, help_text='Ex. [{"label": "Precision@10", "value": "0.75"}]')
    tech = models.CharField("technologies", max_length=255, blank=True, help_text="Séparées par des virgules")
    repo_url = models.URLField("dépôt", blank=True)
    demo_url = models.URLField("démo", blank=True)
    image = models.ImageField(upload_to="projects/", blank=True)
    featured = models.BooleanField("mis en avant", default=False)

    class Meta(Ordered.Meta):
        verbose_name = "projet"

    def __str__(self):
        return self.title


class Education(Ordered):
    degree = models.CharField("diplôme", max_length=200)
    school = models.CharField("établissement", max_length=200)
    period = models.CharField("période", max_length=100)
    details = models.TextField("détails", blank=True)

    class Meta(Ordered.Meta):
        verbose_name = "formation"
        verbose_name_plural = "formations"

    def __str__(self):
        return self.degree


class Certification(Ordered):
    name = models.CharField("nom", max_length=200)
    issuer = models.CharField("organisme", max_length=150, blank=True)
    url = models.URLField(blank=True)

    class Meta(Ordered.Meta):
        verbose_name = "certification"

    def __str__(self):
        return self.name


class Language(Ordered):
    name = models.CharField("langue", max_length=60)
    level = models.CharField("niveau", max_length=120)

    class Meta(Ordered.Meta):
        verbose_name = "langue"

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField("nom", max_length=120)
    email = models.EmailField()
    subject = models.CharField("objet", max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField("reçu le", auto_now_add=True)
    is_read = models.BooleanField("lu", default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "message de contact"
        verbose_name_plural = "messages de contact"

    def __str__(self):
        return f"{self.name} — {self.subject or 'Sans objet'}"
