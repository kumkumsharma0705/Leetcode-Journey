class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.nums = [0] * self.n          # keep track of current values
        self.tree = [0] * (self.n + 1)    # BIT, 1-indexed

        for i, num in enumerate(nums):
            self.update(i, num)

    def _update_tree(self, index, delta):
        # index is 0-based here; BIT is 1-indexed internally
        i = index + 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def _prefix_sum(self, index):
        # sum of nums[0..index], 0-based
        i = index + 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        delta = val - self.nums[index]
        self.nums[index] = val
        self._update_tree(index, delta)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self._prefix_sum(right) - (self._prefix_sum(left - 1) if left > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)