import sys
sys.stdin = open('input.txt')

def dij():
    dist = [987654321] * (V+1)
    dist[0] = 0



V, E = map(int, input().split())
adj = [[987654321] * (V+1) for _ in range(V+1)]
for i in range(E):
    s, e, w = map(int, input().split())
    adj[s][e] = w

