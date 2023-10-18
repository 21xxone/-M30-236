import time
TribonacciNumber_Cache ={}
def TribonacciNumber(n):
 if n == 1 or n == 2:
  return 0
 if n == 3:
  return 1
 if n in TribonacciNumber_Cache:
  return TribonacciNumber_Cache[n]
 nTribonacciNumber = TribonacciNumber(n - 1) + TribonacciNumber(n - 2) + TribonacciNumber(n - 3)
 TribonacciNumber_Cache[n] = nTribonacciNumber
 return nTribonacciNumber
start = time.time()
print(TribonacciNumber(36))
end = time.time()
print(end - start)
print("")
TribonacciNumberCache = [0,0,1]
for i in range(3,100):
 TribonacciNumberCache.append(TribonacciNumberCache[i-1]+TribonacciNumberCache[i-2]+TribonacciNumberCache[i-3])
TribonacciNumbers = [73,10,4,15,20,7]
TribonacciNumbersValue = []
for number in TribonacciNumbers:
 TribonacciNumbersValue.append(TribonacciNumberCache[number - 1])
start1 = time.time()
print(TribonacciNumbersValue)
end1 = time.time()
print(end1 - start1)
