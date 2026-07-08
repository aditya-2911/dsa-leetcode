class Solution:
    def maximumSum(self, arr: List[int]) -> int:

        no_delete = arr[0]
        one_delete = float("-inf")
        res = arr[0]

        for i in range(1, len(arr)):
            prev_no_delete = no_delete
            prev_one_delete = one_delete

            no_delete = max(no_delete + arr[i], arr[i])

            if prev_one_delete == float("-inf"):
                val = arr[i]
            else:
                val = prev_one_delete + arr[i]

            one_delete = max(val, prev_no_delete)

            res = max(res, no_delete, one_delete)

        return res
