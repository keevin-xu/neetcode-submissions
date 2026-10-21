class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        out = len(speed)
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        stack.append((target - cars[0][0])/cars[0][1])
        for i in range(1, len(cars)):
            aheadTime = stack.pop()
            currtime = (target - cars[i][0])/cars[i][1]
            if currtime <= aheadTime:
                out -= 1
                stack.append(aheadTime)
            else:
                stack.append(currtime)
        return out