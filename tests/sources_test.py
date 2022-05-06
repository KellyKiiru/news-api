import unittest
from app.models import Source

class SourcesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.new_source = Source("0987","BBC World Service")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))