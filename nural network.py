def make_waits_aray():
    blank= [[]]
    waits = []
    layers = int(input("enter number of layers"))
    for x in range (layers):
        waits.extend(blank)
    print (waits)
    for x in range (layers):
        nurons = int(input("enter number of nurons in layer",x))
        waits[x].extend(blank)
    print(waits)
