#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int N, M;
int waterpool[50][50];
int visited[50][50];
int dy[4] = {-1,1,0,0};
int dx[4] = {0,0,-1,1};


int bfs(int sy, int sx, int height)
{
	vector<pair<int, int>> queue = vector<pair<int, int>>();
	queue.push_back(pair<int, int>(sy,sx));
	visited[sy][sx] = 1;
	int flag = 1;
	int count = 1;
	while (!queue.empty())
	{
		pair<int, int> cur = queue.front();
		queue.erase(queue.begin());
		for (int i = 0; i < 4; i++)
		{
			int ny = dy[i] + cur.first;
			int nx = dx[i] + cur.second;

			if ((0 <= ny && ny < N) && (0 <= nx && nx < M))
			{
				if (visited[ny][nx] == 0 && waterpool[ny][nx] <= height)
				{
					visited[ny][nx] = 1;
					count++;
					queue.push_back(pair<int, int>(ny, nx));
				}
			}
			else
				flag = 0;
		}
	}
	if (flag == 0)
		return 0;
	return count;
}

int main(void)
{
	int result = 0;
	scanf("%d%d", &N, &M);
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			scanf("%1d", &waterpool[i][j]);
	for (int height = 1; height < 9; height++) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				visited[i][j] = 0;
			}
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (visited[i][j] == 0 && waterpool[i][j] <= height)
					result += bfs(i, j, height);
			}
		}
	}
	printf("%d", result);
	return 0;
}

// #include <bits/stdc++.h>
// using namespace std;
// string S;
// int n, m, i, j, hg, sum, h[53][53], flr[53][53];
// void inft(int a, int b){
//     if(a < 0 || a > 52 || b < 0 || b > 52 || flr[a][b]) return;
//     flr[a][b] = 1;
//     inft(a+1,b);inft(a,b+1);inft(a-1,b);inft(a,b-1);
//     return;
// }
// int main(){
//     cin >> n >> m;
//     for(i = 0; i++ < n;){
//         cin >> S;
//         for(j = 0; j++ < m;) h[i][j] = S[j-1] - '0';
//     }
//     for(hg = 1; hg < 10; hg++){
//         memset(flr, 0, sizeof(flr));
//         for(i = 0; i++ < n;) for(j = 0; j++ < m;) if(h[i][j] >= hg) flr[i][j] = 1;
//         inft(0,0);
//         for(i = 0; i++ < n;) for(j = 0; j++ < m;) if(flr[i][j] == 0) sum++;
//     }
//     cout << sum << '\n';
// }