class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        q, seen = deque([(0, 0, 0)]), set()
        while q:
            p, l, t = q.popleft()
            if p == x: return l
            if (p, t) in seen: continue
            seen.add((p, t))
            for s, tt in (a, 1), (-b, 2):
                if tt * t == 4: continue
                pp = p + s
                if pp not in forbidden and (pp, tt) not in seen and 0 <= pp < 6000:
                    q.append((pp, l + 1, tt))
        return -1