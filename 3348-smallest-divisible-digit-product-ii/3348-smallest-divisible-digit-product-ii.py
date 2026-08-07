from collections import deque

class Solution:
    def smallestNumber(self, num, t):
        factors = {1:(0,0,0,0), 2:(1,0,0,0), 3:(0,1,0,0), 4:(2,0,0,0),
                   5:(0,0,1,0), 6:(1,1,0,0), 7:(0,0,0,1), 8:(3,0,0,0), 9:(0,2,0,0)}

        # Factor t into powers of 2,3,5,7 — if anything else is left, impossible.
        e2 = e3 = e5 = e7 = 0
        tt = t
        while tt % 2 == 0: tt //= 2; e2 += 1
        while tt % 3 == 0: tt //= 3; e3 += 1
        while tt % 5 == 0: tt //= 5; e5 += 1
        while tt % 7 == 0: tt //= 7; e7 += 1
        if tt != 1:
            return "-1"
        target = (e2, e3, e5, e7)

        def cap(s):
            a, b, c, d = s
            return (a if a < e2 else e2, b if b < e3 else e3,
                    c if c < e5 else e5, d if d < e7 else e7)

        # Enumerate the (small) state space and index it.
        all_states = [(a, b, c, d)
                      for a in range(e2 + 1)
                      for b in range(e3 + 1)
                      for c in range(e5 + 1)
                      for d in range(e7 + 1)]
        index = {s: i for i, s in enumerate(all_states)}
        n_states = len(all_states)

        # Reverse graph: for state s, digit d moves s -> nxt (forward edge).
        # Store reverse edges nxt -> s so we can BFS backward from target.
        rev = [[] for _ in range(n_states)]
        for s in all_states:
            si = index[s]
            for d in range(1, 10):
                fa, fb, fc, fd = factors[d]
                nxt = cap((s[0]+fa, s[1]+fb, s[2]+fc, s[3]+fd))
                ni = index[nxt]
                if ni != si:
                    rev[ni].append(si)

        # BFS from target gives, for every state, the minimum number of
        # digits needed to reach target — this replaces the old
        # recursive feasible(remaining_len, state) memoization.
        INF = float('inf')
        dist = [INF] * n_states
        ti = index[target]
        dist[ti] = 0
        q = deque([ti])
        while q:
            u = q.popleft()
            for v in rev[u]:
                if dist[v] == INF:
                    dist[v] = dist[u] + 1
                    q.append(v)

        def min_digits(state):
            return dist[index[state]]

        def smallest_suffix(remaining_len, state):
            res = []
            cur = state
            for pos in range(remaining_len):
                left = remaining_len - pos - 1
                for d in range(1, 10):
                    fa, fb, fc, fd = factors[d]
                    nxt = cap((cur[0]+fa, cur[1]+fb, cur[2]+fc, cur[3]+fd))
                    if left >= min_digits(nxt):
                        res.append(str(d))
                        cur = nxt
                        break
            return "".join(res)

        n = len(num)
        digits = [int(c) for c in num]

        # Precompute prefix states and first-zero index in O(n),
        # instead of recomputing them inside the loop below.
        prefix_states = [(0, 0, 0, 0)] * (n + 1)
        first_zero = n
        seen_zero = False
        for i, dgt in enumerate(digits):
            if dgt == 0:
                if not seen_zero:
                    first_zero = i
                    seen_zero = True
                prefix_states[i + 1] = prefix_states[i]
            else:
                fa, fb, fc, fd = factors[dgt]
                s = prefix_states[i]
                prefix_states[i + 1] = cap((s[0]+fa, s[1]+fb, s[2]+fc, s[3]+fd))

        # Case 1: num itself already works.
        if not seen_zero and prefix_states[n] == target:
            return num

        # Case 2: keep some prefix of num unchanged, modify the rest
        # (same total length). Try shortest modified suffix first.
        for k in range(1, n + 1):
            plen = n - k
            if plen > first_zero:
                continue  # prefix would contain a zero
            prefix_state = prefix_states[plen]
            orig_pivot = digits[plen]
            start_d = orig_pivot + 1 if orig_pivot >= 1 else 1
            rest_len = k - 1
            for d in range(start_d, 10):
                fa, fb, fc, fd = factors[d]
                state_after = cap((prefix_state[0]+fa, prefix_state[1]+fb,
                                    prefix_state[2]+fc, prefix_state[3]+fd))
                if rest_len >= min_digits(state_after):
                    suffix = smallest_suffix(rest_len, state_after)
                    return num[:plen] + str(d) + suffix

        # Case 3: no same-length answer exists — need an extra digit
        # (or more, if that's still not enough).
        M = min_digits((0, 0, 0, 0))
        total_len = max(n + 1, M)
        return smallest_suffix(total_len, (0, 0, 0, 0))