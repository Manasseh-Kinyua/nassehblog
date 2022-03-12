from app import app
import urllib.request,json
from .models import quotes

Quotes = quotes.Quotes

base_url = app.config['QOUTES_API_BASE_URL']
