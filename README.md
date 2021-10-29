# PyDottie
PyDottie is a version of [Dottie.js](https://github.com/mickhansen/dottie.js) written in Python 3.

## Table of Contents.

- [Description](#description)
- [Installation](#installation)
- [Basic Usage](#basic-usage)
  - [Get Value](#get)
  - [Set Value](#set-value)
  - [Transform](#transform-object)
    - [Transform with custom delimiter](#with-a-custom-delimiter)
  - [Get paths in dictionary](#get-paths-in-dictionary)
- [Tests](#tests)
- [Credits](#credits)
- [License](#license)

## Description
PyDottie helps you to play with nested keys in dictionaries.

## Installation
```bash
$ pip install pydottie
```

or

```bash
$ pip3 install pydottie
```

## Basic Usage

### Get
Gets nested value, or None if unreachable, or a default value if passed.

```python
# PyDottie
import pydottie

values = {
    'some': {
        'nested': {
            'key': 'foobar',
        }
    },
    'some.dot.included': {
        'key': 'barfoo'
    }
}

# returns 'foobar'
print(pydottie.get(values, 'some.nested.key'))

# returns None
print(pydottie.get(values, 'some.undefined.key'))

# returns 'defaultval'
print(pydottie.get(values, 'some.undefined.key', 'defaultval'))

# returns 'barfoo'
print(pydottie.get(values, ['some.dot.included', 'key']))
```

### Set value
Sets nested value, creates nested structure if needed.

```python
# PyDottie
import pydottie

values = {
    'some': {
        'nested': {
            'key': 'foobar',
        }
    },
    'some.dot.included': {
        'key': 'barfoo'
    }
}

pydottie.set_value(values, 'some.nested.value', 'someValue')

pydottie.set_value(values, ['some.dot.included', 'value'], 'someValue')

# force overwrite defined non-object keys into objects if needed
pydottie.set_value(values, 'some.nested.object', 'someValue', force=True)
```

### Transform object
Transform dictionary from keys with dottie notation to nested objects.

```python
# PyDottie
import pydottie

values = {
  'user.name': 'Gummy Bear',
  'user.email': 'gummybear@candymountain.com',
  'user.professional.title': 'King',
  'user.professional.employer': 'Candy Mountain'
};

transformed = pydottie.transform(values);

print(transformed);
"""
{
    'user': {
        'name': 'Gummy Bear',
        'email': 'gummybear@candymountain.com',
        'professional': {
            'title': 'King',
            'employer': 'Candy Mountain'
        }
    }
}
"""
```

#### With a custom delimiter
```python
# PyDottie
import pydottie

values = {
  'user_name': 'Mick Hansen',
  'user_email': 'maker@mhansen.io'
}
transformed = pydottie.transform(values, delimiter='_');

print(transformed);
"""
{
    'user': {
        'name': 'Mick Hansen',
        'email': 'maker@mhansen.io'
    }
}
"""

```

## Get paths in dictionary

```python
# PyDottie
import pydottie

values = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}

# ['a', 'b.c', 'b.d.e'];
print(pydottie.paths(values))
```

## Tests
Run the unit tests with the next command.
```bash
python3 -m unittest
```

## Credits
Checkout the original source code of dottie.js at https://github.com/mickhansen/dottie.js


## LICENSE
[MIT](https://github.com/JoseNoriegaa/pydottie/blob/main/LICENSE)
