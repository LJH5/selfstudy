#include <stdio.h>

int main() {
	int num;
	int total_sum = 0;
	for (int i = 0; i < 5; i++) {
		scanf("%d", &num);
		total_sum += num * num;
	}
	
	printf("%d", total_sum % 10);

	return 0;
}