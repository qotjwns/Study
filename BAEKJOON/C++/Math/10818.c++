#include <iostream>
#include <vector>
#include <algorithm>

int main(int args, const char * argv[]){
    int n;
    std::cin >> n;
    std::vector<int> v(n);
    for(int& x : v) std::cin >> x;
    
    auto [mn, mx] = std::minmax_element(v.begin(), v.end());

    std::cout << *mn << " " << *mx;
}