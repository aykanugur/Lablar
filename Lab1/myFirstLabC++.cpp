#include <iostream>
using namespace std;
int main() {

    cout << "What is your name : ";
    string name;
    cin >> name;
    cout << "Hello " << name << endl;
    cout << "What is your student id  : ";
    string student_id;
    cin >> student_id;
    cout << "Your student id is : " << student_id << endl;
    int var1;
    int var2;
    int sum;
    int diff;
    int prod;
    cout << "Enter val1: ";
    cin >> var1;
    cout << "Enter val2: ";
    cin >> var2;
    sum = var1 + var2;
    diff = var1 - var2;
    prod = var1 * var2;
    cout << "Sum is: " << sum << endl;
    cout << "Diff is: " << diff << endl;
    cout << "Prod is: " << prod << endl;

    int labGrade;
    int midGrade;
    int finalGrade;
    int totalGrade = 0;
    cout << "Enter your name : ";
    cin >> name;
    cout << "Enter your Lab grade : ";
    cin >> labGrade;
    cout << "Enter your mid grade : ";
    cin >> midGrade;
    cout << "Enter your final grade : ";
    cin >> finalGrade;
    totalGrade = labGrade * 0.25 + midGrade * 0.35 + finalGrade * 0.40;
    cout << "Name : " << name << endl;
    cout << "Lab grade : " << labGrade << endl;
    cout << "Mid grade : " << midGrade << endl;
    cout << "Final grade : " << finalGrade << endl;
    cout << "Total grade : " << totalGrade << endl;

    cout << "*" << endl << "**" << endl << "***" << endl << "**" << endl << "*" << endl;




    return 0;
}
