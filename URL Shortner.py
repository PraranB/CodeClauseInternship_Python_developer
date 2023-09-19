import pyshorteners

# api key from :-  https://cutt.ly/
API_key = 'API_key'
#API_URL = 'https://cutt.ly/api/api.php'

url = input('Enter the URL you wish to Shorten >> ')
name = input('Give your link a name :-   ')

def urlshortner(url):
    link = pyshorteners.Shortener(api_key = API_key).cuttly.short(url)
    print('\n',name)
    print('Here is your shortened URL :-\t', link)

urlshortner(url)