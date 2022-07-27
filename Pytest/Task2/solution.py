

def solution(number):
    if number==2 or number==3:
        return True
    if number%2==0 or number%3==0 or number==0 or number==1:
        return False
    i=5
    while i*i<=number:
        if number%i==0 or number%(i+2)==0:
            return False
        i+=6
    return True

