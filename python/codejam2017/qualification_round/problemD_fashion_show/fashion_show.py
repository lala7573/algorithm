
class FashionShow:
    @staticmethod
    def get_N_grid(n):
        return [[0 for x in range(n)] for y in range(n)]
    @staticmethod
    def solve(n, m, m_list):

        pass

    @staticmethod
    def main():
        t = int(input())
        for i in range(0, t):
            n_and_m = input()
            n, m = n_and_m.split(' ')
            n, m = int(n), int(m)
            m_list = []
            for j in range(0, m):
                line_m = input()
                char, r, c = line_m.split(' ')
                r, c = int(r), int(c)
                m_list.append((char, r, c))

            print('Case #%s: %s' % (i+1, FashionShow.solve(n, m, m_list)))

if __name__ == "__main__":
    FashionShow.main()
