import requests

r = requests.get('https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236')
print(r.status_code)
