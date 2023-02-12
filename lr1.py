a = 20
b = 30
t = 40
x = 50
f = 60
i_2 = 70

def main() -> None:

    print(f'a = {a}, type(a): {type(a)}\nb = {b}, type(b): {type(b)}\nt = {t}, type(t): {type(t)}\
        \nx = {x}, type(x): {type(x)}\nf = {f}, type(f): {type(f)}\ni_2 = {i_2}, type(i_2): {type(i_2)}')

def func() -> None:

    R_x = a*b + b/t - x + f*i_2
    print(f'R_x = {R_x}')
    print(f'Type of R_x: {type(R_x)}')

if __name__ == "__main__":
    main()
    func()
