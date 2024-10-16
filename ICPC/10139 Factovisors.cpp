#include <iostream>

bool test_prime_fact(int n, int p, int counterr) {
//function to test prim factors of divisor with dividend instead of testing the whole number
    long prime_ = p;
    while (n / prime_ && counterr > 0) {
        counterr -= n / prime_;
        prime_ *= p;
    }
    return counterr <= 0;
}

int main() {
    int fact_num;
    // the first number in the input
    int divisor;
    // the second number
    int counter;
    // we test if i divides divisors and we set a counter for how many times it does
    int current_div;
    //current_div to take the value of the divisor in the input
    bool is_divisor;
    //in default we set true that it divides the factorial number
    while (std::cin >> fact_num >> divisor) {
    //while loop to get the parameters that the function test_prim_fact needs and to output the result
        current_div = divisor;
        //current_div to take the value of the divisor in the input
        is_divisor = true;
        //in default we set true that it divides the factorial number
        for (int i = 2; i * i <= divisor && is_divisor; ++i) {
        // for loop to get the primes we will test later ..... i^2 <= divisor 'prime is smaller or equal to square root
            counter = 0;
            while (divisor % i == 0) {
            // while loop : we test if i divides divisors and we set a counter for how many times it does
                divisor /= i;
                ++counter;
            }
            if (counter > 0) {
            // test the factor i we found with the function 'test_prime_fact'
                is_divisor = test_prime_fact(fact_num, i, counter);
    
            }
        }
        if (divisor > 1 && is_divisor) {
        // case no i fits , then it is a prime itself and we test the whole number now
            is_divisor = test_prime_fact(fact_num, divisor, 1);
        }
        std::cout << current_div << " " << (is_divisor ? "divides" : "does not divide") << " " << fact_num << "!" << std::endl;
        //output the result
    }
}

