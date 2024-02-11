

def TowerOfHanoi(n,source,destination,intermediate):
    if n == 1:
        print("Move disc 1 from pole ",source,"to pole ",destination)
        return
    TowerOfHanoi(n-1,source,intermediate,destination)
    print("Move disc ",n,"from Pole ",source,"to pole ",destination)
    TowerOfHanoi(n-1,intermediate,destination,source)

n = 3
TowerOfHanoi(n,'A','C','B')