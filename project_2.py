import math
from scipy.stats import chi2

# objectives: should players be more aggressive, the relation between age and statistics such as games started or fouls made, and the relation between center and agression

file = open("dataset.csv", "r")
data = file.read()
file.close()

data = data.split("\n")
data2 = []
titles = data[0].split(",")

# for i in range(len(titles)):
#     print(i, titles[i])

for i in range(1,len(data)):
    data[i-1] = (data[i].split(","))

data.pop()
n = len(data)
cols = {
    "POS": 1,
    "Age": 2,
    "GS": 5,
    "PF": 27,
    "PTS": 28
}

for i in range(n):
    data[i][cols["Age"]] = float(data[i][cols["Age"]])
    data[i][cols["GS"]] = float(data[i][cols["GS"]])
    data[i][cols["PF"]] = float(data[i][cols["PF"]])
    data[i][cols["PTS"]] = float(data[i][cols["PTS"]])

# a)
print("a)")
means = {
    "Age": 0,
    "GS": 0,
    "PF": 0,
    "PTS": 0
}
stds = {
    "Age": 0,
    "GS": 0,
    "PF": 0,
    "PTS": 0
}

for i in range(n):
    means["Age"] += data[i][cols["Age"]]
    means["GS"] += data[i][cols["GS"]]
    means["PF"] += data[i][cols["PF"]]
    means["PTS"] += data[i][cols["PTS"]]

means["Age"] /= n
means["GS"] /= n
means["PF"] /= n
means["PTS"] /= n

for i in range(n):
    stds["Age"] += (data[i][cols["Age"]] - means["Age"])**2
    stds["GS"] += (data[i][cols["GS"]] - means["GS"])**2
    stds["PF"] += (data[i][cols["PF"]] - means["PF"])**2
    stds["PTS"] += (data[i][cols["PTS"]] - means["PTS"])**2

stds["Age"] = math.sqrt(stds["Age"]/(n-1))
stds["GS"] = math.sqrt(stds["GS"]/(n-1))
stds["PF"] = math.sqrt(stds["PF"]/(n-1))
stds["PTS"] = math.sqrt(stds["PTS"]/(n-1))

variance = {
    "Age": stds["Age"]**2,
    "GS": stds["GS"]**2,
    "PF": stds["PF"]**2,
    "PTS": stds["PTS"]**2
}

print("Means:", means)
print("Stds:", stds)

# proportion
prop_PF = 0
for i in range(n):
    if (data[i][cols["PF"]] >= 2):
        prop_PF += 1
prop_PF /= n

print("Proportion of aggressive players(PF>=2):", prop_PF)

prop_POS = 0
for i in range(n):
    if (data[i][cols["POS"]] == "C"):
        prop_POS += 1
prop_POS /= n

print("Proportion of Center players:", prop_POS)

# b)
print("b)")
intervals = {
    "mean PTS": 0,
    "variance Age": 0,
    "proportion PF": 0,
    "proportion POS": 0
}
# mu = x +- Z_025 * s / root(n)
Z_025 = 1.96
intervals["mean PTS"] = [means["PTS"] - Z_025 * stds["PTS"]/math.sqrt(n), means["PTS"] + Z_025 * stds["PTS"]/math.sqrt(n)]

# pi = p +- Z_025 * root(pq/n)
intervals["proportion PF"] = [prop_PF - Z_025 * math.sqrt(prop_PF * (1-prop_PF) / n), prop_PF + Z_025 * math.sqrt(prop_PF * (1-prop_PF) / n)]

# pi = p +- Z_025 * root(pq/n)
intervals["proportion POS"] = [prop_POS - Z_025 * math.sqrt(prop_POS * (1-prop_POS) / n), prop_POS + Z_025 * math.sqrt(prop_POS * (1-prop_POS) / n)]

# V = (n-1)s^2/chi(alpha/2), (n-1)s^2/chi(1 - alpha/2)
chi_025_left = chi2.ppf(0.025,482)
chi_025_right = chi2.ppf(0.975,482)
intervals["variance Age"] = [(n-1)*variance["Age"] / chi_025_right, (n-1)*variance["Age"] / chi_025_left]

print("Intervals:", intervals)

# c)
print("c)")
# group 1, age <= 26
# group 2, age > 26
# difference in means

mean1 = 0
n1 = 0
mean2 = 0
n2 = 0
for i in range(n):
    condition = data[i][cols["Age"]]
    item = data[i][cols["GS"]]
    if (condition <= 26):
        mean1 += item
        n1 += 1
    else:
        mean2 += item
        n2 += 1
mean1 /= n1
mean2 /= n2

s1 = 0
s2 = 0

