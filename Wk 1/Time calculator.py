import math


def tic():
    time=float(input("Enter time to be converted (in secs):"))
    hr=math.floor(time/(60*60))
    min=math.floor(time/60)-hr*60
    sec=time-min*60-hr*60*60
    print(hr,"hr,",min,"min,",sec,"sec")
while True:
    tic()
