#pragma once
#include <vector>

class DisjointSets {
private:
	std::vector<int> parent;
	std::vector<int> rank;
	int nSets{0};

public:
	DisjointSets() = default;
	DisjointSets(int N){
		parent.resize(N,-1);
		rank.resize(N,0);
		for (int d = 0; d < N; d++)
			MakeSet(d);
	}

	void MakeSet(int x) {
		if (x >= (int)parent.size() || parent[x] != -1)
			return;
		parent[x] = x;
		rank[x]   = 0;
		nSets++;
	}

	int Find(int x)
	{
		while (parent[x] != x)
			x = parent[x];
		return x;
	}

	void Union(int x, int y)
	{
		int id_x = Find(x);
		int id_y = Find(y);

		if (id_x == id_y)
			return;
		
		if (rank[id_x] > rank[id_y])
			parent[id_y] = id_x;
		else
		{
			parent[id_x] = id_y;
			if (rank[id_x] == rank[id_y])
				rank[id_y]++;
		}
		nSets--;
	}
};