from cryptids.src.model.creature import Creature
import cryptids.src.service.creature as code


sample = Creature(
    name="yeti",
    country="CN",
    area="Himalayas",
    description="Hirsute Himalayan",
    aka="Abominable Snowman",
)


def test_create():
    response = code.create(sample)
    assert response == sample


def test_get_exists():
    response = code.get_one("yeti")
    assert response == sample


def test_get_missing():
    response = code.get_one("nope")
    assert response is None
