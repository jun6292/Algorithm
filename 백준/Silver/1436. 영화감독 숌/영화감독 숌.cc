#include <iostream>
#include <string>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    cin >> N;
    int title = 666, cnt = 0;
    while (true) {
        string tmp = to_string(title);
        for (int i = 0; i < tmp.size() - 2; i++) {
            if (tmp[i] == '6' && tmp[i + 1] == '6' && tmp[i + 2] == '6') {
                cnt++;
                break;
            }
        }
        if (N == cnt) {
            cout << title << "\n";
            break;
        }
        title++;
    }
    return 0;
}