// SegmentTree.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <vector>
#include <iostream>
#include "CSegmentTree.h"
#include <conio.h>

int add(int x, int y) { return x + y; }

int main()
{
    std::vector<int> data = { 1,3,7,9,11,13 };
    CSegmentTree<int> st = CSegmentTree<int>(data, &add);

    for(int i = 0; i < data.size(); ++i)
        for (int j = i; j < data.size(); ++j)
        {
            int res1 = st.query(i, j);
            int res2 = 0;
            for (int k = i; k <= j; ++k)
                res2 += data[k];
            if (res1 != res2)
                std::cout << "Error: " << i << j;
            else
                std::cout << "OK: " << res1 << " " << res2 << "\n";
        }

    _getch();
    return 0;
}


