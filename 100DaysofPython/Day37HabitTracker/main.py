import requests
import datetime

PASSWORD = PASSWORD
USERNAME = USERNAME

header = {"X-USER-TOKEN": PASSWORD}


def post(json, end_point=""):
    url = "https://pixe.la/v1/users/"
    post = requests.post(url=url+end_point, json=json, headers=header)
    print("Created")
    print(post.request.url)
    print(post.text)


def put(json, end_point=""):
    url = "https://pixe.la/v1/users/"
    put = requests.put(url=url+end_point, json=json, headers=header)
    print("Updated")
    print(put.request.url)
    print(put.text)


def delete(end_point=""):
    url = "https://pixe.la/v1/users/"
    put = requests.delete(url=url+end_point, headers=header)
    print("Deleted")
    print(put.request.url)
    print(put.text)


def create_user(name: str, password: str, agreeToTerms="yes", notMinor="yes"):
    params = {
        "token": PASSWORD,
        "username": USERNAME,
        "agreeTermsofService": agreeToTerms,
        "notMinor": notMinor,
    }
    post(json=params)


def create_graph(user):
    params = {
        "id": "graph1",
        "name": "Cycling",
        "unit": "Mins",
        "type": "int",
        "color": "ajisai"
    }

    post(end_point=f"users/{USERNAME}/graphs", json=params)


def post_pixel(graph, qty):
    today = datetime.datetime.now()
    params = {
        "date": today.strftime("%Y%m%d"),
        "quantity": str(qty),
        # "optionalData": {},
    }
    post(end_point=f"{USERNAME}/graphs/{graph}", json=params)


def update_graph():
    pass


def update_pixel(graph, date, qty):
    params = {
        "quantity": str(qty),
    }
    put(end_point=f"{USERNAME}/graphs/{graph}/{date}",
        json=params)


def delete_graph():
    pass


def delete_pixel(graph, date):
    delete(end_point=f"{USERNAME}/graphs/{graph}/{date}")


# create_user(name=USERNAME, password=PASSWORD,agreeToTerms="yes", notMinor="yes")
# create_graph()
delete_pixel(graph="graph1", date="20201215")
