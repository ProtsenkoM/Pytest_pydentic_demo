import pytest

from src.baseclasses.response import Response
from src.schemas.user import User

from src.schemas.computer import Computer
from examples import computer

def test_getting_users_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    #print(make_number)


@pytest.mark.development
@pytest.mark.production
@pytest.mark.skip('[Issue]')
def test_another():
    """
    In that test we try to check that 1 equal 2
    """
    assert 1 == 1


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('a', -1, None)

])
def test_calculation(first_value, second_value, result, calculate):
    """
    In that test we are testing calculation with different values
    """
    assert calculate(first_value, second_value) == result


def test_pydantic_object():
    comp = Computer.parse_obj(computer)
    print(comp.detailed_info)




