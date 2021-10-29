# Unittest
from unittest import TestCase

# Utilities
from src.pydottie import set_value


class SetValueTestCase(TestCase):
    """
    Test cases for the set value function.
    """

    def setUp(self) -> None:
        self.data = {
            'foo': {
                'bar': 'baa'
            }
        }

    def test_set_nested_values_on_existing_structure(self):
        """
        Should set nested values on existing structure.
        """
        set_value(self.data, 'foo.bar', 'baz')
        self.assertEqual(self.data['foo']['bar'], 'baz')

    def test_create_nested_structure_if_not_existing(self):
        """
        Should create nested structure if not existing.
        """

        set_value(self.data, 'level1.level2', 'foo')
        self.assertEqual(self.data['level1']['level2'], 'foo')
        self.assertIsInstance(self.data['level1'], dict)

    def test_handle_setting_a_nested_value_on_an_undefined_value(self):
        """
        Should handle setting a nested value on an undefined value (should convert undefined to object).
        """

        data = {
            'values': None
        }

        set_value(data, 'values.level1', 'foo')
        self.assertEqual(data['values']['level1'], 'foo')

    def test_set_with_a_list_path(self):
        """
        Should be able to set with a list path.
        """

        data = {
            'some.dot.containing': {
                'value': 'foo'
            }
        }

        set_value(data, ['some.dot.containing', 'value'], 'razzamataz')
        self.assertEqual(data['some.dot.containing']['value'], 'razzamataz')

    def test_raise_exception_when_setting_a_nested_value_on_an_existing_key_with_a_non_object_value(self):
        """
        Should raise an exception when setting a nested value on an existing key with a non-object value.
        """

        self.assertRaises(ValueError, set_value, self.data, 'foo.bar.baz', 'someValue')

    def test_overwrite_a_nested_non_object_value_on_force(self):
        """
        Should overwrite a nested non-object value on force: true.
        """

        set_value(self.data, 'foo.bar.baz', 'someValue', force=True)
        self.assertEqual(self.data['foo']['bar']['baz'], 'someValue')
