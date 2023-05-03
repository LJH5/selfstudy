#include <iostream>

using namespace std;

int main()
{   
    int one_student_score;
    int student_scores[5];

    // cout << sizeof(one_student_score) << endl;
    // cout << sizeof(student_scores) << endl;

    one_student_score = 100;

    student_scores[0] = 100; // 1st element
    student_scores[1] = 80;  // 2nd element
    student_scores[2] = 90;  // 3rd element
    student_scores[3] = 50;  // 4th element
    student_scores[4] = 0;   // 5th element

    for (int i = 0; i < 5; i++)
    {
        cout << student_scores[i] << endl;
    }

    cout << (student_scores[0] + student_scores[1]) / 2.0 << endl;

    return 0;
}