#include <bits/stdc++.h>

using namespace std;
const int n = 7;

void printData(int data[])
{
	for ( int i = 0; i < n; i++) {
		printf("%d ", data[i]);
	}
	return ;
}

void bubble(int data[]){
	for (int i = n - 1; i > 1; i--) {
		for (int j = 0; j < i; j++) {
			if (data[j] > data[j + 1])
				swap(data[j], data[j + 1]);
		}
	}
	printData(data);
	return ;
}

void selection(int data[]) {
	for (int i = 0; i < n; i++) {
		int minIndex = i;
		for (int j = i + 1; j < n; j++) {
			if (data[j] < data[minIndex])
				minIndex = j;
		}
		if (minIndex != i)
			swap(data[minIndex], data[i]);
	}
	
	printData(data);
	return ;
}

void insertion(int data[]) {
	int i = 1;
	for (int i = 1; i < n; i++) {
		for (int j = i - 1; j >= 0; j--) {
			if (data[j + 1] < data[j])
				swap(data[j], data[j + 1]);
			else
				break;
		}
	}
	printData(data);
	return ;
}

int main() {
	int data[n] = {1,8,3,11,5,10,9};
	bubble(data);
	cout << '\n';
	insertion(data);
	cout << '\n';
	selection(data);
	cout << '\n';
	return 0;
}