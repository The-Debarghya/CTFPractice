import re
import json

file1 = open("syslog", 'r')
lines1 = file1.readlines()

file2 = open("auth.json", 'r')
jsonLog = file2.read()
jsonArrayS = json.loads(jsonLog)["serial"]



r = re.compile("usb \d-\d: SerialNumber: ([0-9A-F]+)")
for l in lines1:
  m = r.search(l, 0)
  if m is not None:
    hexcode = m.group(1)
    if hexcode not in jsonArrayS:
        print(hexcode)
