import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        requests_handled = [0] * k
        
        available_servers = [i for i in range(k)]
        heapq.heapify(available_servers)
        
        busy_servers = []
        
        for i in range(len(arrival)):
            arr_time = arrival[i]
            task_load = load[i]
            
            while busy_servers and busy_servers[0][0] <= arr_time:
                free_time, s_id = heapq.heappop(busy_servers)
                
                multiplier = max(0, (i - s_id + k - 1) // k)
                shifted_id = s_id + multiplier * k
                
                heapq.heappush(available_servers, shifted_id)
                
            while available_servers and available_servers[0] < i:
                val = heapq.heappop(available_servers)
                heapq.heappush(available_servers, val + k)
                
            if available_servers:
                assigned_shifted_id = heapq.heappop(available_servers)
                
                assigned_server = assigned_shifted_id % k 
                requests_handled[assigned_server] += 1
                
                heapq.heappush(busy_servers, (arr_time + task_load, assigned_server))
                

        max_handled = max(requests_handled)
        return [i for i, count in enumerate(requests_handled) if count == max_handled]