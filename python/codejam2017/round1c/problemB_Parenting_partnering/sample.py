

class ParentingPartner:
    @staticmethod
    def solve(ac, aj, ac_activities, aj_activities):
        ac_activities = sorted(ac_activities, key=lambda x: x[0])
        aj_activities = sorted(aj_activities, key=lambda x: x[0])
        # toggle count를 구한 후
        day = []

        aj_i = 0
        for activity in ac_activities:
            if aj_i == aj:
                day.append(('Ac', activity))
                continue

            if activity < aj_activities[aj_i]:
                day.append(('Ac', activity))
            else:
                day.append(('Aj', aj_activities[aj_i]))
                aj += 1
        print(aj_i, aj)
        while aj_i != aj:
            day.append(('Aj', aj_activities[aj_i]))
            aj_i += 1

        print(day)
        # 720시간을 맞춰준다

        return 2

    @staticmethod
    def main():
        t = int(input())
        for i in range(0, t):
            ac, aj = [int(x) for x in input().split(" ")]
            ac_array = []
            aj_array = []
            for j in range(0, ac):
                ac_array.append([int(x) for x in input().split(" ")])
            for j in range(0, aj):
                aj_array.append([int(x) for x in input().split(" ")])
            print('Case #%s: %s' % (i+1, ParentingPartner.solve()))

if __name__ == "__main__":
    ParentingPartner.main()
