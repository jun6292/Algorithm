#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, M;
    string poket, input;
    map<int, string> poket_num;
    map<string, int> poket_name;
    cin >> N >> M;
    for (int i = 0; i < N; i++) {   // 도감 두개를 만듬.
        cin >> poket;
        poket_num.insert({i + 1, poket});   // {숫자, 포켓몬}
        poket_name.insert({poket, i + 1});  // {포켓몬, 숫자}
    }
    for (int i = 0; i < M; i++) {
        cin >> input;
        if ('0' <= input[0] && input[0] <= '9')
            cout << poket_num[stoi(input)] << "\n";   // 숫자 입력 시 포켓몬 이름 출력
        else
            cout << poket_name[input] << "\n";  // 포켓몬 이름 입력 시 숫자 출력
    }
    return 0;
}