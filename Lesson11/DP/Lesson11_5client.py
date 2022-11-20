import http.client
import pprint

a=input("Введіть URL ресурсу ")
b=input("Введіть метод звернення до серверу ")
connection = http.client.HTTPSConnection(a)
connection.request(b, "/")
response = connection.getresponse()
headers = response.getheaders()
code=response.getcode()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint("Code: {}".format(code))
pp.pprint("Header: {}".format(headers))
