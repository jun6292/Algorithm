#include <iostream>
using namespace std;

int main(void) {
	int fixed, flexible, price;
	cin >> fixed >> flexible >> price;
	if (flexible >= price)
		cout << "-1\n";
	else
		cout << (fixed / (price - flexible)) + 1;
	return 0;
}

// 낮은 난이도에도 불구하고 정답률이 26%인 이유를 알 것 같은 문제
// 처음에 cnt변수를 int형으로 선언해서 while로 증가시키며 풀다가
// 마지막 test case에서 오버플로우 나는 것을 발견, cnt를 long long으로 선언
// 출력은 잘 되나 시간초과가 날 것 같음을 직감
// 결국 while 없이 수식으로 풀기로 코드를 수정
// 정답.
