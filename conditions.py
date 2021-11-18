import wikipedia
import python_weather
import asyncio
def possibility(text):
    answer = "I don't understand"
    if text == "How are you ?":
        answer = "Fine"
    if text.startswith("What is the weather in") == True:
        place = text[22:] 
        async def getweather():
            client = python_weather.Client(format=python_weather.IMPERIAL)
            weather = await client.find(place)
            answer = weather.current.temperature
            await client.close()

        loop = asyncio.get_event_loop()
        loop.run_until_complete(getweather())


    else:
        #wikipedia_text = wikipedia.suggest(text)
        wikipedia_search = wikipedia.summary(text, entences=2)
        answer = wikipedia_search
    return answer
