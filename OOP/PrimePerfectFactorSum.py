class Numbers:
    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        factors_sum = self.SumFactors()
        return factors_sum == self.Value

    def Factors(self):
        factors = [i for i in range(1, self.Value + 1) if self.Value % i == 0]
        print(f"Factors of {self.Value}: {factors}")
        return factors

    def SumFactors(self):
        return sum(self.Factors())

def main():
    num1 = Numbers(26)
    print(f" {num1.Value} a prime number? {num1.ChkPrime()}")
    print(f" {num1.Value} a perfect number? {num1.ChkPerfect()}")
    num1.Factors()             
    print(f"Sum of factors: {num1.SumFactors()}")

    print()
    num2 = Numbers(13)
    print(f" {num2.Value} a prime number? {num2.ChkPrime()}")
    print(f" {num2.Value} a perfect number? {num2.ChkPerfect()}")
    num2.Factors()              
    print(f"Sum of factors: {num2.SumFactors()}")

    print()
    num3 = Numbers(6)
    print(f"{num3.Value} a prime number? {num3.ChkPrime()}")
    print(f" {num3.Value} a perfect number? {num3.ChkPerfect()}")
    num3.Factors()              
    print(f"Sum of factors: {num3.SumFactors()}")

if __name__=="__main__":
    main()
