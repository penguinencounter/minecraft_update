import requests
import re

r = requests.get("https://www.minecraft.net/en-us/download/server/")
print("Server download page:", r.status_code)

regex = r"(https://.*?\.jar)"

test_str = r.text

matches = re.finditer(regex, test_str, re.MULTILINE)

theURI = ""

for matchNum, match in enumerate(matches, start=1):
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        theURI = match.group(groupNum)

print(theURI)
download = requests.get(theURI)
print("Server:", download.status_code)
with open("server.jar", "wb") as f:
    f.write(download.content)

