def s(n, m):
    return n * m


try:
    a = int(input("введите длину стены "))
    b = int(input("введите ширину стены "))
    c = int(input("введите высоту стены "))
    d = int(input("введите ширину окна "))
    e = int(input("введите высоту окна "))
    f = int(input("введите ширину двери "))
    g = int(input("введите высоту двери "))
    k = int(input("введите ширину обоев "))
    l = int(input("введите длину обоев "))
except ValueError:
    print('неверные данные')
else:
    walls = 2*(s(c, b)+s(c, a)) - (2*s(d, e)+s(f, g))
    wallpaper = s(k, l)
    n = round(walls/wallpaper)
    if n < walls/wallpaper:
        n += 1

    print("количество рулонов для обклейки = ", n)
