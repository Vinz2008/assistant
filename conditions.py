import wikipedia
import python_weather
import asyncio
import requests
import json
def possibility(text):
    answer = ""
    if text == "Hello":
        answer = "Hi"
    elif text == "How are you ?":
        answer = "Fine"
    elif text.startswith("What is the weather in") == True:
        place = text[22:] 
        async def getweather():
            client = python_weather.Client(format=python_weather.IMPERIAL)
            weather = await client.find(place)
            answer = weather.current.temperature
            await client.close()

        loop = asyncio.get_event_loop()
        loop.run_until_complete(getweather())


    elif text.startswith("Who is") == True:
        #wikipedia_text = wikipedia.suggest(text)
        text2 = text[6:]
        wikipedia_search = wikipedia.summary(text2, sentences=2)
        answer = wikipedia_search
    elif text.startswith("What is my ip") == True:
        ipadress = requests.get("https://api64.ipify.org/?format=json").json()
        answer = ipadress["ip"]
    elif text.startswith("What is") == True:
        text2 = text[7:]
        wikipedia_search = wikipedia.summary(text2,sentences=2)
    elif True:
        print(text)
        answer = "I don't understand"
    return answer

