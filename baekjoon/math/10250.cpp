#include <iostream>
using namespace std;

int main(void) {
    int test;   // test case
    int height, width, n;   // 호텔의 층 수, 방 수, n번째 손님
    cin >> test;
    for(int i = 0; i < test; i++){
        cin >> height >> width >> n;
        int room = 0, floor;   // 방 배정
        floor = n % height;
        if (floor == 0)
            floor = height; 
        while (n > 0){
            n -= height;
            room++;
        }
        if (room < 10)
            cout << floor << "0" << room << "\n";
        else
            cout << floor << room << "\n";
    }
    return 0;
}
