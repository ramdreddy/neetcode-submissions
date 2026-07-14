class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        ans = []
        ans.append(cars[0])
        for car in cars:
            t = ans[-1]
            ctime = (target - car[0])/car[1]
            ttime = (target - t[0])/t[1]
            if ctime > ttime:
                ans.append(car)
        return len(ans)
            


        