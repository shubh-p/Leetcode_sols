import sortedcontainers
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for i in buildings:
            events.append((0, i[0], i[2]))
            events.append((1, i[1], i[2]))
            
        events = sorted(events, key = lambda x:(x[1], x[0], -x[2] if x[0] == 0 else x[2]))
        
        # print(events)
        
        result = []
        current_hegihts = sortedcontainers.SortedList([0])
        
        for e in events:
            event_type, index, height = e
            # print(e, current_hegihts)
            if event_type == 0: # start 
                if height > current_hegihts[-1]:
                    result.append([index, height])
                current_hegihts.add(height)
            else:
                current_hegihts.remove(height)
                # print(current_hegihts)
                if height > current_hegihts[-1]:
                    result.append([index, current_hegihts[-1]])
        return result