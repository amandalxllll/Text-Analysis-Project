import urllib.request

url = 'https://www.gutenberg.org/cache/epub/37106/pg37106.txt'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
    print(text) # for testing

url = 'https://www.gutenberg.org/files/1260/1260-0.txt'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
    print(text) # for testing