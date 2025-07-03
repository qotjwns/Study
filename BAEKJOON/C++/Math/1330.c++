#include <iostream>

int main(int args, const char * argv[]){
    int a, b;
    std::cin >> a >> b;
    if (a > b) {
        std::cout << ">";
    }
    else if (a < b){
        std::cout << "<";
    }
    else{
        std::cout << "==";
    }
    return 0;
}
