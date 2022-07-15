from test.test_utils import db_session, client, db_engine
import pytest


def test_get_tags(client):
    response = client.get(
      "/tags"
    )
    assert response.status_code == 200
    assert response.json() == [{'tag_id': 1, 'name': 'Sleep'},
                               {'tag_id': 2, 'name': 'Nutrition'},
                               {'tag_id': 3, 'name': 'Exercise'},
                               {'tag_id': 4, 'name': 'Work'},
                               {'tag_id': 5, 'name': 'Brain'}]


def test_add_tag(client):
    client.post(
      "/tag", json={"name": 'Something'}
    )

    response = client.get(
      "/tags"
    )
    assert response.status_code == 200
    assert 'Something' in [tag['name'] for tag in response.json()]


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, '-v', '--import-mode=importlib']))
