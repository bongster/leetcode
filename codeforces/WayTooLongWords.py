def main():
    number_of_problem = int(input())
    for _ in range(number_of_problem):
        word = input()
        if len(word) <= 10:
            print(word)
        else:
            n = len(word) - 2
            print(word[0] + str(n) + word[-1])


if __name__ == '__main__':
    main()
