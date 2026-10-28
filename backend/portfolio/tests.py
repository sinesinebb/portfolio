from django.core.management import call_command
from django.test import TestCase


class ApiTests(TestCase):
    def setUp(self):
        call_command("seed_cv", stdout=open("/dev/null", "w"))

    def test_resume(self):
        data = self.client.get("/api/resume/").json()
        self.assertEqual(data["profile"]["full_name"], "Yassine Mouhamed Bakouetila")
        self.assertEqual(len(data["projects"]), 4)
        self.assertIsInstance(data["experiences"][0]["highlights"], list)

    def test_project_detail(self):
        data = self.client.get("/api/projects/search-dev/").json()
        self.assertEqual(data["metrics"][0]["value"], "0.75")
        self.assertEqual(self.client.get("/api/projects/inconnu/").status_code, 404)

    def test_contact(self):
        payload = {"name": "Test", "email": "a@b.co", "message": "Bonjour"}
        self.assertEqual(self.client.post("/api/contact/", payload).status_code, 201)
        self.assertEqual(self.client.post("/api/contact/", {"name": "x"}).status_code, 400)
