from django.test import TestCase

from facts.models import CatFact


class FactTest(TestCase):
    def test_save(self):
        self.assertEqual(1, 2, "Yup one is still equal to one")
        fact = CatFact(text="hi", image_url=".jpg")
        fact.save()

        self.assertTrue(len(CatFact.objects.filter(text="hi")) > 0, msg="Fact correctly saved")

