#pragma once

#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <functional>
#include <limits>

#include "disjoint_sets.h"


const float fMax = std::numeric_limits<float>::infinity();

class graphdata;

class graph {
public:
	struct edge {
		int   _iv; // vert id
		float _w;  // weight
	};

	struct edge2 {
		int   _iu; // vert id
		int   _iv; // vert id
		float _w;  // weight
	};

	struct vert {
		std::vector<edge> _adj;   // adjacency list: indexes in vVerts
		int   _cc{ -1 };          // index of connected comp where it belongs
		int   _tB{ -1 };          // time when visit begins 
		int   _tE{ -1 };          // time when visit ends 
		int   _dist{ -1 };        // distance to source (number of edges)
		float _fdist{ fMax };     // distance to source (sum of edges weights)
		int   _prev{ -1 };        // index of parent in shortest-path tree  
		bool isVisited() { return _cc != -1; }
		void reset() { _cc = -1; _tB = -1; _tE = -1; _dist = -1; _prev = -1; }
	};

	bool _bDirected{false};
	std::vector<vert>  _vs;
	std::vector<edge2> _es;

	void init(int nV, bool bDirected = false) {
		_vs.clear();
		_vs.resize(nV);
		_bDirected = bDirected;
	}

	int size() { return (int)_vs.size(); }

	void reset()
	{
		for (auto& v : _vs)
			v.reset();
	}

	void addEdge(int iv1, int iv2, float w = 0.0f) {
		vert& v1 = _vs.at(iv1);
		vert& v2 = _vs.at(iv2);
		v1._adj.push_back({ iv2, w });
		if( !_bDirected )
			v2._adj.push_back({ iv1,w });

		_es.push_back( edge2{ iv1,iv2,w } );
	}

	graph getTransposed()
	{
		graph gr;
		gr.init(size(), true);

		for (int iv = 0; iv < (int)_vs.size(); iv++)
		{
			for (auto& e : _vs[iv]._adj)
				gr.addEdge(e._iv, iv, e._w);
		}

		return gr;
	}

	std::list<int> TopologicalSort() 
	{
		std::list<int> vert_ids;
		std::function<void(int)> fTSort = [&vert_ids](int iv) { vert_ids.push_front(iv); };
		DFS(nullptr, fTSort);
		return vert_ids;
	}

	std::list<std::list<int>> SCC()
	{
		std::list<std::list<int>> listSCC;

		graph gr = getTransposed();
		std::list<int> vert_ids; // ids of verts in decreasing post-visit order
		std::function<void(int)> fTSort = [&vert_ids](int iv) { vert_ids.push_front(iv); };
		gr.DFS(nullptr, fTSort);

		reset();
		int cc = 0;
		int t = 0;
		for (auto it = vert_ids.begin(); it != vert_ids.end(); ++it)
		{
			if (_vs[*it].isVisited())
				continue;

			std::list<int> scc_ids;
			std::function<void(int)> fPost = [&scc_ids](int iv) { scc_ids.push_front(iv); };
			dfsVisit(*it, cc, t, nullptr, fPost);
			listSCC.push_front(scc_ids);
		}

		return listSCC;
	}

	// Deep First Search. Returns the number of connected components 
	int DFS(std::function<void(int)> preFn = nullptr, std::function<void(int)> postFn = nullptr)
	{
		reset();

		int cc = 0;
		int t = 0;
		for (int iv = 0; iv < (int)_vs.size(); iv++) {
			if (!_vs[iv].isVisited()) {
				dfsVisit(iv, cc, t, preFn, postFn);
				cc++;
			}
		}
		return cc;
	}

	void dfsVisit(int iv, int cc, int& t, std::function<void(int)> preFn, std::function<void(int)> postFn)
	{
		vert& v = _vs[iv];
		v._cc = cc;
		v._tB = t++;

		if (preFn)
			preFn(iv);

		for (auto& e : v._adj) {
			if (!_vs[e._iv].isVisited())
				dfsVisit(e._iv, cc, t, preFn, postFn);
		}

		v._tE = t++;
		if (postFn)
			postFn(iv);
	}

