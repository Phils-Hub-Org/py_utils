import webbrowser

def openMailApp(recipient_email):
    """ Opens the default email application and pre-fills the recipient's email address. """
    mailto_link = f'mailto:{recipient_email}'
    webbrowser.open(mailto_link)

if __name__ == '__main__':
    recipient_email = input('Enter the recipient\'s email address: ')
    openMailApp(recipient_email)