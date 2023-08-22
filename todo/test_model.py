from django.test import TestCase
from .models import Items


class TestModel(TestCase):
    def test_done_field_defaults_to_false(self):
        item = Items.objects.create(name="Test todo item")
        self.assertFalse(item.done)