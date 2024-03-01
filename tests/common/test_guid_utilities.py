from uuid import uuid4
import uuid
import pytest

from ragchat.common.guid_utilities import is_uuid4, to_uuid4

def test_is_uuid4_returns_true_if_guid_is_a_valid_uuid4():
    assert is_uuid4(str(uuid4()))
    assert is_uuid4(uuid4())

def test_is_uuid4_returns_false_if_string_is_not_a_guid():
    assert not is_uuid4("foo")

def test_is_uuid4_returns_false_if_guid_is_not_v4():
    namespace = uuid.NAMESPACE_DNS
    name = "FOO"

    uuid_v3 = uuid.uuid3(namespace, name)

    assert not is_uuid4(uuid_v3)
    
def test_to_uuid4_returns_uuid4_if_string_is_valid():
    assert to_uuid4(str(uuid4()))

def test_to_uuid4_fails_if_string_is_not_valid_uuid():
    with pytest.raises(ValueError):
        to_uuid4("foo")