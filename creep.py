import os
import random

time = random.randrange(600, 900)

print("운명의 점")
print("너의 컴퓨터는 잠들것이다.")

print("shutdown -r -t %s" % str(time))

os.system("shutdown -r -t %s" % str(time))