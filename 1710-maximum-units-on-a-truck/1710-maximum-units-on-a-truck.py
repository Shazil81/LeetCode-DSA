class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        # Same greedy knapsack type wala hai problem
        total = 0
        boxes = 0
        boxTypes.sort(key=lambda x:x[1], reverse = True)
        for box, units in boxTypes:
            if boxes + box <= truckSize:
                boxes += box
                total += (box * units)
            
            else:
                fraction = truckSize - boxes
                total += (fraction * units)
                break
        
        return total