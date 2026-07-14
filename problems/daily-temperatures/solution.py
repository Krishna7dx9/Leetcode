class Solution(object):
    def dailyTemperatures(self, temperatures):
        
        answer = [0]*len(temperatures)
        unresolved = []

        for i in range(len(temperatures)):
            while len(unresolved) > 0 and temperatures[i] > unresolved[-1][0]:
                temp, idx = unresolved.pop()
                answer[idx] = i - idx
            unresolved.append((temperatures[i], i))
        return answer