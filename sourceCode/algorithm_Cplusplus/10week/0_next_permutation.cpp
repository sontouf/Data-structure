#include <bits/stdc++.h>
using namespace std;

int main()
{
	// �迭��� 
//	int a[] {1,2,3};
//	do {
//		for (int i : a) cout << i << " ";
//		cout << '\n';
//	}while (next_permutation(&a[0], &a[0] + 3));

	// vector ��� 
//	vector<int> a {1,2,3};
//	sort(a.begin(), a.end());
//	do{
//		for (int i : a) cout << i << " ";
//		cout << '\n';
//	}while(next_permutation(a.begin(), a.end()));


	vector<int> a {2,1,3,100,200};
	sort(a.begin(), a.end());
	do{
		for (int i = 0; i < 2; i++){
			cout << a[i] << " ";
		} 
		cout << '\n';
	}while(next_permutation(a.begin(), a.end()));
	return 0;
}
