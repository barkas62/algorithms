import math
import operator

class SegTree:
    def __init__(self, data, merge_func):
        if data is None or merge_func is None:
            return
        self.n_data = len(data)
        if self.n_data == 0:
            return
        n = 2 * 2**math.ceil(math.log2(self.n_data)) - 1
        self.arr = [None]*n
        self.merge = merge_func
        self._build(data, 0, 0, self.n_data - 1)

    def _build(self, data, root_idx, beg_idx, end_idx):
        if beg_idx == end_idx: # it's a leaf
            self.arr[root_idx] = data[beg_idx]
            return

        left_child_idx = 2*root_idx + 1
        right_child_idx = 2*root_idx + 2
        mid_idx = (beg_idx + end_idx)//2

        self._build(data, left_child_idx,  beg_idx,   mid_idx)
        self._build(data, right_child_idx, mid_idx+1, end_idx)

        self.arr[root_idx] = self.merge(self.arr[left_child_idx], self.arr[right_child_idx])

    def _update(self, arr_idx, new_val, root_idx, beg_idx, end_idx):
        if beg_idx == end_idx:
            self.arr[root_idx] = new_val
            return

        left_child_idx = 2*root_idx + 1
        right_child_idx = 2*root_idx + 2
        mid_idx = (beg_idx + end_idx)//2

        if arr_idx > mid_idx:
            self._update(arr_idx, new_val, right_child_idx, mid_idx+1, end_idx)
        else:
            self._update(arr_idx, new_val, left_child_idx, beg_idx, mid_idx)
        self.arr[root_idx] = self.merge(self.arr[left_child_idx], self.arr[right_child_idx])

    def update(self, arr_idx, new_val ):
        self._update(arr_idx, new_val, 0, 0, self.n_data - 1)

    def _query(self, i, j, root_idx, beg_idx, end_idx):
        if i <= beg_idx and end_idx <= j:   # segment is completely inside the range
            return self.arr[root_idx]
        if j < beg_idx or i > end_idx:
            return None

        left_child_idx = 2*root_idx + 1
        right_child_idx = 2*root_idx + 2
        mid_idx = (beg_idx + end_idx)//2

        if i > mid_idx:
            return self._query(i, j, right_child_idx, mid_idx+1, end_idx)
        elif j <= mid_idx:
            return self._query(i, j, left_child_idx, beg_idx, mid_idx)

        left_res  = self._query(i,         mid_idx, left_child_idx,  beg_idx,   mid_idx)
        right_res = self._query(mid_idx+1, j,       right_child_idx, mid_idx+1, end_idx)
        return self.merge(left_res, right_res)

    def query(self, i, j):
        return self._query(i, j, 0, 0, self.n_data-1)


nums = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]
#nums = []
#st = SegTree(nums, operator.add)
st = SegTree(nums, max)
res = st.query(2,8)

pass