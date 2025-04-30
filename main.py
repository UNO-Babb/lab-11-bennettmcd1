#GroceryStoreSim.py
#Name: Bennett McDonald
#Date: 4/30/25
#Assignment: grocery sim
import random
import time

eventLog = []
waitingShoppers = []
idleTime = 0

def shopper(id):
    arrive = time.time()
    items = random.randint(5, 20)
    shoppingTime = items // 2
    time.sleep(shoppingTime)
    done_shopping = time.time()
    waitingShoppers.append((id, items, arrive, done_shopping))

def checker():
    global idleTime
    while True:
        while len(waitingShoppers) == 0:
            idleTime += 1
            time.sleep(1)

        customer = waitingShoppers.pop(0)
        items = customer[1]
        checkoutTime = items // 10 + 1
        time.sleep(checkoutTime)

        eventLog.append((customer[0], customer[1], customer[2], customer[3], time.time()))

def customerArrival():
    customerNumber = 0
    while True:
        customerNumber += 1
        shopper(customerNumber)
        time.sleep(2)

def processResults():
    totalWait = 0
    totalShoppers = 0

    for e in eventLog:
        waitTime = e[4] - e[3]
        totalWait += waitTime
        totalShoppers += 1

    avgWait = totalWait / totalShoppers if totalShoppers > 0 else 0

    print("The average wait time was %.2f minutes." % avgWait)
    print("The total idle time was %d minutes" % idleTime)

def main():
    numberCheckers = 5
    start_time = time.time()

    for i in range(numberCheckers):
        checker()

    customerArrival()

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Total time elapsed: {total_time} seconds")
    print(f"Total number of shoppers who completed shopping: {len(waitingShoppers)}")
    processResults()

if __name__ == '__main__':
    main()

