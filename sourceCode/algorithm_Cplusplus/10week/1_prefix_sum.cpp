// 승철이는 뇌를 다쳤다. 그래서 주어진 범위의 합을 구하는 프로그램을 대신 짜주자.
// 입력
// N: 8 M : 3 (N <= 100000, M <= 100000)
// 1 2 3 4 5 6 7 8
// 1 5
// 1 4
// 2 5

// 출력
// 15
// 10
// 14
#include <bits/stdc++.h>
using namespace std;

int a[100004], b, c, psum[100004], N, M;
int main() {
	cin >> N >> M;

	for (int i = 1; i < N + 1; i++) {
		cin >> a[i];
		psum[i] = psum[i-1] + a[i];
		cout << psum[i] << '\n';
	}
	for (int i = 0; i < M; i++) {
		cin >> b >> c;
		cout << "b :" << b << "C : " << c << '\n';
		cout << psum[c] - psum[b-1] << '\n';
	}
	return 0;
}