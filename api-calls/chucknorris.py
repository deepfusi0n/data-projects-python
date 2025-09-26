import requests
import json


#random chuch norris jokes
random_url = "https://api.chucknorris.io/jokes/random"


#list of categories
category_url = "https://api.chucknorris.io/jokes/categories"


#random joke from a specific category
random_cat_url = "https://api.chucknorris.io/jokes/random?category={category}"


#text search
search_url = "https://api.chucknorris.io/jokes/search?query={query}"


'''
Part I
The program should welcome the user by displaying a random chuch norris joke
'''

# Make an API call, and store the response.

r = requests.get(random_url)
print(f"status code: {r.status_code}")

response_dict = r.json()

print(f"Random url: {random_url}")
print(f"Joke: {response_dict["value"]}")



'''
Part II
list the categories to the user and ask to pick a category
'''

r = requests.get(category_url)
category_list = r.json()
print("\nHere are the categories:")

for i in category_list:
    print(i)


'''
Part III
Display a joke based on the category picked by the user
'''

categories = str(input("Choose a category: "))
random_cat_url = f"https://api.chucknorris.io/jokes/random?category={categories}"
r = requests.get(random_cat_url)
category = r.json()
print(category['value'])




'''
Part IV
See if you can find a match for the user's favorite chuck norris joke
by asking the user to enter in a few key words of the joke
'''


