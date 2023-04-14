from functools import cache

@cache
def title(t):
    import json   # This library will be used to parse the JSON data returned by the API.
    import urllib.request   # This library will be used to fetch the API.

    apikey = "79c76560c3197501d56bf153b6bf5eb1"
    search = t.replace(" ", "+" )
    url = f"https://gnews.io/api/v4/search?q={search}&in=title&lang=en&country=us&max=10&apikey={apikey}"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
        articles = data["articles"]

        for i in range(len(articles)):
            print(f"\n{i+1}. {articles[i]['title']}")   # articles[i].title
            print(f"{articles[i]['description']}")   # articles[i].description
            break
