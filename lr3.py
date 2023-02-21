def main() -> str:
    with open("data_v2.txt") as file:
        lst = []
        cnt = ""
        for i in file:
            for j in i:
                if j in "1234567890":
                    cnt += j
                else:
                    if cnt!='':
                        if (int(cnt) % 3) != 0:
                            lst.append(cnt)
                            cnt = ""
        return lst

if __name__ == '__main__':
    print(main())
