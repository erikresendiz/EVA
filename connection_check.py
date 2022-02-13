import urllib.request
def connect(host='http://google.com'):
    #makes sure there's and internet connection
    #currently this is useless as it uses googles online voice recognition
    #am trying to get an offline voice recognition to work
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False