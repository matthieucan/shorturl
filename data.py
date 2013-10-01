def base_conv(n, input_base=10, output_base=62):
    """
    Converts a number n from base input_base to base output_base.
    
    The following symbols are used to represent numbers:
    0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    """
    raise NotImplementedError()

def store(url):
    """
    Calculates the encoded version of an url and stores the couple.

    Returns url (string) if success, raises Exception otherwise.
    """
    raise NotImplementedError()

def retrieve(encoded_url):
    """
    Retrieves an url, given its encoded version.
    Returns an url (string) if success, raises Exception otherwise.
    """
    raise NotImplementedError()
