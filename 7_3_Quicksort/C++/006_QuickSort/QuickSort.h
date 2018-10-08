#pragma once

#include <vector>
#include <stack>
#include <time.h>
#include <tuple>

using namespace std;

template<typename T>
int PartitionL(vector<T>& v, int ib, int ie) // Lomuto scheme, bad for vectors with all equal elements
{
	srand((unsigned)time(0));
	int im = ib + rand() % (ie - ib + 1);    // Find random pivot 
	swap(v[ib], v[im]);                      // Swap it into first element 

	im = ib;
	T pivot = v[ib];

	for (size_t i = ib + 1; i <= ie; ++i)
	{
		if (v[i] <= pivot)                  // invariant violated
			swap(v[++im], v[i]);            // move pivot position to the right, then swap violating element   
	}

	swap(v[ib], v[im]);                     // swap pivot into its position

	return im;
}

template<typename T>
int PartitionH(vector<T>& v, int ib, int ie) // Hoare scheme
{
	srand((unsigned)time(0));
	int im = ib + rand() % (ie - ib + 1);
	swap(v[ib], v[im]);

	T pivot = v[ib];

	int iDn = ib;
	int iUp = ie + 1;
	while (true)
	{
		while (pivot > v[++iDn] && iDn < ie);
		while (pivot < v[--iUp]);

		if (iDn < iUp)
			swap(v[iDn], v[iUp]);
		else
			break;
	}

	swap(v[ib], v[iUp]);
	return iUp;
}

template<typename T>
void QuickSortH(vector<T>& v, int ib, int ie)   // Hoare partition
{
	if (ib >= ie)
		return;

	int im = PartitionH(v, ib, ie);

	QuickSortH(v, ib, im - 1);  // because of -1 we need to use signed int
	QuickSortH(v, im + 1, ie);
}

template<typename T>
void QuickSortL(vector<T>& v, int ib, int ie)  // Lomuto partition
{
	if (ib >= ie)
		return;

	int im = PartitionH(v, ib, ie);
	QuickSortL(v, ib, im - 1);
	QuickSortL(v, im + 1, ie);
}


template<typename T>
void QuickSortT(vector<T>& v, int ib, int ie) // Trailing recursion eliminated
{
	while (ib < ie)
	{ 
		int im = PartitionH(v, ib, ie);

		if (im - ib < ie - im)
		{
			QuickSortT(v, ib, im - 1);
			ib = im + 1;
		}
		else
		{
			QuickSortT(v, im + 1, ie);
			ie = im - 1;
		}
	}

}


template<typename T>
void QuickSortI(vector<T>& v)  // Iterative version
{
	if (v.size() <= 1)
		return;

	stack< pair<int, int> > st;
	st.push({ 0, (int)size(v) - 1 });

	while (!st.empty())
	{
		//		auto&[ib, ie] = st.top(); st.pop();  c++17
		int ib, ie;
		std::tie(ib, ie) = st.top(); st.pop();
		int im = PartitionH(v, ib, ie);

		if (im > ib + 1)  // better than im-1 > ib because of type mismatch
			st.push({ ib, im - 1 }); // there are elems on the left side of pivot

		if (im + 1 < ie)
			st.push({ im + 1, ie }); // there are elems on the right side of pivot
	}
}

template <typename RandIt>
pair<RandIt, RandIt> Partition3(RandIt it1, RandIt it2)  // Fat pivot
{
	size_t L = distance(it1, it2);

	srand((unsigned)time(0));
	size_t iPivot = rand() % L;

	swap(*it1, *next(it1, iPivot));

	// *it is a Pivot now
	RandIt itE = next(it1); // start of "equal" range
	RandIt itM = next(it1); // start of "more"  range
	RandIt itC = next(it1); // current

	for (; itC != it2; itC = next(itC))
	{
		if (*itC == *it1)
		{
			swap(*itC, *itM);
			itM = next(itM);
		}
		else
			if (*itC < *it1)
			{
				swap(*itC, *itM);
				swap(*itM, *itE);
				itE = next(itE);
				itM = next(itM);
			}
	}

	itE = prev(itE);
	swap(*it1, *itE);

	return { itE, itM };
}


template <typename RandIt>
void QuickSort(RandIt it1, RandIt it2)  // Generic (stl-style) with fat pivot
{
	// Compiler check that RandIt is a Random Access iterator  
	static_assert ( is_same<iterator_traits<RandIt>::iterator_category, random_access_iterator_tag>::value, "QuickSort needs random iterators as parameters" );

	if (it1 == it2 || next(it1) == it2) // empty or size=1
		return;

	auto pivot = Partition3(it1, it2);

	QuickSort(it1, pivot.first);
	QuickSort(pivot.second, it2);
}