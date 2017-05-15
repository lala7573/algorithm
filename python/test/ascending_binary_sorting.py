

class AscendingBinarySorting:
    @staticmethod
    def AscendingBinarySorting(elements):
        elements = sorted(elements)
        elements = sorted(elements, key=lambda i: bin(i).count("1"))
        return elements

    # @staticmethod
    # def main():
    #     t = int(input())
    #     array = []
    #     for i in range(0, t):
    #         array.append(int(input()))
    #     # AscendingBinarySorting.solve(array)

    @staticmethod
    def numberOfPairs(a, k):
        i_count = {}
        for i in a:
            if i not in i_count:
                i_count[i] = 0
            i_count[i] += 1

        # print(a_dict)
        # find pairs
        total = set()
        for i, count in i_count.items():
            if (k - i) in i_count:
                total.add(min(i, k-i))

        return len(total)

    @staticmethod
    def test_string(value):
        stack = []
        for v in value:
            if v == '{' or v == '[' or v == '(':
                stack.append(v)
                continue

            if len(stack) == 0:
                return "NO"

            if v == '}' and stack[-1] == '{':
                stack.pop()
            elif v == ']' and stack[-1] == '[':
                stack.pop()
            elif v == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return "NO"
        if len(stack) == 0:
            return "YES"
        return "NO"

    @staticmethod
    def brace(values):
        ret = []
        for value in values:
            ret.append(AscendingBinarySorting.test_string(value))
        return ret

if __name__ == "__main__":
    # AscendingBinarySorting.AscendingBinarySorting(
    #     [5, 3, 7, 10, 14])
    print(AscendingBinarySorting.numberOfPairs([1, 3, 46, 1, 3, 9], 47))
    print(AscendingBinarySorting.numberOfPairs([6, 6, 3, 9, 3, 5, 1], 12))
    print(AscendingBinarySorting.brace(["{}[]()", "{[}]}"]))
    # AscendingBinarySorting.main()
