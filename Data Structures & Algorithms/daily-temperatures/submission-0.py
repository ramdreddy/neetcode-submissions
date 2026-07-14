class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        final = [0]*len(temperatures)
        for i in range(len(temperatures)):
            val = temperatures[i]
            if ans:
                while(ans and val > temperatures[(ans[-1])]):
                    final[ans[-1]] = (i - ans[-1])
                    ans.pop()
            ans.append(i)
        return final
