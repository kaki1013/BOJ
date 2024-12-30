/*
1,000,000 * 10 * 10 = 100,000,000
MOD 998,244,353
ROOT 3
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MOD 998244353           // NTT-friendly prime
#define ROOT 3                  // Primitive root of MOD

// #define MAX_LENGTH 16           // test
#define MAX_LENGTH 1048576      // 2^20
#define N (2 * MAX_LENGTH)

// Function to compute (base^exp) % mod using modular exponentiation
long long mod_pow(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }

    if (result < 0) result += mod;
    
    return result;
}

// NTT function
void ntt(long long *arr, int n, int inv) {
    if (n == 1) return;

    int w_n = mod_pow(ROOT, (MOD-1)/n, MOD);
    if (inv) w_n = mod_pow(w_n, MOD-2, MOD);

    long long *even = (long long *)calloc(n/2, sizeof(long long));
    long long *odd = (long long *)calloc(n/2, sizeof(long long));
    for (int i = 0; i < n/2; i++) {
        even[i] = arr[2*i];
        odd[i] = arr[2*i+1];
    }

    ntt(even, n/2, inv);
    ntt(odd, n/2, inv);

    long long tmp = 1;
    for (int k = 0; k < n/2; k++) {
        arr[k]       = (even[k] + (tmp * odd[k]) % MOD) % MOD;
        arr[k + n/2] = (even[k] - (tmp * odd[k]) % MOD + MOD) % MOD;

        tmp = (tmp * w_n) % MOD;
    }

    free(even);
    free(odd);
}

// Inverse NTT function
void intt(long long *a, int n) {
    if (n == 1) return;

    ntt(a, n, 1);

    long long n_inv = mod_pow(n, MOD-2, MOD);
    for (int i = 0; i < n; i++)
        a[i] = (a[i] * n_inv) % MOD;
}


// Polynomial multiplication using NTT
void polynomial_multiply(long long *p1, int len1, long long *p2, int len2, long long *result) {
    long long a[N]={0,}, b[N]={0,};

    for (int i = 0; i < len1; i++) a[i] = p1[i];
    for (int i = 0; i < len2; i++) b[i] = p2[i];

    ntt(a, N, 0);
    ntt(b, N, 0);

    for (int i = 0; i < N; i++) a[i] = (a[i] * b[i]) % MOD;

    intt(a, N);

    for (int i = 0; i < N; i++) result[i] = a[i];
}

// Main function for demonstration
int main() {
    char tmp[MAX_LENGTH];
    long long p1[MAX_LENGTH], p2[MAX_LENGTH], result[N];
    int len;
    
    scanf("%s", tmp);
    len = strlen(tmp);  // strlen : O(n)
    for (int i = 0; i < len; i++) p1[len-1-i] = tmp[i] - '0';
    for (int i = len; i < MAX_LENGTH; i++) p1[i] = 0;

    scanf("%s", tmp);
    len = strlen(tmp);  // strlen : O(n)
    for (int i = 0; i < len; i++) p2[len-1-i] = tmp[i] - '0';
    for (int i = len; i < MAX_LENGTH; i++) p2[i] = 0;
    
    polynomial_multiply(p1, MAX_LENGTH, p2, MAX_LENGTH, result);

    int carry = 0;
    for (int i = 0; i < N; i++) {
        result[i] += carry;
        carry = result[i] / 10;
        result[i] -= 10 * carry;
    }

    int first_nonzero = 0;
    for (int i = N-1; i >= 0; i--) {
        if (result[i] != 0) {
            first_nonzero = i;
            break;
        }
    }
    
    for (int i = first_nonzero; i >= 0; i--) {
        printf("%lld", result[i]);
    }
    printf("\n");

    return 0;
}
