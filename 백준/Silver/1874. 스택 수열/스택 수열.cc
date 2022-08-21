#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    // 스택수열
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, num;
    stack<int> st;
    string ans;
    int k = 1;
    
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> num;
        if (num >= k) {
            while (num >= k) {
                st.push(k);
                k++;
                ans += "+";
            }
            st.pop();
            ans += '-';
        }
        else {
            if (num == st.top()) {
                st.pop();
                ans += "-";
            }
            else {
                cout << "NO\n";
                return 0;
            }
        }
    }
    // +, - 출력
    for (int i = 0; i < ans.size(); i++)
        cout << ans[i] << "\n";
    return 0;
}