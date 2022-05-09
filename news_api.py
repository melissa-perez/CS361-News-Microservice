# Date: 5/8/2022
# Description: The news_api.py file is a microservice application
# that connects to the News API for news information. It can be used
# to retrieve specific keywords from the search.

from flask import Flask, request, render_template
import requests
import json

PORT = 8081
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/everything'
DEV_API_KEY = '39897659371e4fb59a57206a15e77a1d'
DEFAULT_SEARCH_TERM = 'finance'
WRITE_TO_FILE = True

app = Flask(__name__)


@app.route('/')
def get_everything_news(term=DEFAULT_SEARCH_TERM):
    """
    Runs a query on the everything section from the NewsAPI.
    The default search term is used to return
    :return: JSON object
    """
    text = [NEWS_API_ENDPOINT,
            '?',
            'q=',
            term,
            '&apiKey=',
            DEV_API_KEY
            ]
    built_url = ''.join(text)
    response = requests.get(built_url)
    news_articles = response.json()

    if WRITE_TO_FILE:
        write_json_into_file(json.dumps(news_articles))

    return news_articles


@app.route('/search_term', methods=['POST'])
def image_page():
    """
    Returns a single random image in a new page from form data. To use, set your form to submit as POST and make sure
    you have an input with the name "url" in your form.
    """
    url = request.form.get("url")
    website = image_to_return(url)
    return render_template('imageresult.html', data=website)


def write_json_into_file(res):
    """
    Writes the returned JSON object into a text file if
    the option is enabled.
    :return: bool
    """
    with open('sample.json', 'w') as outfile:
        outfile.write(res)
    return True


if __name__ == '__main__':
    app.run(port=PORT, debug=True)
