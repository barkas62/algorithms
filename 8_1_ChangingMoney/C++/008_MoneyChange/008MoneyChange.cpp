#include <vector>
#include <iostream>

using namespace std;

int MoneyChangeRec(int A, const vector<int>& Coins)
{
	if (A == 0)
		return 0;

	int nChange = INT_MAX;
	for (auto c : Coins)
	{
		if (A - c >= 0)
		{
			int nC = 1 + MoneyChangeRec(A - c, Coins);
			if (nChange > nC)
				nChange = nC;
		}
	}

	return nChange;
}

int MoneyChangeDP(int A, const vector<int>& Coins)
{
	vector<int> vChange(A + 1, INT_MAX);
	vChange[0] = 0;

	for (int m = 1; m <= A; m++)
	{
		for( auto c : Coins)
		{
			if (m - c >= 0)
			{
				int nC = 1 + vChange[m - c];
				if (vChange[m] > nC)
					vChange[m] = nC;
			}
		}
	}

	return vChange[A];
}



int MoneyChangeMM(int A, const vector<int>& Coins) // Memoization
{
	if (A == 0)
		return 0;

	static vector<int> vChange(A+1, INT_MAX); //memo table

	int nChange = INT_MAX;
	for (auto c : Coins)
	{
		if (A - c >= 0)
		{
			if (vChange[A - c] == INT_MAX) 		
				vChange[A - c] = MoneyChangeMM(A - c, Coins); // no memoized value
			
			int	nC = 1 + vChange[A - c];  // use memoized value
			if (nChange > nC)
				nChange = nC;
		}
	}

	return nChange;
}


int main()
{
	//vector<int> Coins{ 1,3,5,10,20,25,50 };
	vector<int> Coins{ 1,5,3,10,20,25,50 };
	int A = 0;//40;


//	int nChange = MoneyChangeRec(A, Coins);
	int nChange1 = MoneyChangeDP(A, Coins);

//	vector<int> vChange(A, INT_MAX); //memo table
	int nChange2 = MoneyChangeMM(A, Coins);
	// 40: 1s; 45: 5s; 50: 100s; 60: inf  
//	cout << nChange << "  " << nChange1;

    return 0;
}

