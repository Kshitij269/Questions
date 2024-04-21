class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        number = "123456789"
        low_count = len(str(low))
        high_count = len(str(high))
        while high_count >= low_count :
            for i in range(0,len(number)-low_count+1):
                if low<=int(number[i:i+low_count])<=high:
                    ans.append(int(number[i:i+low_count]))
            low_count+=1
        return ans 