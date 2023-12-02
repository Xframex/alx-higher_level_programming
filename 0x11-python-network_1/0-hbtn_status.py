#!/usr/bin/python3
"""urllib reponse"""

if __name__ == "__main__":
    import urllib.request as request
    holb_url = "https://intranet.hbtn.io/status"
    with request.urlopen(holb_url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(utf8_content))
