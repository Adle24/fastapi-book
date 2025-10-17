import os
import pytest
from cryptids.src.model.creature import Creature
from fastapi import HTTPException
from cryptids.src.data import creature

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="yeti",
        aka="Abominable Snowman",
        country="CN",
        area="Himalayas",
        description="Hapless Himalayan",
    )


def test_create(sample):
    resp = creature.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(HTTPException):
        _ = creature.create(sample)


def test_get_one(sample):
    resp = creature.get_one(sample.name)
    assert resp == sample


def test_get_one_missing():
    with pytest.raises(HTTPException):
        resp = creature.get_one("boxturtle")


def test_modify(sample):
    creature.country = "JP"  # Japan!
    resp = creature.modify(sample.name, sample)
    assert resp == sample


def test_modify_missing():
    thing: Creature = Creature(
        name="snurfle", description="some thing", country="somewhere"
    )
    with pytest.raises(HTTPException):
        _ = creature.modify(thing.name, thing)


def test_delete(sample):
    resp = creature.delete(sample.name)
    assert resp is None


def test_delete_missing(sample):
    with pytest.raises(HTTPException):
        _ = creature.delete(sample.name)
