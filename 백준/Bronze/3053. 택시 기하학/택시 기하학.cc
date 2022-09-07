#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    // 택시기하학

    int R;  // 반지름
    double u_area, t_area;  // 유클리드 기하학에서 원의 넓이, 택시 기하학에서 원의 넓이
    const double PI = 3.1415926535897932;

    cin >> R;
    u_area = R * R * PI;
    printf("%.6f\n", u_area);
    
    t_area = (2 * R) * (2 * R) / 2;     // 마름모의 넓이
    printf("%.6f\n", t_area);

	return 0;
}