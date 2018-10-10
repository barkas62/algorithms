#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <forward_list>
#include <iostream>
#include <iterator>

#include <time.h>

using namespace std;

using uvect = vector<unsigned int>;
using uint = unsigned int;

using fvect = vector<float>; 

void BucketSort(fvect& A)
{
	if (A.size() <=1 )
		return;

	size_t n = A.size();
	vector<fvect> Buckets(n);

	for (auto& a : A)
		Buckets[size_t(n*a)].emplace_back(move(a));

	A.clear();
	for (auto& B : Buckets)
	{
		//	std::move(begin(B), end(B), end(A));    out of bounds exception
		std::move(begin(B), end(B), inserter(A, end(A)));
	}
}

void CountSort(uvect& A)
{
	if (A.empty())
		return;

	uint Max = *max_element(begin(A), end(A));
	uint Min = *min_element(begin(A), end(A));
	if( Max == Min )
		return;

	uvect Sorted(A.size());

	uint M = Max - Min + 1;
	uvect Cnt(M, 0);
	uvect Pos(M, 0);

	for (const uint& a : A)
		++Cnt[a-Min];

	for (size_t i = 1; i < M; ++i)
		Pos[i] = Pos[i - 1] + Cnt[i - 1];

	for (const uint& a : A)
		Sorted[Pos[a-Min]++] = a;

//	move(begin(Sorted), end(Sorted), begin(A));
	A = move(Sorted);

	return;
}



template <typename It>
void InsertionSort(It it1, It it2)
{
	if (it1 == it2 || next(it1) == it2) // empty or size=1
		return;

	for (It it = next(it1); it != it2; it=next(it))
		for (It ir = it; ir != it1 && *ir < *prev(ir); ir = prev(ir))
			swap(*prev(ir), *ir);
}

template <typename It>
void MergeGrow(It itB, It itM, It itE, It Dest)
{
	It it1 = itB;
	It it2 = itM;
	It dst = Dest;
	while( it1 != itM && it2 != itE)
		*dst++ = (*it1 < *it2) ? *it1++ : *it2++;

	while(it1 != itM)
		*dst++ = *it1++;

	while(it2 != itE)
		*dst++ = *it2++;

	It DestE = Dest; advance(DestE, distance(itB, itE));

	copy(Dest, DestE, itB);
}

template <typename It> 
void MergeSort(It itS1, It itS2, It itA)
{
	if (itS1 == itS2 || next(itS1) == itS2) // empty or size=1
		return;

	auto med = distance(itS1, itS2)/2;

	It itS0 = itS1;	advance(itS0, med);

	MergeSort(itS1, itS0, itA);
	MergeSort(itS0, itS2, itA);

	MergeGrow(itS1, itS0, itS2, itA);

	return;
}

template <typename It>
bool isSorted(It it1, It it2)
{
	It itE = prev(it2);
	for (It it = it1; it != itE; ++it)
		if (*it > *next(it))
			return false;

	return true;
}

uvect AA{ 20,3,5,5, 2,2, 4,4,4,1,2,0 };
uvect BB{ 3, 2,1,0 };
uint pA[]{ 3,5,5, 2,2, 4,4,4,1,2,0 };

forward_list<int> L{3,2,6,5,8,9};

fvect F{ 0.1f, 0.8f, 0.2f, 0.01f, 0.9f, 0.99f };

int main()
{
	//CountSort(AA);
	BucketSort(F);

	InsertionSort(begin(AA), end(AA));

	constexpr size_t maxSize = 1000;
	constexpr size_t maxElem = 1000;

	srand((unsigned)time(0));

	uvect TT(AA.size(),-1);
	MergeSort(AA.begin(), AA.end(), TT.begin());

	//QuickSort(AA.begin(), AA.end());
	//QuickSort(pA, pA+11);

//	using cont = uvect;
//	using cont = deque<uint>;
	using cont = list<uint>;

	for (int i = 0; i < 1000; i++)
	{
		size_t rnd = rand();
		size_t nSize = (maxSize*rnd) /(RAND_MAX + 1) + 1;

		cont A(nSize);

		cout << "i: " << i << " nSize: "<<nSize<<endl;

		std::generate(A.begin(), A.end(),
			[maxElem]()
		{	uint Elem = maxElem*rand() / (RAND_MAX + 1);
			if (Elem >= maxElem)
				Elem = maxElem - 1;
			return Elem;
		}
		);

		cont T(A);

//		QuickSort(A.begin(), A.end());
//		MergeSort(A.begin(), A.end(), T.begin());
//		A = CountSort(T);

		if (!isSorted(A.begin(), A.end()))
		{
			cout << "Err!";	break;
		}

	}

	char s;
	cin.get(s);

    return 0;
}

