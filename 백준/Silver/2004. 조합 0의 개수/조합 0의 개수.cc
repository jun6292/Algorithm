#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int cnt(int k, int n) { // k는 k!, n은 팩토리얼 안의 개수를 구하고자 하는 숫자
    int num = 0;
    for (unsigned long long i = n; i <= k; i *= n)
        num += k / i;
    return num;
}

int main()
{
    // 조합 0의 개수
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;
    int cnt_five = 0, cnt_two = 0;
    cin >> n >> m;
    // 조합공식: nCm = n! / (m! * (n - m)!)
    cnt_two = cnt(n, 2) - cnt(n - m, 2) - cnt(m, 2);    // 분자의 2의 개수에서 분모의 2의 개수를 뺌
    cnt_five = cnt(n, 5) - cnt(n - m, 5) - cnt(m, 5);   // 분자의 5의 개수에서 분모의 5의 개수를 뺌
    cout << min(cnt_five, cnt_two) << '\n'; // 두 값 중 더 작은 값을 출력
}