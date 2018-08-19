class PrimeFactors():

    @staticmethod
    def generate(num):
        if (num == 0):
            raise ValueError(f'{num} does not have a prime factorization')
        elif (num < 0):
            raise ValueError(f'{num} is negative and thus does not have a prime factorization')

        primes = []
        candidate = 2
        while num > 1:
            while num % candidate == 0:
                primes.append(candidate)
                num = int(num / candidate)
            candidate = candidate + 1
        return primes