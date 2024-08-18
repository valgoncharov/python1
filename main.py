import requests
import pandas


my_requests = requests.get("https://python.org")


print(my_requests)
print(my_requests.text)
print(my_requests.status_code)
