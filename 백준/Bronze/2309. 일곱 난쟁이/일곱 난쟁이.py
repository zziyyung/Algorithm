import sys

heights = list(int(sys.stdin.readline().strip()) for _ in range(9))

for i in range(len(heights)):
    for j in range(i+1, len(heights)):
        if sum(heights) - (heights[i] + heights[j]) == 100:
            x,y = heights[i], heights[j]
        break
        
heights.remove(x)
heights.remove(y)

print('\n'.join(map(str,sorted(heights))))
