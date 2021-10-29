# Unittest
from unittest import TestCase

# Utilitites
from src.pydottie import paths


class PathsTestCase(TestCase):
    """
    Test cases for the paths function.
    """


    def test_raise_exception_for_non_objects(self):
        """
        Test that the function raises an exception for non-objects.
        """

        self.assertRaises(TypeError, paths, 'no object')

    def test_return_keys_of_flat_object(self):
        """
        Test that the function returns the keys of a flat object.
        """

        self.assertEqual(paths({ 'a': 1, 'b': 2 }), ['a', 'b'])

    def test_return_paths_of_deeply_nested_object(self):
        """
        Test that the function returns the paths of a deeply nested object.
        """

        obj = {
            'a': 1,
            'b': {
                'c': 2,
                'd': { 'e': 3 }
            }
        }

        self.assertEqual(paths(obj), ['a', 'b.c', 'b.d.e'])

    def test_include_keys_of_null_objects(self):
        """
        Test that the function includes keys of null objects.
        """

        obj = {
            'nonNullKey': 1,
            'nullKey': None
        }

        self.assertEqual(paths(obj), ['nonNullKey', 'nullKey'])
