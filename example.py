def greet(name):
    print("Hello, {0}!".format(name))

print("What's your name?")
name = input()
greet(name)
from dotenv.main import load_dotenv
import os
load_dotenv()
favorite_language = os.environ['LANGUAGE']
my_name = os.environ['MY_NAME']
print (f'favorite language is {favorite_language} and my name is {my_name}')
