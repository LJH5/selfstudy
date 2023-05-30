#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
    // PGM 파일 읽기
    ifstream infile("map.pgm");
    string line;
    getline(infile, line);
    getline(infile, line);
    int width, height, max_value;
    istringstream iss(line);
    iss >> width >> height;
    getline(infile, line);
    istringstream iss2(line);
    iss2 >> max_value;

    vector<vector<int>> prob_map(height, vector<int>(width));
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            int pixel_value;
            infile >> pixel_value;
            // 픽셀 값을 점유 확률로 변환
            prob_map[i][j] = (pixel_value > 128) ? 1 : 0;
        }
    }
    infile.close();

    // 그리드 맵 생성
    ofstream outfile("grid_map.txt");
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            outfile << prob_map[i][j] << " ";
        }
        outfile << "\n";
    }
    outfile.close();

    return 0;
}
