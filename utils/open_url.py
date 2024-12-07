import webbrowser

def openUrl(url: str):
    """ Open the specified URL in the default web browser. """
    webbrowser.open(url)

if __name__ == '__main__':
    openUrl('https://google.com')