import requests
import json
import pandas as pd

def rowTitle():
  return ["firstname", "lastname", "age",
          "race", "gender", "lat", "lng",
          "address", "community", "incidenttype",
          "date", "month", "year", "time",
          "linkURL"]

def returnRow(c):
  return [
      c['gsx$firstname']['$t'],
      c['gsx$lastname']['$t'],
      c['gsx$age']['$t'],
      c['gsx$raceethnicity']['$t'],
      c['gsx$gender']['$t'],
      c['gsx$lat']['$t'],
      c['gsx$lng']['$t'],
      c['gsx$incidentaddress']['$t'],
      c['gsx$communityarea']['$t'],
      c['gsx$incidenttype']['$t'],
      c['gsx$dateofincident']['$t'],
      c['gsx$month']['$t'],
      c['gsx$year']['$t'],
      c['gsx$timeofincident']['$t'],
      c['gsx$storylink']['$t']
  ]

r = requests.get("https://spreadsheets.google.com/feeds/list/1S6d6BQ3OjTq2QEUDDM4WkSqr0C4kxxqakX8n70eGyYs/1/public/values?alt=json")
listrows = json.loads(r.text)["feed"]["entry"]

rawdata = [returnRow(k) for k in listrows]
df = pd.DataFrame(rawdata, columns=rowTitle())
