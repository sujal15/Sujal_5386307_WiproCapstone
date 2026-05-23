from oopsconcept.calc import Calc

calcobj = Calc()
print(calcobj.add(10,5))
print(calcobj.sub(10,5))
print(calcobj.mul(10,5))
numbers = [10,20,30]
count = len(numbers)
print(f'length: {count}')
try:
    res = calcobj.fdiv(10,0)
    for i in range(0, count+1 ):
        print(numbers[i])
except IndexError:
    print('check the index')
except ZeroDivisionError:
    print('0 in denominator')
else:
    print(res)
finally:
    print('Done !!')
