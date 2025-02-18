class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        List = []
        for i in nums:
            List.append(str(i))
        for i in range(len(List)-1):
            for j in range(i+1,len(List)):
                val1 = List[i]+List[j]
                val2 = List[j]+List[i]
                if (val1 < val2):
                    List[i],List[j] = List[j],List[i]
        result = ''.join(List)

        if result[0] == '0':
            result = '0'
        return result 

    
        

        
