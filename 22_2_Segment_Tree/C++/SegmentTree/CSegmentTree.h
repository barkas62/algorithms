#pragma once

using namespace std;

#include <vector>
#include <functional>
#include <stdexcept>

template<typename T>
class CSegmentTree
{
	function <T(T, T)> merge_func_;
	vector<T> tree_;
	int data_size_ = -1;

public:
	CSegmentTree(vector<T>& data, function<T(T, T)> merge_func) {
		merge_func_ = merge_func;
		data_size_ = (int)data.size();
		tree_.resize(2* (1<<((int)log2(data_size_)+1)) + 1);
		build_tree(data, 0, data_size_ - 1, 0);
	};

	T query(int i, int j) {
		if ((i > j) || (j < 0) || i >= data_size_)
			throw std::invalid_argument("invalid interval");

		return query(i, j, 0, data_size_ - 1, 0);
	}

protected:
	void build_tree(vector<T>& data, int beg, int end, int root) {
		if (beg == end) {
			tree_[root] = data[beg];
			return;
		}

		int mid = (beg + end) / 2;
		int l_child = 2 * root + 1;
		int r_child = 2 * root + 2;

		build_tree(data, beg, mid, l_child);
		build_tree(data, mid + 1, end, r_child);

		tree_[root] = merge_func_(tree_[l_child], tree_[r_child]);
	}

	T query(int i, int j, int beg, int end, int root) {
		if (i <= beg && j >= end)
			return tree_[root];

		int mid = (beg + end) / 2;
		int l_child = 2 * root + 1;
		int r_child = 2 * root + 2;

		if (i > mid)
			return query(i, j, mid + 1, end, r_child);
		else if (j <= mid)
			return query(i, j, beg, mid, l_child);

		T l_res = query(i, j, beg, mid, l_child);
		T r_res = query(i, j, mid + 1, end, r_child);

		return merge_func_(l_res, r_res);
	}
};

