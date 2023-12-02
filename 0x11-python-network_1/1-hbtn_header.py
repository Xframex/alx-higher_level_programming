#!/usr/bin/python3
"""takes in a URL, sends a request to the URL"""

if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    holb_url = argv[1]
    with request.urlopen(holb_url) as response:
        print(response.headers.get("X-Request-Id"))
