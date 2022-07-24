#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// 유클리드 호제 a > b
int gcd(int a, int b) {
    int r = 0;
    while (b) {
            r = a % b;
            a = b;
            b = r;
    }
    return a;
}

int solution(vector<int> arr) {
    while (arr.size() != 1) {
        int i = arr.size() - 1;
        int x = arr[i];
        int y = arr[i - 1];
        arr.pop_back();
        arr.pop_back();
        arr.push_back((x * y) / gcd(x, y));
    } 
    return arr[0];
}
                      