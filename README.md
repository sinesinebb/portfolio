# Portfolio — Yassine Mouhamed Bakouetila

Portfolio personnel : **Nuxt 3 + Tailwind CSS** (frontend, SSR) et **Django + Django REST Framework** (backend / API).
Tout le contenu (profil, compétences, expériences, projets, formations, certifications, langues) est stocké
en base et modifiable depuis l'admin Django — aucune modification de code nécessaire pour mettre à jour le site.

```
portfolio/
├── backend/            Django + DRF
│   ├── config/         settings, urls
│   └── portfolio/      modèles, API, admin, commande seed_cv
├── frontend/           Nuxt 3
│   ├── pages/          accueil, projets, projets/[slug], contact
│   ├── components/     header, footer, cartes, icônes…
│   └── composables/    useResume (appel API)
└── docker-compose.yml  PostgreSQL + backend + frontend
```

## Démarrage en local

### 1. Backend (port 8000)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate          # Windows : .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py seed_cv           # importe le contenu du CV
python manage.py createsuperuser   # pour accéder à /admin
python manage.py runserver
```

- Admin : http://localhost:8000/admin
- API : http://localhost:8000/api/resume/

### 2. Frontend (port 3000)

```bash
cd frontend
npm install
npm run dev
```

Site : http://localhost:3000

## API

| Méthode | URL                         | Description                       |
|---------|-----------------------------|-----------------------------------|
| GET     | `/api/resume/`              | Tout le CV en une requête         |
| GET     | `/api/projects/`            | Liste des projets                 |
| GET     | `/api/projects/<slug>/`     | Détail d'un projet                |
| POST    | `/api/contact/`             | Formulaire de contact (5 / heure) |

Les messages de contact sont enregistrés (visibles dans l'admin) et envoyés par email à `CONTACT_NOTIFY_EMAIL`
(affichés dans la console en développement ; configurer SMTP dans `.env` pour la production).

## Mettre à jour le contenu

Depuis l'admin Django :
- **Profil** : photo, CV en PDF (bouton « CV » dans le hero), liens GitHub / LinkedIn, téléphone
- **Projets** : liens dépôt / démo, image, métriques (`[{"label": "…", "value": "…"}]`), mise en avant
- **Ordre** d'affichage modifiable directement dans les listes

⚠️ `python manage.py seed_cv` **remplace** le contenu existant par celui du CV : ne l'utilisez qu'à l'initialisation.

## Tests

```bash
cd backend && python manage.py test portfolio
```

## Docker

```bash
docker compose up --build
docker compose exec backend python manage.py seed_cv
docker compose exec backend python manage.py createsuperuser
```

## Déploiement (suggestion)

- **Backend** : Render / Railway (PostgreSQL inclus) avec `DATABASE_URL`, `DJANGO_SECRET_KEY`,
  `DJANGO_DEBUG=False`, `DJANGO_ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS=https://votre-site`.
  Prévoir un stockage persistant (ou S3) pour les fichiers `media/`.
- **Frontend** : Vercel / Netlify avec `NUXT_PUBLIC_API_BASE=https://votre-api/api`.
