class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # we have to sort as one car cannot pass th other, so it should be in order
        # sorting: both postion & speed should in sync
        comb = sorted(zip(position, speed), key=lambda x:x[0], reverse=True)
        min_steps = None
        total_fleets = 1
        for each in comb:
            pos, speed = each[0], each[1]
            steps = (target - pos) / speed

            # since starting from right side, set first step as min step
            if min_steps is None:
                min_steps = steps

            # if we need more steps, then not colliding, hence use that right object as reference for the next items
            if not (steps <= min_steps):
                total_fleets += 1
                min_steps = steps

        return total_fleets
        