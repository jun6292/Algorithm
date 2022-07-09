#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    int size = nums.size();                                 // 변경 되기 이전의 nums 배열 크기
    sort(nums.begin(), nums.end());                         // nums 배열의 요소들을 오름차순 정렬
    nums.erase(unique(nums.begin(), nums.end()), nums.end());    // nums 배열의 중복되는 요소들 모두 제거
    int i = 0;
    while ((i < size / 2) && (i < nums.size())){
        i++;        
        answer++;
    }
    return answer;
}