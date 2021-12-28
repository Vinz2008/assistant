import time
import conditions
while True:
    text = input(" :")
    if text == "exit":
        break
    else:
        print(conditions.possibility(text)) 
