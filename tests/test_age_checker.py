import pytest
from lib.age_checker import age_checker

"""
the method takes an age that is over 16 years old,
returns a message stating "access granted"
"""
def test_age_checker_user_over_16():
    assert age_checker("2002-12-29") == "access granted"

"""
the method takes an age that is under 16 years old,
returns a message stating "access denied"
"""
def test_age_checker_user_under_16():
    assert age_checker("2011-01-29") == "access denied"

"""
the method takes an invalid date format,
raises an exception "invalid date format"
"""
def test_age_checker_invalid_date_format():
    with pytest.raises(Exception) as e:
        age_checker("01-29-2011")
    error = str(e.value)
    assert error == "invalid date format"