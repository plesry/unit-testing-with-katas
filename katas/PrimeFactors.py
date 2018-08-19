class PrimeFactors():

    @staticmethod
    def generate(num):
        primes = []
        candidate = 2
        while num > 1:
            while num % candidate == 0:
                primes.append(candidate)
                num = int(num / candidate)
            candidate = candidate + 1
        return primes