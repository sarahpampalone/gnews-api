from functools import cache

@cache
def xnum(num, cat):
    # https://docs.python.org/3/library/json.html
    # This library will be used to parse the JSON data returned by the API.
    import json
    # https://docs.python.org/3/library/urllib.request.html#module-urllib.request
    # This library will be used to fetch the API.
    import urllib.request

    apikey = "79c76560c3197501d56bf153b6bf5eb1"
    match cat:
        case "1": category = "general"
        case "general": category = cat
        case "2": category = "world"
        case "world" : category = cat
        case "3": category = "nation"
        case "nation": category = cat
        case "4": category = "business"
        case "business": category = cat
        case "5": category = "technology"
        case "technology": category = cat
        case "6": category = "entertainment"
        case "entertainment": category = cat
        case "7": category = "sports"
        case "sports": category = cat
        case "8": category = "science"
        case "science": category = cat
        case "9": category = "health"
        case "health": category = cat
        case _: category = "general"
    url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=en&country=us&max={num}&apikey={apikey}"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
        articles = data["articles"]

        for i in range(len(articles)):
            # articles[i].title
            print(f"\n{i+1}. {articles[i]['title']}")
            # articles[i].description
            print(f"{articles[i]['description']}")
            # You can replace {property} below with any of the article properties returned by the API.
            # articles[i].{property}
            # print(f"{articles[i]['{property}']}")

            # Delete this line to display all the articles returned by the request. Currently only the first article is displayed.
            #break