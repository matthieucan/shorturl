def base_conv(n, input_base=10, output_base=10):
    """
    Converts a number n from base input_base to base output_base.
    
    The following symbols are used to represent numbers:
    0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    n can be an int if input_base <= 10, and a string otherwise.
    The result will be a string.
    """
    numbers = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    ## base 10 conversion
    n = str(n)
    size = len(n)
    baseten = 0
    
    for i in range(size):
        baseten += numbers.index(n[i]) * input_base ** (size - 1 - i)
    
    ## base output_base conversion
    # we search the biggest number m such that n^m < x
    max_power = 0
    while output_base ** (max_power + 1) <= baseten:
        max_power += 1
    
    result = ""
    for i in range(max_power + 1):
        coeff = baseten / (output_base ** (max_power - i))
        baseten -= coeff * (output_base ** (max_power - i))
        result += numbers[coeff]
    
    return result

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

if __name__ == "__main__":
    assert(base_conv(10) == "10")
    assert(base_conv(42) == "42")
    assert(base_conv(5673576) == "5673576")
    assert(base_conv(10, input_base=2) == "2")
    assert(base_conv(101010, input_base=2) == "42")
    assert(base_conv(43, input_base=10, output_base=2) == "101011")
    assert(base_conv(256**3 - 1, input_base=10, output_base=16) == "ffffff")
    assert(base_conv("d9bbb9d0ceabf", input_base=16, output_base=8) ==
           "154673563503165277")
    assert(base_conv("154673563503165277", input_base=8, output_base=10) ==
           "3830404793297599")
    assert(base_conv(0, input_base=3, output_base=50) == "0")
