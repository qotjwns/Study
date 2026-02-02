#include <iostream>
#include <stack>

long long sum_stack_destructive(std::stack<int>& st) {
    long long sum = 0;
    while (!st.empty()) {
        sum += st.top();
        st.pop();
    }
    return sum;
}

int main(){
    int K, num;    
    std::cin >> K;
    std::stack<int> st;
    
    for (int i = 0; i < K; i++){

        std::cin >> num;
        if(num == 0){
            st.pop();
        }else{
            st.push(num);
        }
    }
    std::cout << sum_stack_destructive(st);
}