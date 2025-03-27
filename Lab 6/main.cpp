/*
*globalVal = 0
def question3(n):
global globalVal
if n > 0:
globalVal += 1/n
question3(n-1)

*/
using namespace std;
#include <iostream>


double x = 0;
double question3(double n) {
    if (n >0)
    {
        x += 1/n;
        cout << "1/" << n << endl;
        question3(n-1);
    }else {
        return x;
    }
}
double question3() {
    cout << "enter val" << endl;
    double n;
    cin >> n;
    return question3(n);
}

