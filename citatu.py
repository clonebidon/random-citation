import requests

def citata_generate():
    response = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=ru")
    data = response.json()
    citata = data["quoteText"]
    author = data["quoteAuthor"]
    return citata, author

citata, author = citata_generate()
print("Случайная цитата:")
print(f'"{citata}" - {author}')
