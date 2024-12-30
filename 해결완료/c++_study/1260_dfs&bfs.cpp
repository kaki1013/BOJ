// BOJ 1260
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> adj[1001];
bool visited[1001] = {false, };
queue<int> q;

void dfs(int s) {
    if (visited[s]) return;
    visited[s] = true;
    cout << s << " ";
    for (auto t: adj[s]) {
        dfs(t);
    }
}

void bfs(int s) {
    visited[s] = true;
    q.push(s);
    cout << s << " ";
    while (!q.empty()) {
        int s = q.front(); q.pop();
        for (auto t: adj[s]) {
            if (visited[t]) continue;
            visited[t] = true;
            q.push(t);
            cout << t << " ";
        }
    }
}

int main() {
    int N, M, V, u, v;

    cin >> N >> M >> V;
    for (int i=0; i<M; i++) {
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    for (int i=1; i<=N; i++)
        sort(adj[i].begin(), adj[i].end());

    dfs(V);
    cout << "\n";
    
    for (int i=0; i<1001; i++) visited[i] = false;
    bfs(V);
    cout << "\n";

    return 0;
}
