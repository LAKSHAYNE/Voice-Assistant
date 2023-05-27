import wolframalpha
import urllib.parse
import requests
# Taking input from user
question = urllib.parse.quote("Today's Temperature")
print(question)
# App id obtained by the above steps
app_id = '2Y723Y-V9LV23EALL'

# Instance of wolf ram alpha
# client class
s='http://api.wolframalpha.com/v1/spoken?appid='+app_id+'&i='+question
#client = wolframalpha.Client(app_id)
res=requests.get(s)
# Stores the response from
# wolf ram alpha
#res = client.query(question)

# Includes only text from the response
print(res.content.decode('utf-8'),res.status_code)
#answer = next(res.results).text

#print(answer)
