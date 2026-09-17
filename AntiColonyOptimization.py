# Ant Colony Optimization - Simple Path Selection

# R = Pheromone level
# E = Distance
# P = Path
R1 = int(input("Enter the R1  Value"))
R2 = int(input("Enter the R2 value"))

E1 = int(input("Enter the E1 value"))
E2 = int(input("Enter the E2 value"))

total = R1+R2

P1 = R1/total
P2 = R2/total

print("Path 1 probability (P1):",P1)
print("Path 2 Probability (P2):",P2)

print("\nPath 1 probability:",P1*100,"%")
print("\nPath 2 probability:",P2*100,"%")

if E1 < E2 :
    print("\nMinimum Distance Path: Path 1")
    print("Minimum Distance:",E1)

elif E2 < E1:
    print("\nMinimum Distance Path: Path 2")
    print("Minimum Distance:", E2)

else:
    print("\nBoth Paths have the same distance.")
    print("Path 1 Distance:", E1)
    print("Path 2 Distance:", E2)
    print("Minimum Distance:", E1)
