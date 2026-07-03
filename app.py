from flask import Flask, render_template, request
import requests
from config import NEWS_API_KEY

app = Flask(__name__)

BASE_URL = "https://newsapi.org/v2/everything"

@app.route("/", methods=["GET"])
def home():
    query = request.args.get("q", "Artificial Intelligence")

    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 20,
        "apiKey": NEWS_API_KEY,
    }

    articles = []

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        articles = response.json().get("articles", [])
    except Exception as e:
        print(e)

    return render_template(
        "index.html",
        articles=articles,
        query=query
    )

if __name__ == "__main__":
    app.run(debug=True)