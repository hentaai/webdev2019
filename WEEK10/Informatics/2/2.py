def main():

    year = input()
    n = int(year)
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0 :
        print("YES")
    else :
        print("NO")

if __name__ == '__main__':
    main()