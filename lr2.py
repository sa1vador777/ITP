def main() -> str:
    count = 0
    a = ['a', ['b', 'c'], ['d', 'e'], 'f', 'g']
    for x in a:
        if type(x) == list:
            count += 1
    return str(count)

if __name__ == '__main__':
    print(main())
