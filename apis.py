import requests
# https://docs.python-requests.org/en/latest/

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)

# https://www.webfx.com/web-development/glossary/http-status-codes/
if response.status_code != 200:
    raise Exception("Error")

response.raise_for_status()

data = response.json()
iss = response.json()["iss_position"]
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
iss_tuple = (longitude, latitude)
print(data)
print(iss)
print(longitude)
print(iss_tuple)

response = requests.get("https://api.kanye.rest")
response.raise_for_status()
data = response.json()
quote = data["quote"]
print(quote)
