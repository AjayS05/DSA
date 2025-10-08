class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_string = len(strs[0])
        for i in range (1,len(strs)):
            smallest_string = min(len(strs[i]), smallest_string)


        low = 0
        high = smallest_string - 1
        prefix_len = 0

        while low <= high:
            mid = low + (high - low) // 2
            print("mid: ", mid)
            if self.substring_common(strs,low, mid) is True:
                prefix_len = mid + 1
                low = mid + 1
                print("low: ",low)
            else:
                high = mid - 1
                print("high: ", high)
            print("prefix: ",prefix_len)
        return strs[0][:prefix_len]

    def substring_common(self,arr, low, high):
        for i in range(1, len(arr)):
            for j in range(low, high+1):
                if arr[i][j] != arr[0][j]:
                    return False
        return True