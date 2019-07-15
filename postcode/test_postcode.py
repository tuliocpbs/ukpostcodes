import pytest

from .exceptions import InvalidPostCode
from .models import UKPostcode


def test_postcode_validation():
    valids = ["GU167HF", "L18JQ", "IP29JP", "ab389NL"]
    invalids = ["GUFFLHF", "LL8JQ", "IP2KJP", "ABXX9NL"] 

    for postcode in valids:
        assert UKPostcode(postcode).postcode in valids
    
    for postcode in invalids:
        with pytest.raises(InvalidPostCode):
            assert UKPostcode(postcode)