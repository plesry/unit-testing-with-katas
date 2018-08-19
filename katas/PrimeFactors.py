class PrimeFactors():

    @staticmethod
    def generate(num):
        primes = []
        if num > 1:
            if num % 2 == 0:
                primes.append(2)
                num = int(num / 2)
            if num > 1:
                primes.append(num)
        return primes