for i in range(n):
    condition = data[i][cols["Age"]]
    item = data[i][cols["GS"]]
    if (condition <= 26):
        s1 += (item - mean1)**2
    else:
        s2 += (item - mean2)**2
s1 /= (n1-1)
s2 /= (n2-1)

# point
pointEstimator = mean1 - mean2
print("Point estimator for difference young and old, in terms of means games started:", pointEstimator)

# interval
# older starts more games
intervalDiff = [pointEstimator - Z_025 * math.sqrt(s1/n1 + s2/n2), pointEstimator + Z_025 * math.sqrt(s1/n1 + s2/n2)]
print("Interval for difference of young and old, in terms of mean games started:", intervalDiff)
print("since the range is negative, then older players start more games")

#--------------------

p1 = 0
n1 = 0
p2 = 0
n2 = 0
for i in range(n):
    condition = data[i][cols["Age"]]
    item = data[i][cols["PF"]]
    if (condition <= 26):
        if (item >= 2):
            p1 += 1
        n1 += 1
    else:
        if (item >= 2):
            p2 += 1
        n2 += 1
p1 /= n1
p2 /= n2

# point
pointEstimator = p1 - p2
print("Point estimator for difference young and old, in terms of proportion of aggressive players:", pointEstimator)

# interval
# older makes more fouls
P_bar = (n1*p1 + n2*p2)/(n1+n2)
intervalDiff = [pointEstimator - Z_025 * math.sqrt(P_bar*(1-P_bar)/n1 + P_bar*(1-P_bar)/n2), pointEstimator + Z_025 * math.sqrt(P_bar*(1-P_bar)/n1 + P_bar*(1-P_bar)/n2)]
print("Interval for difference of young and old, in terms of proportion of aggressive players:", intervalDiff)
print("since the range is negative, then older players tend to be more aggressive")


# d)
print("d)")

# claim 1, attacking players are more aggressive and so more fouls, but also more scored points
# PF>=2(1), PF<2(2) -> PTS1 > PTS2

# H0: PTS1 <= PTS2, PTS1 - PTS2 <= 0
# H1: PTS1 > PTS2, PTS1 - PTS2 > 0

pts1 = 0
n1 = 0
pts2 = 0
n2 = 0
for i in range(n):
    condition = data[i][cols["PF"]]
    item = data[i][cols["PTS"]]
    if (condition >= 2):
        pts1 += item
        n1 +=1
    else:
        pts2 += item
        n2 += 1
pts1 /= n1
pts2 /= n2

s1 = 0
s2 = 0

for i in range(n):
    condition = data[i][cols["PF"]]
    item = data[i][cols["PTS"]]
    if (condition >= 2):
        s1 += (item - pts1)**2
    else:
        s2 += (item - pts2)**2
s1 /= (n1-1)
s2 /= (n2-1)

Z_cal = ((pts1-pts2) - (0))/math.sqrt(s1/n1 + s2/n2)

Z_tabulated = 1.645

isReject = Z_cal >= Z_tabulated
print("Relating aggression to points per game: ", Z_cal, isReject)
print("Since Z_cal is in the Rejection Region, then we reject and thus more aggressive players score more points")

# claim 2
# H0: P(GS=0) >= 0.5
# H1: P(GS>0) < 0.5

pGS = 0
for i in range(n):
    if (data[i][cols["GS"]] > 0):
        pGS += 1
pGS /= n

Z_cal = (pGS - 0.5)/math.sqrt(0.5*0.5/n)

Z_tabulated = 1.645

isReject = Z_cal < Z_tabulated
print("Considering the proportion of players that start games: ", Z_cal, isReject)
print("Since Z_cal lies in RR, then we reject and so less than half the players always start the games")

# claim3
# g1 => C, g2 => not C
# H0: pf1 <= pf2
# H1: pf1 > pf2

pf1 = 0
n1 = 0
pf2 = 0
n2 = 0
for i in range(n):
    condition = data[i][cols["POS"]]
    item = data[i][cols["PF"]]
    if (condition == "C"):
        pf1 += item
        n1 +=1
    else:
        pf2 += item
        n2 += 1
pf1 /= n1
pf2 /= n2

s1 = 0
s2 = 0

for i in range(n):
    condition = data[i][cols["POS"]]
    item = data[i][cols["PF"]]
    if (condition == "C"):
        s1 += (item - pf1)**2
    else:
        s2 += (item - pf2)**2
s1 /= (n1-1)
s2 /= (n2-1)

Z_cal = ((pf1-pf2) - (0))/math.sqrt(s1/n1 + s2/n2)

Z_tabulated = 1.645

isReject = Z_cal >= Z_tabulated
print("Relating aggression and position:", Z_cal, isReject)
print("Since Z_cal is in the RR, then we reject and so Center players are more aggressive")