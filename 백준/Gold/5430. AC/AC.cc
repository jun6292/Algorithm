#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
    // AC
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T, n;   //  테스트 케이스 개수, 배열에 들어있는 수의 개수
    string p, input;   // 수행할 함수, 입력 배열

    cin >> T;
    for (int i = 0; i < T; i++) {
        bool err = false;
        string ele = "";    // 두 자리 수 이상 원소 처리
        deque<int> dq;
        cin >> p;
        cin >> n;
        cin >> input;
        if (n != 0) {
            for (int j = 0; j < input.size(); j++) {    // 입력받은 배열에서 [ , ] 를 제외하고 deque에 push
                if (input[j] == '[' || input[j] == ']' || input[j] == ',') {
                    if (input[j] != '[') {
                        dq.push_back(stoi(ele));
                        ele = "";
                    }
                }
                else
                    ele += input[j];
            }
        }
        int rev = 1;    // 배열이 뒤집어졌는지 판단, 1이면 정상, -1이면 뒤집힘
        for (int j = 0; j < p.size(); j++) {
            if (p[j] == 'R') {  // 'R' 명령어를 만나면 배열을 뒤집는다.
                rev *= -1;
            }
            else if (p[j] == 'D') {     // 'D' 명령어를 만났을 때
                if (dq.size() == 0) {   // 배열이 비어있으면 에러 출력
                    cout << "error\n";
                    err = true;
                    break;
                }
                else {
                    if (rev == 1)   // 배열의 순서가
                        dq.pop_front(); // 정방향이면 앞에서 pop
                    else
                        dq.pop_back();  // 역방향이면 뒤에서 pop
                }
            }
        }
        if (!err) {
            cout << '[';
            if (rev == 1) { // 정방향이면 정방향대로 출력
                while (!dq.empty()) {
                    cout << dq.front();
                    dq.pop_front();
                    if (dq.size() != 0)
                        cout << ',';
                }
            }
            else {  // 역방향이면 역방향대로 출력
                while (!dq.empty()) {
                    cout << dq.back();
                    dq.pop_back();
                    if (dq.size() != 0)
                        cout << ',';
                }
            }
            cout << "]\n";
        }
    }
}