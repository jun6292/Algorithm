#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main()
{
    // 큐 2
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    queue<int> q;
    string str;

    for (int i = 0; i < N; i++) {
        cin >> str;

        if (str == "push") {
            int num;
            cin >> num;
            q.push(num);
        }
        else if (str == "size") {
            cout << q.size() << "\n";
        }
        else if (str == "front") {
            if (!q.empty())
                cout << q.front() << "\n";
            else
                cout << "-1\n";
        }
        else if (str == "back") {
            if (!q.empty())
                cout << q.back() << "\n";
            else
                cout << "-1\n";
        }
        else if (str == "pop") {
            if (!q.empty()) {
                cout << q.front() << "\n";
                q.pop();
            } 
            else
                cout <<"-1\n";
        }
        else if (str == "empty") {
            if (!q.empty())
                cout << "0\n";
            else
                cout << "1\n";
        }
    }
	return 0;
}