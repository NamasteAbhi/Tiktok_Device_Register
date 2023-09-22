import requests

url = "https://tiktok-device-registeration.p.rapidapi.com/Tiktok_Device_Gen/"

rapid_key='' 

querystring = {
  "Proxy":"username:password@host:port",
  "Country":"us"
}

headers = {
	"Content-Type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": rapid_key,
	"X-RapidAPI-Host": "tiktok-device-registeration.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
