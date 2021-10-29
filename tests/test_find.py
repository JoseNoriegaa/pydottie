# Unittest
from unittest import TestCase

# Utilties
from src.pydottie import find


class FindTestCase(TestCase):
    """
    Test cases for the find function.
    """

    def setUp(self) -> None:
        self.data = {
            'foo': {
                'bar': 'baz'
            },
            'zoo': 'lander'
        }

    def test_get_the_first_level_values(self):
        """
        Should get first-level values.
        """

        self.assertEqual(find('zoo', self.data), 'lander')

    def test_get_nested_level_values(self):
        """
        Should get nested-level values.
        """

        self.assertEqual(find('foo.bar', self.data), 'baz')
