

class Ratatouille:
    @staticmethod
    def solve(N, P, R, Q):
        smallest = 10000000
        for n in range(N):
            Q[n]/

    @staticmethod
    def main():
        t = int(input())
        for i in range(0, t):
            n_p_input = input()
            N, P = [int(i) for i in n_p_input.split(' ')]

            r_input = input()
            R = [int(r) for r in r_input.split(' ')]

            Q = []
            for n in range(N):
                q_input = input()
                Q.append([int(q) for q in q_input.split(' ')])
            print('Case #%s: %s' % (i+1, Ratatouille.solve(N, P, R, Q)))

if __name__ == "__main__":
    Ratatouille.main()
