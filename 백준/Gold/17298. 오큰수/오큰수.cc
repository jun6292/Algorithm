#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main()
{
    // 오큰수
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, A;
    stack<int> st;
    vector<int> v;
    vector<int> ans;

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> A;
        v.push_back(A);
    }

    for (int i = N - 1; i >= 0; i--) {
        while (!st.empty() && st.top() <= v[i])
            st.pop();

        if (st.empty())
            ans.push_back(-1);
        else
            ans.push_back(st.top());

        st.push(v[i]);
    }

    for (int i = N - 1; i >= 0; i--)
        cout << ans[i] << " ";

    return 0;
}