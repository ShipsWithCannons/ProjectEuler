def get_biggest_palindrome():
    biggest_palindrome = 0

    for i in xrange(100, 999):
        for j in xrange(100, 999):
            product = i * j
            product_string = str(product)
            if product_string == product_string[::-1]:
                if product >= biggest_palindrome:
                    biggest_palindrome = product
    return biggest_palindrome

print get_biggest_palindrome()
