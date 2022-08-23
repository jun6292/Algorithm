#include <iostream>
#include <queue>

using namespace std;

int main()
{
    // 카드 2
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    queue<int> q;
    
    cin >> N;
    for (int i = 1; i <= N; i++) {  // 카드를 1부터 N까지 순서대로 큐에 넣는다.
        q.push(i);
    }
    // 카드가 한 개 남을때 까지 반복
    while (q.back() != q.front()) {
        q.pop();    // 제일 위에 있는 카드를 버린다.
        q.push(q.front());  // 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
        q.pop();
    }

    cout << q.front() << "\n";
    return 0;
}