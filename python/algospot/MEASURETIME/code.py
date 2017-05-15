class FenwickTree:
    tree = []

    def __init__(self, n):
        self.tree = [0]*(n+1)

    def sum(self, pos):
        pos += 1
        ret = 0
        while pos > 0:
            ret += self.tree[pos]
            pos &= (pos-1)
        return ret

    def add(self, pos, val):
        pos += 1
        while pos < len(self.tree):
            self.tree[pos] += val
            pos += (pos & -pos)
        print(self.tree)


class MeasureTimeFenwickTree:
    tree = []

    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def query(self, pos):
        pos += 1
        ret = 0
        while pos > 0:
            print('pos : %s' % pos)
            print(self.tree)
            ret += self.tree[pos]
            pos &= (pos - 1)
        return self.tree[-1] - ret

    # tree[val]에..
    def add(self, pos):
        self.tree[pos] += 1
        pos += 1
        while pos < len(self.tree):
            self.tree[pos] += 1
            pos += (pos & -pos)

class MEASURETIME:
    @staticmethod
    def solve(n, array):
        sorted_array = sorted(array)
        mapped_dict = {}
        idx = 0
        prev = 0
        for i in range(0, n):
            if prev != sorted_array[i]:
                idx += 1
            mapped_dict[sorted_array[i]] = idx
            prev = sorted_array[i]
        mapped_array = []
        for i in range(0, n):
            mapped_array.append(mapped_dict[array[i]])

        print(mapped_array)
        fenwick = MeasureTimeFenwickTree(n)

        acc = 0
        for i in range(0, len(mapped_array)):
            fenwick.add(mapped_array[i])
            print(n)
            print(mapped_array[i]+1)
            print('acc : %s' % acc)
            acc += fenwick.query(mapped_array[i])

        return acc
    # @staticmethod
    # def solve(array):
    #     acc = 0
    #     for i in range(0, len(array)):
    #         c, array = MEASURETIME.insertionSortAndReturnSwapcount(i, array)
    #         acc += c
    #     return acc
    #
    # @staticmethod
    # def insertionSortAndReturnSwapcount(n, array):
    #     count = 0
    #     for i in range(0, n):
    #         if array[n] < array[i]:
    #             count = n - i
    #             # swap
    #             ret = array[n]
    #             del array[n]
    #             array.insert(i, ret)
    #             break
    #     return count, array

    @staticmethod
    def main():
        t = int(input())
        for i in range(0, t):
            n = int(input())
            array = [int(elem) for elem in input().split(' ')]
            print(MEASURETIME.solve(n, array))

if __name__ == "__main__":
    MEASURETIME.main()

