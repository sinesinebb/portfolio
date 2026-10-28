from django.core.management.base import BaseCommand
from django.db import transaction

from portfolio.models import (
    Certification, Education, Experience, Language, Profile, Project, Skill, SkillCategory,
)

PROFILE = {
    "full_name": "Yassine Mouhamed Bakouetila",
    "title": "Développeur Full Stack · ML Engineer · Data Scientist",
    "tagline": "Je conçois des applications web et des systèmes d'IA, de la donnée brute jusqu'au produit.",
    "bio": (
        "Développeur full stack diplômé d'une Licence professionnelle en génie logiciel (mention Bien). "
        "Au Ministère de la Santé et de la Population, j'ai participé au développement d'une application "
        "web et mobile de suivi des femmes enceintes (Nuxt.js, Laravel, Flutter, MySQL) et géré une base "
        "de données volumineuse.\n\n"
        "Passionné par l'IA et le NLP, j'ai co-conçu un moteur de recherche à scoring hybride (BM25, "
        "CamemBERT, PageRank) en microservices, évalué selon la méthodologie TREC, ainsi qu'un assistant "
        "virtuel basé sur un modèle de 6,74 milliards de paramètres.\n\n"
        "Rigoureux et méthodique, je vise un poste de Développeur full stack, ML Engineer ou Data Scientist."
    ),
    "location": "Brazzaville, Congo",
    "email": "mouhamed.bakouetila@gmail.com",
    "available": True,
}

SKILLS = [
    ("Data Science & Machine Learning", "brain", [
        ("Python (pandas, NumPy)", "advanced"),
        ("scikit-learn", "good"), ("PyTorch", "good"), ("TensorFlow", "good"),
        ("Matplotlib", "good"), ("Seaborn", "good"),
        ("NLP : CamemBERT", "good"), ("BM25 / TF-IDF", "good"),
        ("Embeddings", "good"), ("LLM", "good"),
    ]),
    ("Développement", "code", [
        ("Nuxt.js", "good"), ("Vue.js 3", "good"), ("JavaScript", "good"),
        ("HTML / CSS", "good"), ("Tailwind CSS", "good"),
        ("Django", "good"), ("FastAPI", "good"), ("Laravel", "good"),
        ("Flutter", "good"), ("C++", "good"),
    ]),
    ("Données & infrastructure", "database", [
        ("SQL", "good"), ("MySQL", "good"), ("PostgreSQL", "good"), ("Elasticsearch", "good"),
        ("Docker", "good"), ("Kafka", "good"), ("Redis", "good"), ("Nginx", "good"),
        ("Git / GitHub", "good"), ("Excel", "good"),
        ("Kubernetes", "basic"), ("Linux", "basic"), ("AWS", "basic"),
        ("Power BI", "basic"), ("Prometheus", "basic"), ("Grafana", "basic"),
    ]),
    ("Réseaux & support", "network", [
        ("CCNA", "basic"), ("Support technique & dépannage", "basic"),
    ]),
]

EXPERIENCES = [
    {
        "role": "Data Manager",
        "company": "District Sanitaire de Makelekele",
        "start": "Janvier 2026", "end": "Juin 2026",
        "highlights": (
            "Suivi et gestion des données de 9 formations sanitaires du district, avec saisie dans DHIS2\n"
            "Rédaction de TDR (termes de référence) et résolution des problèmes techniques du district"
        ),
        "tech": "DHIS2, Excel",
    },
    {
        "role": "Développeur Full Stack",
        "company": "Ministère de la Santé et de la Population — DTIC",
        "start": "Octobre 2024", "end": "Septembre 2025",
        "highlights": (
            "Participation à la conception d'une application de suivi des femmes enceintes dans les "
            "hôpitaux, permettant au ministère de récupérer ces données\n"
            "Frontend Nuxt.js et Tailwind CSS, backend Laravel, version mobile Flutter ; tests des API avec Postman\n"
            "Gestion d'une base de données MySQL volumineuse et appui technique aux utilisateurs"
        ),
        "tech": "Nuxt.js, Tailwind CSS, Laravel, Flutter, MySQL, Postman",
    },
    {
        "role": "Gestionnaire de base de données",
        "company": "Ministère de la Santé — District Sanitaire de Bacongo",
        "start": "Novembre 2020", "end": "Septembre 2021",
        "highlights": (
            "Accueil, enregistrement et gestion des données des bénéficiaires du site de vaccination "
            "COVID-19 (environ 10 personnes par jour)\n"
            "Conseils aux personnes vaccinées sur les précautions à suivre après le vaccin ; contact direct avec le public"
        ),
        "tech": "",
    },
]

