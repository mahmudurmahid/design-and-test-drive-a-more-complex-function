# {{Age_Tracker}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def age_checker(dob):
    """
    function denies underage users access and grants access to users of age
    """
    # parameters - date_of_birth (str - "YYYY-MM-DD")
    # returns a message (str - if underage "access denied", if of age "access granted")
    # side effects - none

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
the method takes an age that is over 16 years old,
returns a message stating "access granted"
"""
age_checker("2002-01-29") => "access granted"

"""
the method takes an age that is under 16 years old,
returns a message stating "access denied"
"""
age_checker("2011-01-29") => "access denied"

"""
the method takes an invalid date format,
raises an exception "invalid date format"
"""
age_checker("01-29-2011") => Exception("invalid date format")

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
