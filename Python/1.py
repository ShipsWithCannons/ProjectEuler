def multiple_of_3_or_5(n):
    for i in xrange(1, n):
        if not (i % 3) or not (i % 5):
            yield i

def main():
    print sum(multiple_of_3_or_5(1000))

if __name__ == "__main__":
    main()