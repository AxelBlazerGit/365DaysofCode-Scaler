vector<int> Solution::sieve(int A) {
    int n = A;
    if (n <= 2) return vector<int>();

    vector<bool> isPrime(n, true);
    vector<int> primes;
    for (int i = 2; i < n; i++) {
        if (isPrime[i]) {
            primes.push_back(i);
            for (int j = 2 * i; j < n; j += i) {
                isPrime[j] = false;
            }
        }
    }

    return primes;
}
