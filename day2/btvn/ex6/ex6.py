p, q, r, s, u, v = map(int, open("FBALL.INP").read().split(" "))
teamA = (3 if p > q else 1 if p == q else 0) + (3 if r > s else 1 if r == s else 0)
teamB = (3 if q > p else 1 if q == p else 0) + (3 if u > v else 1 if u == v else 0)
teamC = (3 if s > r else 1 if s == r else 0) + (3 if v > u else 1 if p == q else 0)

# if p > q:
#     teamA += 3
# elif p == q:
#     teamA += 1
#     teamB += 1
# else:
#     teamB += 3
#
# if r > s:
#     teamA += 3
# elif r == s:
#     teamA += 1
#     teamC += 1
# else:
#     teamC += 3

# if u > v:
#     teamB += 3
# elif u == v:
#     teamC += 1
#     teamB += 1
# else:
#     teamC += 3
with open("FBALL.OUT", "w")  as f:
    f.write(f"{str(teamA)} {str(teamB)} {str(teamC)}")