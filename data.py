def store(url, encoded_url):
    """
    Stores an url and its encoded version.
    Returns True if success, raises Exception otherwise.
    """
    raise NotImplementedError()

def retrieve(encoded_url):
    """
    Retrieves an url, given its encoded version.
    Returns an url (string) if success, raises Exception otherwise.
    """
    raise NotImplementedError()
