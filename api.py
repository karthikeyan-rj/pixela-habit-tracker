import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

def create_user_account(username, token):
    user_params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    res1 = requests.post(url=PIXELA_ENDPOINT, json=user_params )
    return res1.json()

# print(create_user_account("asdfbcghfgkjjhfghdbfvggf", "fsfskjfdsiuerfkjlfdskj"))

def create_graph(username, token, graph_id, name, unit):
    headers = {
        "X-USER-TOKEN": token
    }
    graph_params = {
        "id": graph_id,
        "name": name,
        "unit": unit,
        "type": "int",
        "color": "shibafu"
    }
    graph_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs"
    res2 = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
    return res2.json()
# print(create_graph("asdfbcghfgkjjhfghdbfvggf", "fsfskjfdsiuerfkjlfdskj", "graph-asdfhj", "something", "km")

def add_pixel(username, token, graph_id, date, quantity):
    headers = {
        "X-USER-TOKEN": token
    }
    base = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}"
    body = {"date": date, "quantity": quantity}
    res = requests.post(url=base, json=body, headers=headers)
    return res.json()


def update_pixel(username, token, graph_id, date, quantity):
    headers = {
        "X-USER-TOKEN": token
    }
    base = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}"
    body = {"quantity": quantity}
    res = requests.put(url=f"{base}/{date}", json=body, headers=headers)
    return res.json()


def delete_pixel(username, token, graph_id, date):
    headers = {
        "X-USER-TOKEN": token
    }
    base = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}"
    res = requests.delete(url=f"{base}/{date}", headers=headers)
    return res.json()

if __name__ == "__main__":

    pass