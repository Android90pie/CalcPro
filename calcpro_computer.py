import math
from fractions import gcd
from fractions import Fraction
import termcolor

err = termcolor.colored('Ошибка - вы написали неверный символ(ы) ', 'red')

h = input(termcolor.colored('''


⠀⠀⠀⠀

                                                                                                            
                                    S@@                                                                       
                                    S@@                                                                       
                                    S@@                                                                       
                                    S@@                                                                       
     r@@@@@@A        H@@@@@@        S@@          H@@@@@@      @@@  @@@@@r       @@@  H@@@@S      X@@@@@H      
   A@@@@@@@@@@@    @@@@@@@@@@@      S@@       .@@@@@@@@@@@    @@@@@@H@@@@@S     @@@@@@@@@@H    @@@@@@@@@@@    
  2@@A       M              @@@     S@@       @@@       @     @@@H      @@@     @@@,          @@@2      @@@   
  @@@                       ,@@     S@@      M@@r             @@@       G@@S    @@@           @@r       2@@   
  @@@               ,@@@@@@@@@@     S@@      @@@              @@@       S@@G    @@@          ,@@        ,@@   
  @@@              @@@@@@@@@@@@     S@@      @@@              @@@       S@@G    @@@          ,@@        ,@@   
  @@@             @@@        @@     S@@      @@@              @@@       S@@S    @@@           @@        ,@@   
  @@@             @@G        @@     S@@      i@@@             @@@       @@@.    @@@           @@@       @@@   
   @@@H    G@@M   @@@S      @@@      @@M      @@@@,    @@@    @@@@S    @@@@     @@@           S@@@S    @@@r   
    M@@@@@@@@@     A@@@@@@@@A@@      9@@@@     i@@@@@@@@@.    @@@ @@@@@@@@      @@@             @@@@@@@@@     
                                                              @@@                                             
                                                              @@@                                             
                                                              @@@                                             
                                                              @@@  
    
    Что хотите сделать?
    
    p - сложение
    m - вычетание
    t - умножение
    n - деление
    n - наибольший общий делитель 
    l - сложение дробей
    i - нахождение процента от числа 
    b - нахождение числа по проценту
    j - квадратный корень
    s - перевести градусы в радианы ''', 'blue' ))







if h =='n':
   try:
    a = input('Введите первое число ')
    b = input('Введите второе число ')
    d = gcd(int(a),int(b),)
    print(d)
   except:
       ValueError
       print(err)

if h == 'l':
   try:
    x = input('Введите числитель 1 дроби ')
    y = input('Введите знаменатель 1 дроби ')
    s = input('Введите числитель 2 дроби ')
    m = input('Введите знаменатель 2 дроби ')
    g = (Fraction(int(x), int(y)))
    z = (Fraction(int(s), int(m)))
    print(g + z)
   except:
       ValueError
       print(err)

if h == 'i':
   try:
    q = input('Введите число, от которого хотите найти процент ')
    o = input('Введите процент, который хотите найти ')
    w = int(q) * (int(o) / 100)
    print(w)
   except:
       ValueError
       print(err)

if h == 'j':
   try:
    b = input('Число для нахождения квадратного корня ')
    print(math.sqrt(int(b)))
   except:
     ValueError
     print(err)

if h == 's':
   try:
    v = input('Введите градусы (формат дробных чисел 0.0)')
    pro = float(v) * 3.141592653589793 / 180.0
    print(pro)
   except:
       ValueError
       print(err)

if h == 'p':
    try:
     lj = input('Введите первое число ')
     hsh = input('Введите второе число ')
     print(int(lj) + int(hsh))
    except:
        ValueError
        print(err)

if h == 'm':
    try:
     hg = input('Введите первое число ')
     hv = input('Введите второе число ')
     print(int(hg) - int(hv))
    except:
        ValueError
        print(err)

if h == 't':
    try:
        ij = input('Введите первое число ')
        nb = input('Введите второе число ')
        print(int(ij) * int(nb))
    except:
        ValueError
        print(err)

if h == 'n':
    try:
     hd = input('Введите первое число ')
     yq = input('Введите второе число ')
     print(int(hd) / int(yq))
    except:
        ValueError
        print(err)

if h == 'b':
    try:
        qq = input('Введите число соответсующее проценту ')
        oo = input('Введите процент ')
        ww = int(qq) / (int(oo) / 100)
        print(ww)
    except:
        ValueError
        print(err)
