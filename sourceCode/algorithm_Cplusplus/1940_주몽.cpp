#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[15004];
int cnt;
int combi(int n, int r) {
	if (r == 0) return n;
	return n * combi(n-1, r - 1);
}


int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) cin >> arr[i];

	if (m > 200000) cout << 0 << '\n';
	else {
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				if (arr[i] + arr[j] == m) cnt++;
			}
		}
		cout << cnt << '\n';
	}
	return 0;
}