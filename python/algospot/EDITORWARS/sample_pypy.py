#
# class NaiveDisjointSet:
#     """
#     union에서 합성되는 것이 기울어진 트리를 만들 수 있어서 최악의 경우 O(N)이 될 수 있다
#     """
#     def __init__(self, n):
#         self.parent = [None] * n
#         for i in range(0, n):
#             self.parent[i] = i
#
#     def find(self, u):
#         if self.parent[u] == u:
#             return u
#         return self.find(self.parent[u])
#
#     def union(self, u, v):
#         u = self.find(u)
#         v = self.find(v)
#         if u == v:
#             return
#         self.parent[u] = v
#
#
# class OptimizedDisjointSet:
#     def __init__(self, n):
#         self.parent = [None] * n
#         self.rank = [1] * n
#         for i in range(0, n):
#             self.parent[i] = i
#
#     def find(self, u):
#         if self.parent[u] == u:
#             return u
#         self.parent[u] = self.find(self.parent[u])
#         return self.parent[u]
#
#     def union(self, u, v):
#         u = self.find(u)
#         v = self.find(v)
#         if u == v:
#             return
#         if self.rank[u] > self.rank[v]:
#             # swap and make v is bigger than u
#             tmp = v
#             v = u
#             u = tmp
#         self.parent[u] = v
#         if u == v:
#             self.rank[v] += 1
#
#
# class EditorParty:
#     def __init__(self, n):
#         self.enemy = [-1] * n
#         self.rank = [1] * n
#         self.size = [1] * n
#         self.parent = [None] * n
#         for i in range(0, n):
#             self.parent[i] = i
#
#     def find(self, u):
#         if self.parent[u] == u:
#             self.parent[u] = u
#             return u
#         self.parent[u] = self.find(self.parent[u])
#         return self.parent[u]
#
#     def union(self, u, v):
#         if u == -1 or v == -1:
#             # ignore
#             return max(u, v)
#         u = self.find(u)
#         v = self.find(v)
#         if u == v:
#             return v
#         if self.rank[u] > self.rank[v]:
#             # swap and make v is bigger than u
#             tmp = v
#             v = u
#             u = tmp
#         self.parent[u] = v
#         self.size[v] += self.size[u]
#         if u == v:
#             self.rank[v] += 1
#         return v
#
#     def ack(self, u, v):
#         u = self.find(u)
#         v = self.find(v)
#         # 적인지 확인한다
#         if u == self.enemy[u] or v == self.enemy[v]:
#             return False
#         a = self.union(u, v)
#         b = self.enemy[a] = self.union(self.enemy[u], self.enemy[v])
#         if b != -1:
#             self.enemy[b] = a
#
#     def dis(self, u, v):
#         u = self.find(u)
#         v = self.find(v)
#         if u == v:
#             return False
#
#         self.enemy[v] = self.union(u, self.enemy[v])
#         self.enemy[u] = self.union(v, self.enemy[u])
#
#
# class EditorWars:
#     @staticmethod
#     def solve(n, m, m_list):
#         # print("%s, %s, %s" % (n, m, m_list))
#         party = EditorParty(n)
#         for i in range(0, m):
#             info, a, b = m_list[i]
#             if info:
#                 if party.ack(a, b) is False:
#                     return False, i + 1
#             else:
#                 if party.dis(a, b) is False:
#                     return False, i + 1
#
#         acc = 0
#         for i in range(0, n):
#             if party.parent[i] == i:
#                 enemy = party.enemy[i]
#                 if enemy > i:
#                     continue
#                 acc += max(party.size[i], party.size[enemy])
#
#         return True, acc
#
#     @staticmethod
#     def main():
#         t = int(raw_input())
#         for i in range(0, t):
#             n, m = map(int, raw_input().split())
#             m_list = []
#             for j in range(0, m):
#                 info, a, b = raw_input().split()
#                 info = True if info == 'ACK' else False
#                 a = int(a)
#                 b = int(b)
#                 m_list.append((info, a, b))
#
#             result, value = EditorWars.solve(n, m, m_list)
#             if result:
#                 print "MAX PARTY SIZE IS %s" % value
#             else:
#                 print "CONTRADICTION AT %s" % value
#
# if __name__ == "__main__":
#     EditorWars.main()
