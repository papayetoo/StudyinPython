numOfCities = input()
MAX = 17
buffer = list( list( 0 for i in range(1 << 16)) for i in range(MAX))
cost = list(list(map(int, input().split())) for i in range(int(numOfCities)))
