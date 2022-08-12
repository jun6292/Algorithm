#include <iostream>
#include <set>
#include <string>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int A, B, num;   // 집합 A의 원소의 개수, 집합 B의 원소의 개수, 숫자 입력
    set<int> s_A, s_B;  // 집합 A, 집합 B
    cin >> A >> B;
    int cnt = A + B;
    for (int i = 0; i < A; i++) {
        cin >> num;
        s_A.insert(num);
    }
    for (int i = 0; i < B; i++) {
        cin >> num;
        s_B.insert(num);
    }
    for (auto a : s_A) {
        if (s_B.find(a) != s_B.end())
            cnt -= 2;
    }
    cout << cnt << "\n";
    return 0;
}