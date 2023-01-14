#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int gcd(int x, int y) { // 최대 공약수 구하기, 유클리드 호제
    int r;
    while (y) {
            r = x % y;
            x = y;
            y = r;
        }
    return x;
}

int main()
{
    // 검문
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, num;
    vector<int> num_vec, ans_vec;

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> num;
        num_vec.push_back(num);
    }
    sort(num_vec.begin(), num_vec.end()); // 오름 차순 정렬
    int diff = num_vec[1] - num_vec[0];
    for (int i = 2; i < num_vec.size(); i++)
        diff = gcd(diff, num_vec[i] - num_vec[i - 1]); // 두 수의 차들의 최대 공약수
    ans_vec.push_back(diff);
    for (int i = 2; i * i <= diff; i++) {   // 시간 초과 방지
        if (diff % i == 0) {
            ans_vec.push_back(i);
            ans_vec.push_back(diff / i);
        }
    }
    sort(ans_vec.begin(), ans_vec.end());
    ans_vec.erase(unique(ans_vec.begin(), ans_vec.end()), ans_vec.end());
    for (int i = 0; i < ans_vec.size(); i++)
        cout << ans_vec[i] << ' ';  // diff의 1을 제외한 약수들을 오름차순으로 출력
}