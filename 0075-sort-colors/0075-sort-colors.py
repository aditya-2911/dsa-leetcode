class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            left = [x for x in arr[1:] if x < pivot]
            right = [x for x in arr[1:] if x >= pivot]
            return quick_sort(left) + [pivot] + quick_sort(right)

        arr[:]= quick_sort(arr)
