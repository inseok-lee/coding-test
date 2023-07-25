import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    # 최대공약수와 최소공배수
    gcd = math.gcd(denom1, denom2)
    lcm = (denom1*denom2)//gcd
    
    numer = (lcm // denom1) * numer1 + (lcm // denom2) * numer2
    denom = lcm
    
    new_gcd = math.gcd(denom, numer)
    numer = numer / new_gcd
    denom = denom / new_gcd
    
    # result
    answer = [numer, denom]
    
    return answer



# best
# import math

# def solution(denum1, num1, denum2, num2):
#     denum = denum1 * num2 + denum2 * num1
#     num = num1 * num2
#     gcd = math.gcd(denum, num)
#     return [denum//gcd, num//gcd]


# alternative
# from fractions import Fraction

# def solution(denum1, num1, denum2, num2):
#     answer = Fraction(denum1, num1) + Fraction(denum2, num2)
#     return [answer.numerator, answer.denominator]