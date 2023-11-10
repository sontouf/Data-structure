#include <bits/stdc++.h>

using namespace std;

vector<string> split(string input, string delimiter){
	size_t pos = 0;
	vector<string> ret;
	string token = "";
	while ((pos = input.find(delimiter)) != string::npos) {
		token = input.substr(0, pos);
		ret.push_back(token);
		input.erase(0, pos + delimiter.length());
	}
	ret.push_back(input);
	return ret;

}

int main(){
	string s = "앙녕하ㅔ숑 I'm lee younggyu. I want to be the best programmer!!";
	string d = " ";
	vector<string> a = split(s, d);
	for (string b : a) cout << b << '\n';
	return 0;
}