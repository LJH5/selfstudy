#include <iostream>

using namespace std; 

enum StudentName    
{
    // 가능은 하지만 권장하지는 않음
    Jack,         // 0 
    Dash,         // 1
    Micle,        // 2
    NUM_STUDENTS, // 3
};

int main() {
    int my_array[] = {1, 2, 3, 4, 5};
    // int my_array[]{1, 2, 3, 4, 5};  // C++ 17 버전 이상
    cout << my_array[Jack] << endl;
    cout << my_array[Dash] << endl;
    cout << my_array[Micle] << endl;
    cout << my_array[3] << endl;
    cout << my_array[4] << endl;

    int students_scores[NUM_STUDENTS];  // 이렇게도 사용이 가능함

    students_scores[Jack] = 100;
    students_scores[Dash] = 80;


}