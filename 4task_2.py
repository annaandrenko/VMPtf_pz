#варіант 2
import requests


url = "https://api.github.com" # URL публічного API
response = requests.get(url) # відправляємо запит до API
data = response.json() # отр дані у форматі JSON

print(data)