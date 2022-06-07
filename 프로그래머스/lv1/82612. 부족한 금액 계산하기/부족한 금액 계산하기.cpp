using namespace std;

long long solution(int price, int money, int count)
{
    long long answer = -1;
    long long total = 0;    // 놀이기구 총 이용금액
    int inc = price;    // 요금 인상
    while (count > 0){
        total += price;
        price += inc;
        count--;
    }
    if (total <= money)
        answer = 0;
    else
        answer = total - money;
    return answer;
}