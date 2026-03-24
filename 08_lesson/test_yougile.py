from YougileApi import YougileApi


api = YougileApi("https://ru.yougile.com/api-v2")


def test_get_company_list():
    response = api.get_company_list()
    assert response.status_code == 200

    json_data = response.json()
    assert json_data['content'][0]['name'] == 'Skypro Tests'
    print(json_data)


def test_create_key():
    response = api.get_company_list()
    assert response.status_code == 200


def test_create_project_positive():
    response = api.get_company_list()
    assert response.status_code == 200


def test_create_project_negative():
    response = api.get_company_list()
    assert response.status_code == 400


def test_put_project_positive():
    response = api.get_company_list()
    assert response.status_code == 200


def test_put_project_negative():
    response = api.get_company_list()
    assert response.status_code == 400


def test_search_project_id_positive():
    response = api.get_company_list()
    assert response.status_code == 200


def test_search_project_id_negative():
    response = api.get_company_list()
    assert response.status_code == 401
