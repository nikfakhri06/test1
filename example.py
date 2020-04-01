import requests


def hello():
    print("Howdy!")
    print("Howdy!!!")
    print("Hello there.")


hello()
hello()
hello()

r = requests.get("https://automatetheboringstuff.com")
print(r.status_code)
