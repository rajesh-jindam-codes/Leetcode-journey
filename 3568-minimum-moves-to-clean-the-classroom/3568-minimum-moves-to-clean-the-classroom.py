from collections import deque

class Solution:
    def minMoves(self, classroom, energy):

        m = len(classroom)
        n = len(classroom[0])

        start_r = start_c = 0
        litter_id = {}

        # Find S and number all L cells
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c

                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = len(litter_id)

        k = len(litter_id)

        # No litter
        if k == 0:
            return 0

        target = (1 << k) - 1

        # visited[r][c] is a dictionary:
        # mask -> maximum energy remaining
        visited = [[{} for _ in range(n)] for _ in range(m)]

        q = deque()

        # r, c, energy, mask, distance
        q.append((start_r, start_c, energy, 0, 0))

        visited[start_r][start_c][0] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:

            r, c, e, mask, dist = q.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                # Every move costs 1 energy
                if e == 0:
                    continue

                ne = e - 1
                nmask = mask

                cell = classroom[nr][nc]

                # Collect litter
                if cell == 'L':
                    bit = litter_id[(nr, nc)]
                    nmask |= (1 << bit)

                # Reset energy
                if cell == 'R':
                    ne = energy

                # All litter collected
                if nmask == target:
                    return dist + 1

                # Check whether this state is dominated
                old_energy = visited[nr][nc].get(nmask, -1)

                if ne <= old_energy:
                    continue

                # This state is better because it has more energy
                visited[nr][nc][nmask] = ne

                q.append((nr, nc, ne, nmask, dist + 1))

        return -1