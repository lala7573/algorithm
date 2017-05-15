import math
import queue


class Stall:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.next_idx = int((start + end) / 2)
        self.Ls = self.next_idx - start
        self.Rs = end - self.next_idx

    def get_tuple(self):
        return -self.Ls, -self.Rs, self.next_idx, self.start, self.end

    def get_next_stall(self):
        first = (self.start, self.next_idx-1)
        second = (self.next_idx + 1, self.end)

        if self.Ls == 0:
            return [second]
        if self.Rs == 0:
            return [first]

        if self.Ls >= self.Rs:
            return [first, second]
        else:
            return [second, first]


class BathroomStalls:
    @staticmethod
    def brute_force(n, k):
        occupied = [0, n+1]
        for i in range(0, k-1):
            next_stall = BathroomStalls.get_next_stall(occupied)
            print(next_stall)
            occupied.append(next_stall[0])
            occupied = sorted(occupied)
        ret = BathroomStalls.get_next_stall(occupied)
        # print(ret)
        return ret[2], ret[1]

    @staticmethod
    def get_next_stall(occupied):
        len_occupied = len(occupied)

        maximize_min = 0
        maximize_max = 0
        stall_min_max = []
        for i in range(0, len_occupied - 1):
            for j in range(occupied[i]+1, occupied[i + 1]):
                Rs = occupied[i + 1] - j - 1
                Ls = j - occupied[i] - 1
                min_of_Ls_Rs = min(Ls, Rs)
                max_of_Ls_Rs = max(Ls, Rs)
                if maximize_min < min_of_Ls_Rs:
                    maximize_min = min_of_Ls_Rs
                stall_min_max.append((j, min_of_Ls_Rs, max_of_Ls_Rs))

        # choose
        maximized_min_list = []
        for min_max in stall_min_max:
            if min_max[1] == maximize_min:
                if maximize_max < min_max[2]:
                    maximize_max = min_max[2]
                maximized_min_list.append(min_max)

        for min_max in maximized_min_list:
            if min_max[2] == maximize_max:
                return min_max

    @staticmethod
    def bathroom_stalls(n, k):
        stalls_ranges = []
        stalls_info = queue.PriorityQueue()
        stall = Stall(1, n)
        stalls_info.put(stall.get_tuple())
        stalls_ranges.extend(stall.get_next_stall())

        max_k = 2 ** math.ceil(math.log(k, 2))
        for _ in range(1, max_k):
            target = stalls_ranges.pop(0)
            stall = Stall(*target)
            stalls_info.put(stall.get_tuple())
            stalls_ranges.extend(stall.get_next_stall())

        x = None
        for _ in range(0, k):
            x = stalls_info.get()
            print(x)
        return -x[1], -x[0]

    @staticmethod
    def solve(n, k):
        x = BathroomStalls.brute_force(n, k)
        # x = BathroomStalls.bathroom_stalls(n, k)
        return x

    @staticmethod
    def main():
        t = int(input())
        for i in range(0, t):
            s = input()
            n, k = s.split(' ')
            print('Case #%s: %s' % (i+1, '%s %s' % BathroomStalls.solve(int(n), int(k))))

if __name__ == "__main__":
    BathroomStalls.main()
