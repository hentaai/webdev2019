def mutate_string(string, position, character):
    p = int(position)
    str = string[:p] + character + string[p+1:]
    return str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)