#include <bits/stdc++.h>
using namespace std;

int cnt = 0;
int N, K;
// Merge two subarrays L and M into arr
void merge(int arr[], int p, int q, int r) {
	int tmp[N];
	int i = p, j = q+1, t = p;
	while (i <= q || j <= r) {
		if (i == q + 1 || (j <= r && arr[i] >= arr[j]))
			tmp[t++] = arr[j++];
		else
			tmp[t++] = arr[i++];
	}
	t = p;
	while (t <= r) {
		arr[t] = tmp[t];
		cnt++;
		if (cnt == K)
			printf("%d", arr[t]);
		t++;
	}
}

// Divide the array into two subarrays, sort them and merge them
void mergeSort(int arr[], int l, int r) {
  if (l < r) {
    // m is the point where the array is divided into two subarrays
    int m = (l + r) / 2;

    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);

    // Merge the sorted subarrays
    merge(arr, l, m, r);
  }
}

int main() {
	cin >> N >> K;
	int arr[N] {};
	for (int i = 0; i< N; i++) {
		cin >> arr[i]; 
	}
	// int arr[] = {6, 5, 12, 10, 9, 1};
	int size = sizeof(arr) / sizeof(arr[0]);

	mergeSort(arr, 0, size - 1);
	if (cnt < K)
		cout << -1 << '\n';
	return 0;
}