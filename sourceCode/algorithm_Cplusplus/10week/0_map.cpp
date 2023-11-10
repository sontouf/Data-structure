#include <bits/stdc++.h>
using namespace std;
map<int,int> mp;

int main(){
	vector<int> a {2,2,1,2,2,3,3,3,3,3};
	for (auto i : a) {
		if (mp[i]) {
			continue;
		}else {
			mp[i] = i;
		}
	}

	vector<int> b;
	for (auto i : mp) {
		b.push_back(i.first);
	}
	for(int i : b) cout << i << '\n';

	return 0;
}