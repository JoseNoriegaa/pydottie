# Unittest
from unittest import TestCase

# Utilitites
from src.pydottie import transform


class TransformTestCase(TestCase):
    """
    Test cases for the transform function.
    """

    def test_create_a_property_nested_object_from_basic_dottie_notation(self):
        """
        Should create a properly nested object from a basic dottie notated set of keys
        """

        values = {
            'user.name': 'John Doe',
            'user.email': 'jd@foobar.com',
            'user.location.country': 'Zanzibar',
            'user.location.city': 'Zanzibar City'
        }

        transformed = transform(values)

        self.assertIsNotNone(transformed['user'])
        self.assertIsNotNone(transformed['user']['location'])

        self.assertIsInstance(transformed['user'], dict)
        self.assertIsInstance(transformed['user']['location'], dict)

        self.assertEqual(transformed['user']['email'], 'jd@foobar.com')
        self.assertEqual(transformed['user']['location']['city'], 'Zanzibar City')

    def test_mixture_of_nested_properties_and_dottie_notated_set_of_keys(self):
        """
        Should be able to handle a mixture of nested properties and dottie notated set of keys
        """

        values = {
            'user': {
                'name': 'John Doe'
            },
            'user.email': 'jd@foobar.com',
            'user.location.country': 'Zanzibar',
            'user.location.city': 'Zanzibar City',
            'project.title': 'dottie'
        }

        transformed = transform(values)

        self.assertIsNotNone(transformed['user'])
        self.assertIsNotNone(transformed['user']['location'])
        self.assertIsNotNone(transformed['project'])

        self.assertIsInstance(transformed['user'], dict)
        self.assertIsInstance(transformed['user']['location'], dict)
        self.assertIsInstance(transformed['project'], dict)

        self.assertEqual(transformed['user']['email'], 'jd@foobar.com')
        self.assertEqual(transformed['user']['location']['city'], 'Zanzibar City')
        self.assertEqual(transformed['project']['title'], 'dottie')

    def test_base_level_properties_together_with_nested(self):
        """
        Should be able to handle base level properties together with nested
        """

        values = {
            'customer.name': 'John Doe',
            'customer.age': 15,
            'client': 'Lolcat'
        }

        transformed = transform(values)

        self.assertIsNotNone(transformed['client'])
        self.assertIsNotNone(transformed['customer'])

        self.assertIsInstance(transformed['client'], str)
        self.assertIsInstance(transformed['customer'], dict)

        self.assertEqual(transformed['client'], 'Lolcat')
        self.assertEqual(transformed['customer']['name'], 'John Doe')
        self.assertEqual(transformed['customer']['age'], 15)


    def test_null_valued_properties_not_assigning_nested_level_objects(self):
        """
        Should be able to handle null valued properties, not assigning nested level objects
        """

        values = {
            'section.id': 20,
            'section.layout': None,
            'section.layout.id': None,
            'section.layout.name': None
        }

        transformed = transform(values)

        self.assertEqual(transformed['section']['layout'], None)
        self.assertEqual(transformed.get('section.layout.id'), None)
        self.assertEqual(transformed.get('section.layout.name'), None)

    def test_supports_lists(self):
        """
        Should support lists
        """

        values = [
            {
                'customer.name': 'John Doe',
                'customer.age': 15,
                'client': 'Lolcat'
            },
            {
                'client.name': 'John Doe',
                'client.age': 15,
                'customer': 'Lolcat'
            }
        ]

        transformed = transform(values)

        self.assertEqual(transformed[0]['customer']['name'], 'John Doe')
        self.assertEqual(transformed[1]['client']['name'], 'John Doe')

    def test_supports_custom_delimiters(self):
        """
        Should support custom delimiters
        """

        values = {
            'user': {
                'name': 'John Doe'
            },
            'user_email': 'jd@foobar.com',
            'user_location_country': 'Zanzibar',
            'user_location_city': 'Zanzibar City',
            'project_title': 'dottie'
        }

        transformed = transform(values, delimiter='_')

        self.assertIsNotNone(transformed['user'])
        self.assertIsNotNone(transformed['user']['location'])
        self.assertIsNotNone(transformed['project'])

        self.assertIsInstance(transformed['user'], dict)
        self.assertIsInstance(transformed['user']['location'], dict)
        self.assertIsInstance(transformed['project'], dict)

        self.assertEqual(transformed['user']['email'], 'jd@foobar.com')
        self.assertEqual(transformed['user']['location']['city'], 'Zanzibar City')
        self.assertEqual(transformed['project']['title'], 'dottie')
