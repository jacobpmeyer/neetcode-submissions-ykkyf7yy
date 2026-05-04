class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        mh = [-i for i in count.values()]
        heapq.heapify(mh)
        q = deque()
        time = 0
        while mh or q:
            time += 1
            if mh:
                val = 1 + heapq.heappop(mh)
                if val:
                    q.append([val, time + n])
            if q and q[0][1] == time:
                heapq.heappush(mh, q.popleft()[0])
        return time
