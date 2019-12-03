import math

mod = 1000000007

class demo_class:
    def countOnes(self, arr, n):
        return arr.count(1)

    def isPalindrome(self, L):
        if(len(L) == 0 or len(L) == 1):
            return True
        i = 0
        j = len(L) - 1
        while(i < j and i != j):
            if(L[i] != L[j]):
                return False
            i += 1
            j -= 1
        return True

    def fibonacci(self, n):
        l = [1, 1]
        for i in range(2, n + 2):
            l.append(l[i - 1] + l[i - 2])
        return l[n]
    def isPrime(self, n):
        if (n <= 1) :
            return False
        if (n <= 3):
            return True
        if (n % 2 == 0 or n % 3 == 0):
            return False
        i = 5
        while(i * i <= n):
            if(n % i == 0 or n % (i + 2) == 0):
                return False
            i += 6
        return True

    def GCD(self, a, b):
        return (a == 0) and b or self.GCD(b % a, a)

    def setKthBit(self, n, k):
        return (n | (1 << k))

    def mod(self, num, m):
        ans = 0
        for i in range(len(num)):
            ans = (ans * 10 + int(num[i])) % m
        return ans

    def isAlternatePattern(self, n): #10101010 --> True and 1101101010 --> False
        val = n ^ (n >> 1)
        return ((val + 1) & val == 0) and "YES" or "NO"

    def XorSubarray(self, arr, N):
        res = 0
        for i in range(N):
            if (((i + 1) * (N - i)) % 2 == 1):
                res ^= arr[i]
        return res

    def swapOddEvenBits(self, N):
        even = N & 0xAAAAAAAA
        odd = N & 0x55555555
        even >>= 1
        odd <<= 1
        return (even | odd)
d = demo_class()


# d.countPathMaze(3, 3)
d.countOnes([1, 1, 0, 0], 4)
d.fibonacci(5)
d.isPalindrome('')
d.isPalindrome('a')
d.isPalindrome('abcd')
d.isPalindrome('aba')
d.isPrime(4)
d.isPrime(2)
d.isPrime(1)
d.isPrime(24)
d.isPrime(23)
d.isPrime(25)
d.isPrime(123)
d.GCD(0, 5)
d.GCD(10, 12)
d.GCD(13, 7)
d.mod("3982378328623737256363272383732653623327637", 10)
d.mod("1767251462623553343156443113153644118798162145153", 6)
d.isAlternatePattern(10) # YES
d.isAlternatePattern(12) # NO
d.XorSubarray([3, 5, 2, 4, 6], 5)
d.XorSubarray([251, 16, 1, 33, 13, 4], 6)
d.swapOddEvenBits(23)
d.swapOddEvenBits(2)
# d.Fastfib(2, [0, 0])

# print(d.add(2, 3))
# print(d.mul(2.3, 4.3))
# print(d.fibonacci(5))
# print(d.isPalindrome('abcd'))
# print(d.isPalindrome('aba'))
# print(d.isPrime(4))
# print(d.isPrime(2))
# print(d.isPrime(1))
# print(d.CeilDiv(4, 5))

# print(d.fibonacci(1))
# print(d.fibonacci(2))
# print(d.fibonacci(3))
# print(d.fibonacci(4))
# print(d.fibonacci(5))

# print(d.fibonacci(50))
# print(d.fibonacci(0))
# print(d.fibonacci(14))
# print(d.fibonacci(3))
# print(d.fibonacci(77))
# print(d.fibonacci(11))
# print(d.fibonacci(4))
# print(d.fibonacci(18))
