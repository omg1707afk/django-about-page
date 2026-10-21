from django.test import TestCase, Client
import json

class DealershipAPITests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_all_dealers(self):
        response = self.client.get("/dealers/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("dealers", data)
        self.assertGreaterEqual(len(data["dealers"]), 1)

    def test_dealer_by_id(self):
        response = self.client.get("/dealers/1/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("dealer", data)
        self.assertEqual(data["dealer"]["id"], 1)

    def test_dealers_by_state(self):
        response = self.client.get("/dealers/by-state/?state=Kansas")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("dealers", data)
        self.assertEqual(data["dealers"][0]["state"], "Kansas")

    def test_car_makes(self):
        response = self.client.get("/car-makes/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("car_makes", data)

    def test_sentiment_analysis(self):
        payload = {"review": "Fantastic services"}
        response = self.client.post(
            "/analyze-review/",
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["sentiment"], "Positive")
