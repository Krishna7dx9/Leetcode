class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleet_count = 1
        cars = [] # (position, arrival_time)

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))

        cars.sort(key=lambda car: car[0], reverse = True)

        if len(position) > 0:
            fleet_time = cars[0][1]

        for i in range(1, len(cars)):
            if cars[i][1] > fleet_time:
                fleet_count += 1
                fleet_time = cars[i][1]

        return fleet_count