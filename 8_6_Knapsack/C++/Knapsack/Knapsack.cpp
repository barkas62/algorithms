#include <vector>
#include <algorithm>

using namespace std;
using wv_pair = pair<int, int>;

//Fractional
float KnapsackFrac(int W, vector<wv_pair>& Items)
{
	float maxVal = 0;
	sort(Items.begin(), Items.end(), [](wv_pair& p1, wv_pair& p2) {
		return float(p1.second)/p1.first >float(p2.second)/p2.first; } );

	int Capacity = W;
	for( auto&it : Items )
	{
		auto[iw, iv] = it;
		if (iw > Capacity)
		{
			maxVal += float(Capacity*iv) / iw;
			break;
		}
		{
			maxVal   += iv;
			Capacity -= iw;
		}
	}

	return maxVal;
}

// With repetitions
int KnapsackMult(int W, const vector<pair<int, int>>& Items)
{
	vector<int> V(W + 1, 0);
	
	for (auto w = 1; w <= W; ++w)
	{
		for (auto& it : Items)
		{
			auto[iw, iv] = it;
			if (w - iw >= 0)
			{
				auto newV = V[w - iw] + iv;
				if (V[w] < newV)
					V[w] = newV;
			}
		}
	}

	return V[W];
}

// Without repetitions
int Knapsack01(int W, const vector<pair<int, int>>& Items)
{
	int nItems = size(Items);
	vector<vector<int>> V(nItems+1, vector<int>(W + 1, 0));

	for (int i = 1; i <= nItems; ++i)
	{
		auto[iw, iv] = Items[i - 1];
		for (int w = 1; w <= W; ++w)
		{
			V[i][w] = V[i - 1][w];
			
			if (w >= iw)
			{
				int newV = V[i-1][w-iw] + iv;
				if (V[i][w] < newV)
					V[i][w] = newV;
			}
		}
	}
	return V[nItems][W];
}


int main()
{
	int W = 10;
	vector<pair<int, int>> Items{ {2,9} ,{6,30}, {4,16}, {3,14} };

	int   Val0 = Knapsack01(W, Items);
	int   ValM = KnapsackMult(W, Items);
	float ValF = KnapsackFrac(W, Items);

    return 0;
}

