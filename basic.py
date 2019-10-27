def prime_factorization(original):
    """
    do prime factorization
    Parameters
    ----------
    original : int
        It is done prime factorization

    Returns
    -------
    result : List
        prime factorization result
    """
    result = []
    prime_number = get_prime(original // 2 + 1)
    for i in prime_number:
        n = original
        while True:
            if n % i == 0:
                result.append(i)
                n //= i
            else:
                break
    return result


def get_prime(origin):
    """
    get prime number range of 2 for origin
    Parameters
    ----------
    origin : int
        max number

    Returns
    -------
    prime_number : List
        prime number list range of 2 for origin
    """
    if origin < 2:
        raise ValueError("Please input more than 2 integer")
    prime_number = []
    for i in range(2, origin):
        switch = True
        if not prime_number:
            prime_number.append(i)
            continue
        for n in prime_number:
            if i % n == 0:
                switch = False
                break
        if switch:
            prime_number.append(i)
    return prime_number


def int_input(text):
    """
    Parameters
    ----------
    text : str
        this text print when do input()
    Returns
    -------
    n : int
        input number
    """
    while True:
        try:
            n = int(input("{}\n>>>".format(text)))
            return n
        except ValueError:
            print("please input integer")


if __name__ == "__main__":
    prime_factorization(123)
