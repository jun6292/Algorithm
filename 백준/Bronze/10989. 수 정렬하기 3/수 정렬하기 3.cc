#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int count[10001] = { 0 };
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        int num;
        cin >> num;
        count[num]++;
    }
    for (int i = 0; i < 10001; i++) {
        for (int j = 0; j < count[i]; j++)
            cout << i << "\n";
    }
    return 0;
}