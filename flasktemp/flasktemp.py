from flask import Flask
import random
import numpy
import time

app = Flask(__name__)


@app.route('/')
def main():

 global x,n
 n = 0
 x = random.uniform(17, 25)
 y=random.randint(1,10)
 while True:
   if y<=3:
     while n <= 3:
          time.sleep(1.5)
          n+=1
     while x <= 19:
          time.sleep(1.5)
          return("Current temperature is &.1f" % (x))
          time.sleep(1.5)
          x += 1.543
     while x>19 and n>0:
          time.sleep(1.5)
          return("Current temperature is &.1f" % (x))
          x += 0.874
          time.sleep(1.5)
          n-=2
          while n==0:
                time.sleep(1.5)
                return("Current temperature is &.1f" % (x))
                time.sleep(1.5)

   if y>3:
     time.sleep(1.5)
     return('Current temperature: %.1f' %(x))
     time.sleep(1.5)

if __name__ == "__main__":
 app.run('host=0.0.0.0', use_reloader=False)
