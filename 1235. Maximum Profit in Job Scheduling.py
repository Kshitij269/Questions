startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]

intervals = sorted(zip(startTime,endTime,profit))
intervals = sorted(zip(startTime,endTime,profit))
        cache={}
        def dfs(i):
            if i==len(intervals):
                return 0
            if i in cache:
                return cache[i]

            #dont include
            res = dfs(i+1)

            #include
            j=bisect.bisect(intervals,(intervals[i][1],-1,-1))
            cache[i] = res = max(res,intervals[i][2]+dfs(j))
            return res

        return dfs(0)