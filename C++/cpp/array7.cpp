#include <iostream>

using namespace std;

int main()
{
    // 배열 반복문 사용
    int scores[] = { 84, 90, 76, 54, 79 };

    const int num_students = sizeof(scores) / sizeof(int);

    int total_score = 0;
    int max_score = 0;

    for (int i = 0; i < num_students; ++i) {
        cout << i << endl;
        total_score += scores[i];
        // max_score = (max_score < scores[i]) ? scores[i] : max_score;
        if (max_score < scores[i]) max_score = scores[i];
    }

    double avg_score = static_cast<double>(total_score) / num_students;
    
    cout << avg_score << endl;

}