import statistics
from statistics import mode
median = 0.0
mode = 0.0
mean = 0.0
tSum = 0.0
i = 0
def main(list):
    if len(list) !=0:
        median = statistics.median(list)
        mode = max(set(list),key=list.count)
        mean = sum(list)/len(list)
    else:
        median = 0.0
        mode = 0.0
        mean = 0.0
    print("Median:",str(median))
    print("Mode:",str(mode))
    print("Mean:",str(mean))
