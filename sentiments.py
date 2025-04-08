from textblob import TextBlob
from colorama import Fore,Style,init
import time
init(autoreset=True)
print("welcome to the chatbot")
print("How are you feeling today?")
print("type exit to leave the chatbot")
while True :
    user_input = input("\n You:")
    if user_input.lower()=="exit":
        print(Fore.YELLOW+"Have a Great day! BYE BYE!")
        break
    print("analyzing sentiment....",end="",flush=True)
    time.sleep(1)
    print(".",end="",flush=True)
    time.sleep(1)
    print(".",flush=True)
    time.sleep(0.5)
    blob= TextBlob(user_input)
    polarity = blob.sentiment.polarity
    if polarity>0:
        print(Fore.GREEN+"sentiment=positivity")
    elif polarity<0:
        print(Fore.RED+"sentiment=negativity or hate")
    else:
        print(Fore.CYAN+"Sentiment=neutral")
        





          


                       
