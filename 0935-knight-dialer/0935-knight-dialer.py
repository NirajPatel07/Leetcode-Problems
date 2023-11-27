class Solution:
    def knightDialer(self, N):
        
        '''
        State Transfer function
        Cur state comes from previous state
        0         <-> 4, 6
        1         <-> 6, 8
        2         <-> 7, 9
        3         <-> 4, 8
        4         <-> 0, 3, 9
        5         <-> NULL (i.e. No solution when length >= 2 )
        6         <-> 0, 1, 7
        7         <-> 2, 6 
        8         <-> 1, 3
        9         <-> 2, 4
        '''

        CONSTANT = 10**9+7
        method_count = [1 for _ in range(10)]

        for step in range(N-1):
            prev = method_count.copy()
            method_count[0] = prev[4] + prev[6]
            method_count[1] = prev[6] + prev[8]
            method_count[2] = prev[7] + prev[9]
            method_count[3] = prev[4] + prev[8]
            method_count[4] = prev[0] + prev[3] + prev[9]
            method_count[5] = 0 # NULL
            method_count[6] = prev[0] + prev[1] + prev[7]
            method_count[7] = prev[2] + prev[6]
            method_count[8] = prev[1] + prev[3]
            method_count[9] = prev[2] + prev[4]

        return sum(method_count) % CONSTANT