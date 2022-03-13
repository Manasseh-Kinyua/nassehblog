# from app import app
# import urllib.request,json
# from .models import quotes

# Quotes = quotes.Quotes

# base_url = app.config['QOUTES_API_BASE_URL']
# base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

# def get_quotes():
#     get_quotes_url = base_url

#     with urllib.request.urlopen(get_quotes_url) as url:
#         get_quotes_data = url.read()
#         get_quotes_response = json.loads(get_quotes_data)

#         author = get_quotes_response[0]['author']
#         quote = (get_quotes_response[0]['quote'])
#     return author,quote
