#include<iostream>
#include<algorithm>
using namespace std;

int unique(int* arr, int size);
int find(int arr[], int n, int key);

int main() {
	int n;
	int arr[1000000];
	int sorted[1000000];

    cin >> n;

    for (int i = 0; i < n; i++){
        cin >> arr[i];
        sorted[i] = arr[i];
    }

    sort(sorted, sorted + n);
    int cnt = unique(sorted,n);
    
    for (int i = 0; i<n;i++){
        cout << find(arr,cnt,sorted[i]) << " ";
    }
    return 0;
}

int unique(int* arr, int size) {
	int i, j = 0;
	for (i = 1; i < size; i++) {
		if (arr[j] == arr[i]) continue;
		arr[++j] = arr[i];
	}
	return ++j;
}


int find(int arr[], int n, int key) {

	int mid;
	int low = 0;
	int high = n - 1;

	while (low <= high) {
		mid = (low + high) / 2;
		if (arr[mid] == key) return mid;
		else if (key < arr[mid]) high = mid - 1;
		else if (key > arr[mid]) low = mid + 1;
	}
	return -1;
}