#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int w = 0, h = 0;   // width, height
    
    // 가로, 세로 길이 중 더 큰 값을 가로길이로 변경.
    for (int i = 0; i < sizes.size(); i++){
        if (sizes[i][0] < sizes[i][1])
            swap(sizes[i][0], sizes[i][1]);
    }
    for (int i = 0; i < sizes.size(); i++){
        if (w < sizes[i][0])
            w = sizes[i][0];
        if (h < sizes[i][1])
            h = sizes[i][1];
    }
    answer = w * h;
    return answer;
}