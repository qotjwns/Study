#include <iostream>
#include <iomanip>

int main(int args, const char * argv[]){
    double a, b;
    std::cin >> a >> b;
    std::cout << std::fixed
              << std::setprecision(10)
    << (a / b);
    return 0;
}