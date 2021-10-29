# Unittest
from unittest import TestCase

# Utilities
from src.pydottie import get


class GetTestCase(TestCase):
    """
    Test cases for the get function.
    """

    def setUp(self) -> None:
        self.data = {
            'foo': {
                'bar': 'baz'
            },
            'zoo': 'lander',
            'false': {
                'value': False
            },
            'null': {
                'value': None
            },
            'nullvalue': None,
            'nested.dot': {
                'key': 'value'
            }
        }

    def test_return_none_if_value_is_none(self):
        """
        Should return None if value is None.
        """

        self.assertIsNone(get(None, 'foo'))

    def test_return_none_if_key_is_none(self):
        """
        Should return None if key is None.
        """

        self.assertIsNone(get(self.data, None))

    def test_get_first_level_values(self):
        """
        Should get first-level values.
        """

        self.assertEqual(get(self.data, 'zoo'), 'lander')

    def test_get_nested_level_values(self):
        """
        Should get nested-level values.
        """

        self.assertEqual(get(self.data, 'foo.bar'), 'baz')

    def test_return_none_if_not_found(self):
        """
        Should return None if not found.
        """

        self.assertIsNone(get(self.data, 'foo.zoo.lander'))

    def test_return_false_values_properly(self):
        """
        Should return false values properly.
        """

        self.assertFalse(get(self.data, 'false.value'))

    def test_return_none_if_accessing_a_child_property_of_a_null_value(self):
        """
        Should return None if accessing a child property of a null value.
        """

        self.assertIsNone(get(self.data, 'nullvalue.childProp'))
        self.assertIsNone(get(self.data, 'null.value.childProp'))

    def test_return_none_if_accessing_a_child_property_of_a_string_value(self):
        """
        Should return None if accessing a child property of a string value.
        """

        self.assertIsNone(get(self.data, 'foo.bar.baz.yapa'))

    def test_get_nested_values_with_keys_that_have_dots(self):
        """
        Should get nested values with keys that have dots.
        """

        path = ['nested.dot', 'key']

        self.assertEqual(get(self.data, path), 'value')
        self.assertEqual(path, ['nested.dot', 'key'])
