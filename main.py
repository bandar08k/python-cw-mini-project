# write your code here
def padel_court_cost(court_type):
     if court_type =="indoor":
          return 30
     elif court_type =="outdoor":
          return 20

def rackets_cost(racket_brand):
     if racket_brand =="Nox":
          return 140
     elif racket_brand == "Siux":
          return 200

def padel_balls_cost(ball_boxes):
     if  ball_boxes =="one box":
          return 2
     elif ball_boxes =="two boxes":
          return 3.5
     elif ball_boxes == "three boxes":
          return 5

def padel_game_cost():
     court_type = input("indoor / outdoor: ")
     racket_brand = input("Nox / Siux: ")
     ball_boxes = input("one / two / three boxes") 
     total = padel_court_cost(court_type) + rackets_cost(racket_brand) + padel_balls_cost(ball_boxes)
     return total
print(f"{padel_game_cost()}")