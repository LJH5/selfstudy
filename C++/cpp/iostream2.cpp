#include <iostream>
#include <iomanip>	// ����� ����

using namespace std;

int main()
{
	cout.setf(ios::showpos);	b					// ��ȣ ǥ���ϱ�
		cout << 108 << endl;

	cout.unsetf(ios::showpos);					// ��ȣ ǥ�� �� �ϱ�
	cout << 108 << endl;

	//cout.setf(ios::hex, ios::basefield);		// 16������ ǥ���ϱ�
	cout << hex;								        // 16������ ǥ���ϱ�2
	cout << 108 << endl;

	cout << dec;										// 10������ ǥ���ϱ�
	cout << 108 << endl;

	cout.setf(ios::uppercase);					// �ҹ��ڸ� �빮�ڷ� ǥ��
	cout << hex << 108 << endl;

	cout << boolalpha;								// true, false�� ���ڿ� �� ���
	cout << true << " " << false << endl;

	cout << setprecision(3) << 123.456 << endl;	// �� �ڸ��� ǥ��. �ݿø�
	cout << setprecision(4) << 123.456 << endl;
	cout << setprecision(5) << 123.456 << endl;
	cout << setprecision(6) << 123.456 << endl;

	cout << fixed;	// �Ҽ��� �Ʒ� �ڸ��� ǥ��
	cout << setprecision(3) << 123.456 << endl;
	cout << setprecision(4) << 123.456 << endl;
	cout << setprecision(5) << 123.456 << endl;
	cout << setprecision(6) << 123.456 << endl;

	cout << scientific;	// ���� ǥ���
	cout << setprecision(3) << 123.456 << endl;
	cout << setprecision(4) << 123.456 << endl;
	cout << setprecision(5) << 123.456 << endl;
	cout << setprecision(6) << 123.456 << endl;

	return 0;
}