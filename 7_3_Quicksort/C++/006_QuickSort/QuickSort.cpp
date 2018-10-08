#include <list>
#include <algorithm>
#include <iostream>
#include <fstream>
#include "QuickSort.h"

int main()
{
//	vector<int> v{ 4,6,2,8,5,1 };
	vector<int> v{ 4,4,4,4,4,4 };

//	list<int> L{ 2,1,5,3,2,1 };

//	vector<int> v{
//		8, 29, 34, 54, 63, 9, 45, 41, 45, 39, 23, 31, 47, 52, 57, 29, 8, 52, 24, 39, 57, 54, 20, 40, 18, 25, 35, 19, 7, 15, 62, 11, 6, 33, 26, 0, 8, 51, 26, 27, 38, 10, 3, 29, 47, 11, 48, 3, 55, 6, 7, 44, 49, 50, 43, 61, 1, 58, 51, 5, 11, 57, 28, 29
//	};

	QuickSortI(v);



	int nSize = 1 << 6;

	for (int iTest = 0; iTest < nSize; iTest++)
	{
		vector<int> v0(nSize);
		srand( (unsigned int)time(0));
		//srand(0);

		generate(begin(v0), end(v0), [&] { return rand() % nSize; });

		{
			ofstream ost("g://tmp//vect.txt", ios::trunc);

			for (auto i : v0)
				ost << i << ", ";
		}

		vector<int> v(size(v0));

		v = v0;
		QuickSortH(v, 0, (int)v.size() - 1);

		v = v0;
		QuickSortL(v, 0, (int)v.size() - 1);

		v = v0;
		QuickSortT(v, 0, (int)v.size() - 1);

		v = v0;
		QuickSortI(v);                 

		v = v0;
		QuickSort(begin(v), end(v));   

	}

	//QuickSort(begin(L), end(L)); will not compile: static_assert in QuickSort

    return 0;
}

