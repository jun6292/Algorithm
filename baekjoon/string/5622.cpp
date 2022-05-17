#include <iostream>
#include <string>
using namespace std;

int main() {
	string str;
	int arr[] = { 3,4,5,6,7,8,9,10 };
	int sum = 0;
	cin >> str;
	for(int i = 0; i < str.length(); i++){
		if ('A' <= str[i] && str[i] <= 'C')
			sum += arr[0];
		else if ('D' <= str[i] && str[i] <= 'F')
	        sum += arr[1];
	    else if ('G' <= str[i] && str[i] <= 'I')
		    sum += arr[2];
		else if ('J' <= str[i] && str[i] <= 'L')
		    sum += arr[3];
		else if ('M' <= str[i] && str[i] <= 'O')
			sum += arr[4];
		else if ('P' <= str[i] && str[i] <= 'S')
			sum += arr[5];
		else if ('T' <= str[i] && str[i] <= 'V')
			sum += arr[6];
		else if ('W' <= str[i] && str[i] <= 'Z')
		    sum += arr[7];
	}
	cout << sum;
				  return 0;
}
