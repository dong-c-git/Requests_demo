#coding:utf-8
class Count:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def is_prime(self,n):
        if n <= 1:
            return False

        for i in range(2,n):
            if n % i == 0:
                return True
            return False


if __name__=="__main__":
    Count(5,6)