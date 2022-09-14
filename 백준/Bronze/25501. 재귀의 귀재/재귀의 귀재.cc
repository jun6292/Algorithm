#include <iostream>
#include <string>
using namespace std;


int main()
{
    // 재귀의 귀재
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    string S;

    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> S;

        int cnt = 0;
        int left = 0;
        int right = S.size() - 1;
        int isPal = 1;
        
        while (left <= right) {
            cnt++;
            if (S[left] != S[right]) {
                isPal = 0;
                break;
            }
            left++;
            right--;
        }
        cout << isPal << " ";
        if (S.size() % 2 == 0 && isPal == 1)
            cout << cnt + 1 << "\n";
        else
            cout << cnt << "\n";
    }
    return 0;
}