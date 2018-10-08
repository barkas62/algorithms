#include <vector>
#include <algorithm>

#include "gtest/gtest.h"
#include "../006_QuickSort/QuickSort.h"

using namespace std;


TEST(QuickSortTests, Empty)  // Empty vector
{
	vector<int> v;

	int ie = (int)size(v) - 1;

	QuickSortH(v, 0, ie); EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Hoare version failed on line " << __LINE__;

	QuickSortL(v, 0, ie); EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Lomuto version failed on line " << __LINE__;

	QuickSortT(v, 0, ie); EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Trail version failed on line " << __LINE__;

	QuickSortI(v);                 EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Iterative version failed on line " << __LINE__ ;

	QuickSort(begin(v), end(v));   EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Fat partition version failed on line " << __LINE__;

}

TEST(QuickSortTests, Equal) // All elements in vector are equal 
{
	vector<int> v0(1024,0);

	vector<int> v(size(v0));

	int ie = (int)size(v) - 1;

	v = v0;
	QuickSortH(v, 0, ie); EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Hoare version failed on line " << __LINE__;

	v = v0;
	QuickSortL(v, 0, ie); EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Lomuto version failed on line " << __LINE__;

	v = v0;
	QuickSortT(v, 0, ie); EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Trail version failed on line " << __LINE__;

	v = v0;
	QuickSortI(v);                 EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Iterative version failed on line " << __LINE__;

	v = v0;
	QuickSort(begin(v), end(v));   EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Fat partition version failed on line " << __LINE__;

}

TEST(QuickSortTests, Sorted) // Vector is already sorted
{
	vector<int> v0(1024);

	int n = 0;
	generate(begin(v0), end(v0), [&n] { return ++n; });

	vector<int> v(size(v0));

	int ie = (int)size(v) - 1;

	v = v0;
	QuickSortH(v, 0, ie); EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Hoare version failed on line " << __LINE__;

	v = v0;
	QuickSortL(v, 0, ie); EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Lomuto version failed on line " << __LINE__;

	v = v0;
	QuickSortT(v, 0, ie); EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Trail version failed on line " << __LINE__;

	v = v0;
	QuickSortI(v);                 EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Iterative version failed on line " << __LINE__;

	v = v0;
	QuickSort(begin(v), end(v));   EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Fat partition version failed on line " << __LINE__;

}

TEST(QuickSortTests, Random) // Vector is filled with random numbers
{
#ifdef _DEBUG
	int nMaxSize = 1 << 5;
#else
	int nMaxSize = 1 << 10;
#endif

	srand((unsigned int)time(0));

	// nMaxSize tests. Each test generates a random vector of size nSize, which is incremented from test to test 
	for (int nSize = 0; nSize < nMaxSize; nSize++)
	{
		vector<int> v0(nSize);
		generate(begin(v0), end(v0), [&] { return rand() % nSize; });

		vector<int> v(size(v0));
		int ie = (int)size(v) - 1;

		v = v0;
		QuickSortH(v, 0, ie); EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Hoare version failed on line " << __LINE__;

		v = v0;
		QuickSortL(v, 0, ie); EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Lomuto version failed on line " << __LINE__;

		v = v0;
		QuickSortT(v, 0, ie); EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Trail version failed on line " << __LINE__;

		v = v0;
		QuickSortI(v);                 EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Iterative version failed on line " << __LINE__;

		v = v0;
		QuickSort(begin(v), end(v));   EXPECT_TRUE(is_sorted(begin(v), end(v))) << "Fat partition version failed on line " << __LINE__;

	}
}