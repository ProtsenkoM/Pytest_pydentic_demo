import pytest

from src.generators.player_localization import PlayerLocalization
from src.enums.user_enums import Statuses


@pytest.mark.parametrize("status", [
    *Statuses.list()
])
def test_something(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize("balance_value", [
    "100",
    "0",
    "-10",
    "absd"
])
def test_generate_with_balance(balance_value, get_player_generator):
    print(get_player_generator.set_balance(balance_value).build())


@pytest.mark.parametrize("delete_key", [
    "account_status",
    "balance",
    "localize",
    "avatar"
])
def test_check_mandatory(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


@pytest.mark.parametrize("localization, loc", [
    ("fr", "fr_FR")
])
def test_check_change_local(get_player_generator, localization, loc):
    object_to_send = get_player_generator.update_inner_value(['localize', localization],
                                                             PlayerLocalization(loc).set_number(15).build()).build()
    print(object_to_send)
