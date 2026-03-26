from filecmp import clear_cache
import os
import requests
from twilio.rest import Client

account_sid = os.getenv(ACC_ID)
auth_token = os.getenv(AUTH_TOKEN)
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#     to='+18777804236'
# )
# print(message.sid)
api_key = "f16d9e1a20b73883e3c780705f5a17c0"
lat = 36.69842
lon =  137.36258
# response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}")
# print(response.status_code)
# data = response.json()
# print(data)

#------OR----------
end_point = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4,
}

res = requests.get(end_point,params=weather_params)
print(res.status_code)
weather_data = res.json()
# print(weather_data)

will_rain = False
for j in weather_data["list"]:

    for k in j["weather"] :

        if k["id"] < 700 :
            will_rain = True

if will_rain: #will print it only one time instead of
    # printing more inside upper loop
    client = Client(account_sid,auth_token)

    message = client.messages.create(
        body="This messsage is to inform you that it will be pouring outside so don't forget to bring an umbrella",
        from_="+16402145594",
        to= "+919622073762"
    )
    #
    # message = client.messages.create(
    #     from_="whatsapp:+16402145594",
    #     body="It's going to rain today. Remember to bring an umbrella",
    #     to="whatsapp:+919622073762"
    # )
    print(message.status)
