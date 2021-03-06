#include <vector>
#include <list>
#include <functional>
#include "graph.h"



struct TSort {
	std::list<int> vert_ids;

	void operator()(int i) { vert_ids.push_front(i); }
};

int main()
{
	graph G;

	G.init(5);
	G.addEdge(0, 1);
	G.addEdge(1, 2);
	G.addEdge(0, 2);
	G.addEdge(3, 4);

	int nC = G.DFS_Iter();

	graph DG;
/*
	DG.init(4, true);
	DG.addEdge(0, 1);
	DG.addEdge(1, 3);
	DG.addEdge(0, 2);
	DG.addEdge(2, 3);
*/

//========= Topological sort =====================
	graph DG1;

	DG1.init(3, true);
	DG1.addEdge(0, 1);
	DG1.addEdge(2, 1);

	std::list<int> vert_ids = DG1.TopologicalSort();


//========= Strongly Connected Components =====================
	graph DG2;

	DG2.init(12, true);
	DG2.addEdge(1, 0);
	DG2.addEdge(2, 1);
	DG2.addEdge(3, 1);
	DG2.addEdge(1, 4);
	DG2.addEdge(4, 1);
	DG2.addEdge(2, 5);
	DG2.addEdge(5, 2);
	DG2.addEdge(5, 4);
	DG2.addEdge(6, 4);
	DG2.addEdge(7, 5);
	DG2.addEdge(7, 6);
	DG2.addEdge(6, 8);
	DG2.addEdge(8, 9);
	DG2.addEdge(9, 6);
	DG2.addEdge(10, 7);
	DG2.addEdge(9, 11);
	DG2.addEdge(11, 10);

	std::list<std::list<int>> listSCC = DG2.SCC();

//========= Shortest Path =====================
	graph DG3;
	DG3.init(8);
	DG3.addEdge(0, 1);
	DG3.addEdge(0, 4);
	DG3.addEdge(1, 5);
	DG3.addEdge(5, 2);
	DG3.addEdge(5, 6);
	DG3.addEdge(2, 6);
	DG3.addEdge(2, 3);
	DG3.addEdge(3, 7);
	DG3.addEdge(6, 7);

	DG3.BFS(1);

	std::list<int> Path;
	bool bOK = DG3.getShortestPath(Path, 0, 3);

//========== Dijkstra ===========================
	graph DG4;
	DG4.init(4,true);
	DG4.addEdge(0, 1, 4);
	DG4.addEdge(0, 2,10);
	DG4.addEdge(2, 1, 2);
	DG4.addEdge(1, 3, 1);
	DG4.addEdge(3, 2, 3);

	DG4.Dijkstra(0);

//========== BellmanFord ===========================
	graph DG5;
	DG5.init(4, true);
	DG5.addEdge(0, 1, 4);
	DG5.addEdge(0, 2, 10);
	DG5.addEdge(2, 1, 2);
	DG5.addEdge(1, 3, 1);
	DG5.addEdge(3, 2, -4);

	bool bNWC = DG5.BellmanFord(0);

//========== Kruskal ===========================
	graph DG6;
	DG6.init(9, true);
	DG6.addEdge(0, 1, 4);
	DG6.addEdge(1, 2, 8);
	DG6.addEdge(2, 3, 7);
	DG6.addEdge(3, 4, 9);
	DG6.addEdge(4, 5, 10);
	DG6.addEdge(5, 6, 2);
	DG6.addEdge(6, 7, 1);
	DG6.addEdge(7, 0, 8);
	DG6.addEdge(6, 8, 6);
	DG6.addEdge(7, 8, 7);
	DG6.addEdge(7, 1, 11);
	DG6.addEdge(8, 2, 2);
	DG6.addEdge(5, 2, 4);
	DG6.addEdge(5, 3, 14);

	std::vector<graph::edge2> vST;
	float W = DG6.Kruskal(vST);

    return 0;
}

