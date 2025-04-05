#include<iostream>
using namespace std;

void s_sort(int n, int array[]) {
	int i, j, max, temp;
	for (i = 0; i < n-1; i++) {
		max = i;
		for (int j = i + 1; j < n; j++) {
			if (array[max] < array[j]) {
				max = j;
			}
		}
		temp = array[i];
		array[i] = array[max];
		array[max] = temp;
	}
}

int main() {
	int i, num, size = 0;
	int array[1000];

	cin >> num;
	while (num > 0) {
		array[size++] = num % 10;
		num /= 10;
	}
	s_sort(size, array);

	for (i = 0; i < size; i++) {
		cout << array[i];
	}

	


}