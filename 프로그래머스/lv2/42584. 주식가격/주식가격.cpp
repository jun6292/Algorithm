#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> prices) {
    int size = prices.size();
    vector<int> answer(size, 0);
    stack<int> st;  // 인덱스를 저장하는 스택
    
    for (int i = 0; i < size; i++) {
        // 주식 가격이 떨어졌을 경우
        while (!st.empty() && prices[st.top()] > prices[i]) {
            answer[st.top()] = i - st.top();
            st.pop();
        }
        st.push(i); // 현재 인덱스를 스택에 push
    }
    // 스택에 남아있는 인덱스의 경우, 주식 값이 떨어지지는 않았음을 의미
    while (!st.empty()) {
        answer[st.top()] = size - 1 - st.top();
        st.pop();
    }
    
    return answer;
}