PROJECTS = [
    {
        "title": "Search.dev",
        "slug": "search-dev",
        "subtitle": "Moteur de recherche spécialisé en informatique · Mémoire de Licence (codéveloppé)",
        "period": "Septembre 2025 – Octobre 2026 · soutenu le 10 octobre 2026",
        "summary": (
            "Moteur de recherche en architecture microservices avec un scoring hybride "
            "BM25 + CamemBERT + PageRank, évalué selon la méthodologie TREC."
        ),
        "description": (
            "Search.dev est un moteur de recherche dédié aux contenus informatiques, conçu dans le cadre de "
            "mon mémoire de Licence. Le système est découpé en microservices (crawler, scraper, indexation, "
            "NLP, PageRank, scheduler, recherche) qui communiquent via Kafka, avec Elasticsearch pour l'index "
            "et Redis pour le cache.\n\n"
            "Le classement combine un score lexical (BM25), un score sémantique (embeddings CamemBERT) et un "
            "score d'autorité (PageRank). L'interface est développée en Nuxt.js, l'API de recherche en FastAPI, "
            "et les espaces utilisateur et administrateur sous Django, le tout derrière Nginx et supervisé "
            "avec Prometheus et Grafana."
        ),
        "highlights": (
            "Microservices : crawler, scraper, indexing, NLP, PageRank, scheduler, search\n"
            "Elasticsearch, Redis, Kafka ; supervision Prometheus / Grafana\n"
            "Scoring hybride BM25 + CamemBERT + PageRank\n"
            "Frontend Nuxt.js, API FastAPI, espaces utilisateur et admin sous Django, Nginx"
        ),
        "metrics": [
            {"label": "Precision@10", "value": "0.75"},
            {"label": "Recall@20", "value": "0.68"},
            {"label": "F1-score", "value": "0.71"},
            {"label": "Temps de réponse moyen", "value": "280 ms"},
        ],
        "tech": "Python, FastAPI, Django, Nuxt.js, Elasticsearch, Kafka, Redis, CamemBERT, Nginx, Docker, Prometheus, Grafana",
        "featured": True,
    },
    {
        "title": "Syne",
        "slug": "syne",
        "subtitle": "Assistant virtuel pour professionnels · Projet personnel",
        "period": "",
        "summary": (
            "Assistant multilingue qui conseille et accompagne les professionnels dans leurs projets, "
            "basé sur le modèle Syne_coder_V2 (6,74 milliards de paramètres)."
        ),
        "description": (
            "Syne est un assistant virtuel pensé pour les professionnels : il les conseille et les "
            "accompagne dans la conduite de leurs projets. Il repose sur le modèle Syne_coder_V2, un LLM "
            "de 6,74 milliards de paramètres, et fonctionne en plusieurs langues."
        ),
        "highlights": (
            "Modèle Syne_coder_V2 : 6,74 milliards de paramètres\n"
            "Assistant multilingue\n"
            "Conseil et accompagnement de projets professionnels"
        ),
        "metrics": [{"label": "Paramètres", "value": "6,74 Md"}],
        "tech": "Python, LLM, PyTorch, Prompt Engineering",
        "featured": True,
    },
    {
        "title": "Gestion de stock de supermarché",
        "slug": "gestion-stock-supermarche",
        "subtitle": "Application web · Projet personnel",
        "summary": "Application de gestion de stock pour un supermarché.",
        "description": "Application web permettant de suivre les produits et l'état du stock d'un supermarché.",
        "highlights": "",
        "metrics": [],
        "tech": "HTML, CSS, Tailwind CSS, JavaScript, MySQL",
        "featured": False,
    },
    {
        "title": "Site de restauration",
        "slug": "site-restauration",
        "subtitle": "Site web · Projet personnel",
        "summary": "Site vitrine pour un restaurant.",
        "description": "Site web de présentation d'un restaurant.",
        "highlights": "",
        "metrics": [],
        "tech": "HTML, CSS, Tailwind CSS, JavaScript, MySQL",
        "featured": False,
    },
]

EDUCATION = [
    {
        "degree": "Licence professionnelle — Génie logiciel",
        "school": "CFI-CIRAS",
        "period": "2021 – 2024 · Soutenance : 10 octobre 2026",
        "details": (
            "Mention Bien (soutenance : 17/20). Mémoire : « Conception et création d'un moteur de "
            "recherche spécialisé en informatique »."
        ),
    },
    {
        "degree": "Python et Django",
        "school": "Centre de formation MoyiTech (cours du soir)",
        "period": "Septembre 2022 – Janvier 2023",
        "details": "",
    },
    {
        "degree": "Data Science",
        "school": "Centre de formation MoyiTech (cours du soir)",
        "period": "Août 2019 – Novembre 2021",
        "details": "",
    },
    {
        "degree": "Baccalauréat, série D",
        "school": "Lycée Savorgnan de Brazza",
        "period": "2020 – 2021",
        "details": "Mention Assez Bien.",
    },
]

CERTIFICATIONS = [
    "CCNA1",
    "Scrapy : Python Web Scraping & Crawling",
    "Agentic AI, Gen AI, Prompt Engineering and RL",
    "Data Science et Machine Learning",
    "Docker & Kubernetes",
    "Vue JS 3",
]

LANGUAGES = [
    ("Français", "Langue maternelle"),
    ("Anglais", "Intermédiaire (formation suivie)"),
]


class Command(BaseCommand):
    help = "Remplit la base avec le contenu du CV (remplace le contenu existant)."

    @transaction.atomic
    def handle(self, *args, **options):
        for model in (Profile, SkillCategory, Experience, Project, Education, Certification, Language):
            model.objects.all().delete()

        Profile.objects.create(**PROFILE)

        for i, (name, icon, skills) in enumerate(SKILLS):
            cat = SkillCategory.objects.create(name=name, icon=icon, order=i)
            Skill.objects.bulk_create(
                Skill(category=cat, name=n, level=lvl, order=j) for j, (n, lvl) in enumerate(skills)
            )

        for i, data in enumerate(EXPERIENCES):
            Experience.objects.create(order=i, **data)
        for i, data in enumerate(PROJECTS):
            Project.objects.create(order=i, **data)
        for i, data in enumerate(EDUCATION):
            Education.objects.create(order=i, **data)
        for i, name in enumerate(CERTIFICATIONS):
            Certification.objects.create(name=name, order=i)
        for i, (name, level) in enumerate(LANGUAGES):
            Language.objects.create(name=name, level=level, order=i)

        self.stdout.write(self.style.SUCCESS("Contenu du CV importé."))
