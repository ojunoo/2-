#include<iostream>
using namespace std;

void cs_sort(int n, int array[]) {
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
	int n, k;
	int array[1000];

	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		cin >> array[i];
	}
	s_sort(n, array);

	cout << array[k-1] << " ";
	


}