	// Iterative version
	int DFS_Iter(std::function<void(vert)> preFn = nullptr, std::function<void(vert)> postFn = nullptr)
	{
		reset();

		int cc = 0;
		int t = 0;
		for (int i = 0; i < (int)_vs.size(); i++) {
			if (!_vs[i].isVisited()) {
				dfsVisitIt(i, cc, t, preFn, postFn);
				cc++;
			}
		}
		return cc;
	}

	void dfsVisitIt(int iv, int cc, int& t, std::function<void(vert)> preFn, std::function<void(vert)> postFn)
	{
		vert& v = _vs[iv];
		v._cc = cc;
		v._tB = t++;

		if (preFn)
			preFn(v);

		std::stack<int> stk1;
		stk1.push(iv);

		while (!stk1.empty())
		{
			vert& v = _vs[stk1.top()]; 

			bool bFinished = true;
			for (auto& e : v._adj) {
				vert& v1 = _vs[e._iv];
				if (!v1.isVisited()) { // v1 is discovered
					v1._cc = cc;
					v1._tB = t++;

					if (preFn)
						preFn(v1);
					stk1.push(e._iv);
					bFinished = false;
					break; // from for(iv)
				}
			}

			if (bFinished)
			{
				v._tE = t++;
				if (preFn)
					preFn(v);
				stk1.pop();
			}
		}
	}

	void BFS(int is)
	{
		reset();
		std::queue<int> Q;
		_vs[is]._dist = 0;
		Q.push(is);

		while (!Q.empty())
		{
			int iu = Q.front();
			Q.pop();
			vert& u = _vs[iu];
			for (auto& e : u._adj)
			{
				vert& v = _vs[e._iv];
				if (v._dist == -1)
				{
					v._dist = u._dist + 1;
					v._prev = iu;
					Q.push(e._iv);
				}
			}
		}		
	}

	

	bool getShortestPath(std::list<int>& Path, int is, int iv)
	{
		Path.clear();
		
		BFS(is);
		if (_vs[iv]._dist == -1)
			return false; // no path between is and iv
		
		Path.push_front(iv);
		iv = _vs[iv]._prev;
		while (iv != -1)
		{
			Path.push_front(iv);
			iv = _vs[iv]._prev;
		}

		return true;
	}

	void Dijkstra(int is)
	{
		reset();
		
		const auto less_w = [this](const int iv, const int iu) { return _vs[iv]._fdist < _vs[iu]._fdist; };
		std::set<int, decltype(less_w)> Q(less_w);

		_vs[is]._fdist = 0.f;
		Q.insert(is);

		while (!Q.empty())
		{
			int   iu   = *Q.begin();
			float dist = _vs[iu]._fdist;
			Q.erase(Q.begin());

			for (edge& e : _vs[iu]._adj)
			{
				if (_vs[e._iv]._fdist > dist + e._w)
				{
					Q.erase(e._iv);
					_vs[e._iv]._fdist = dist + e._w;
					_vs[e._iv]._prev = iu;
					Q.insert(e._iv);
				}
			}
		}
	}

	bool BellmanFord( int is )
	{
		reset();
		bool bNWC = false;
		_vs[is]._fdist = 0.f;

		for (int it = 0; it < size(); it++)
		{
			for (int iu = 0; iu < size(); iu++)
			{
				vert& u = _vs[iu];
				if (u._fdist == fMax)
					continue;
				for (edge& e : u._adj)
				{
					vert& v = _vs[e._iv];
					if (v._fdist > u._fdist + e._w)
					{
						v._fdist = u._fdist + e._w;
						v._prev  = iu;
						if (it == size() - 1)
							bNWC = true;
					}
				}
			}
			
		}
		return bNWC;
	}

	float Kruskal( std::vector<edge2>& vST )
	{
		float W = 0.f;

		std::sort(_es.begin(), _es.end(), [](const edge2& e1, const edge2& e2) {return e1._w < e2._w;});
		DisjointSets DS(_vs.size());

		for (auto& e : _es)
		{
			if (DS.Find(e._iu) != DS.Find(e._iv))
			{
				W += e._w;
				vST.push_back(e);
				DS.Union(e._iu, e._iv);
			}
		}

		return W;
	}

};
