#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int m) {
    vector<int> answer;
    int gcd = 1, lcm;   // greatest common divisor, least common multiple
    int a = n, b = m;
    
    // int i = 1;
    // while (i <= n && i <= m){
    //     if (n % i == 0 && m % i == 0)
    //         gcd = i;
    //     i++;
    // }

    if (a > b){
        while (1){
            int r = a % b;  // n > m
            if (r == 0){
                gcd = b;
                break;
            }
            a = b;
            b = r;
        }
    } 
    else {
        while (1){
            int r = b % a;  // n < m
            if (r == 0){
                gcd = a;
                break;
            }
            b = a;
            a = r;
        }
    }
    answer.push_back(gcd);
    answer.push_back((n*m)/gcd);
    return answer;
}