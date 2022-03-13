from app import app
import urllib.request,json
from .models import Quotes

base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_quotes():
    get_quotes_url = base_url.format()

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_obj = None
        if get_quotes_response:
            author = get_quotes_response.get('author')
            quote = get_quotes_response.get('quote')

            quote_obj = Quotes(author,quote)

    return quote_obj
