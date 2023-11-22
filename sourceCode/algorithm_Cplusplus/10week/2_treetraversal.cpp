#include <bits/stdc++.h>
using namespace std;

vector<int> adj[1004];
int visited[1004];


void postOrder(int here) {
	if (visited[here] == 0) {
		if (adj[here].size() == 1) postOrder(adj[here][0]);
		if (adj[here].size() == 2) {
			postOrder(adj[here][0]);
			postOrder(adj[here][1]);
		}
		visited[here] = 1;
		cout << here << ' ';
	}
}

void preOrder(int here) {
	if (visited[here] == 0) {
		visited[here] = 1;
		cout << here << ' ';
		if (adj[here].size() == 1) preOrder(adj[here][0]);
		if (adj[here].size() == 2) {
			preOrder(adj[here][0]);
			preOrder(adj[here][1]);
		}
	}
	
}

void inOrder(int here) {
	if (visited[here] == 0) {
		if (adj[here].size() == 1){
			preOrder(adj[here][0]);
			visited[here] = 1;
			cout << here << ' ';
		}
		else if (adj[here].size() == 2) {
			preOrder(adj[here][0]);
			visited[here] = 1;
			cout << here << ' ';
			preOrder(adj[here][1]);
		}
		else {
			visited[here] = 1;
			cout << here << ' ';
		}
	}
	
}

int main() {
	adj[1].push_back(2);
	adj[1].push_back(3);
	adj[2].push_back(4);
	adj[2].push_back(5);
	int root = 1;
	cout << "트리 순회 : postOrder \n";
	postOrder(root);
	memset(visited, 0, sizeof(visited));
	return 0;
}