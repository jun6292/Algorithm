#include <iostream>
#include <stack>

using namespace std;

int main()
{ 
    // 제로
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int K, num;
    int sum = 0;
    stack<int> st;
    cin >> K;
    for (int i = 0; i < K; i++) {
        cin >> num;
        if (num != 0)
            st.push(num);
        else
            st.pop();
    }
    if (st.empty())
        cout << "0\n";
    else {
        while (!st.empty()) {
            sum += st.top();
            st.pop();
        }
        cout << sum << "\n";
    }
    return 0;
}