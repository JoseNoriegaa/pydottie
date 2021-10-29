# Unittest
from unittest import TestCase

# Utils
from src.pydottie import flatten


class FlattenTestCase(TestCase):
    """
    Test cases for the flatten function.
    """

    def setUp(self) -> None:
        self.data = {
            'foo': {
                'bar': 'baa',
                'baz': {
                    'foo': 'bar'
                }
            },
            'bar': 'baz'
        }

    def test_basic_nested_structure_without_lists(self):
        """
        Should handle a basic nested structure without lists.
        """

        self.assertEqual(
            flatten(self.data),
            {
                'foo.bar': 'baa',
                'foo.baz.foo': 'bar',
                'bar': 'baz'
            }
        )

    def test_custom_separator(self):
        """
        Should be possible to define your own seperator.
        """

        self.assertEqual(
            flatten(self.data, '_'),
            {
                'foo_bar': 'baa',
                'foo_baz_foo': 'bar',
                'bar': 'baz'
            }
        )
