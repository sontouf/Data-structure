#include <bits/stdc++.h>

using namespace std;
int n = 5;
int main() {

	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			for (int k = j + 1; k < n; k++) {
				cout << i << " " << j << " " << k << '\n';
			}
		}
	}

	return 0;
}