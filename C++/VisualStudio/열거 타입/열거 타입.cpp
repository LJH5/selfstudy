#include <iostream>
using namespace std;

enum class PieceType { 
	King = 1,		// 1
	Queen,			// 2
	Rook = 10,	// 10
	Pawn				// 11
};
PieceType piece{ PieceType::Pawn };

int main() {
	cout << static_cast<int>(piece);
}
