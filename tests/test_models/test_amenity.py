#!/usr/bin/python3
"""
Unit tests for Amenity class
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    """
    Test class for Amenity
    """

    def setUp(self):
        """
        Sets up a new instance of Amenity for testing
        """
        self.value = Amenity()

    def test_name(self):
        """
        Tests that name attribute is a string
        """
        new = self.value
        self.assertEqual(type(new.name), str)

    def test_str(self):
        """
        Tests that the __str__ method returns a string
        """
        new = self.value
        self.assertEqual(type(str(new)), str)

    def test_to_dict(self):
        """
        Tests that the to_dict method returns a dictionary
        """
        new = self.value
        self.assertEqual(type(new.to_dict()), dict)
