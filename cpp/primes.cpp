#include <iostream>

bool is_prime(int);

int main() {
    std::cout << "Hello world" << std::endl;
    for(int k=1; k<100; k++) {
        if(is_prime(k)) {
            std::cout << k << std::endl;
        }
    }
}

bool is_prime(int n) {
    for(int i=2; i<n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}