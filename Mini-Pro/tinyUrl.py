# code design by aurejien
import urllib.request

def tiny_url(url):
    apiurl = "http://tinyurl.com/api-create.php?url="
    tiny_url = urllib.request.urlopen(apiurl + url).read()
    return tiny_url.decode("utf-8")

print()
print()
print("—————————————————————————————————————————————————————————————————————————————")
print()
url = input("Enter your normal url: \n→    ")
print()
print("—————————————————————————————————————————————————————————————————————————————")
print()
print("Your shorter url: \n→    ", tiny_url(url))
print()
print("—————————————————————————————————————————————————————————————————————————————")
print()
print()