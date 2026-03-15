import time

def show_solution(goal):

    path=[]

    while goal:
        path.append(goal)
        goal=goal.parent

    path.reverse()

    for s in path:

        A=[]
        B=[]
        C=[]

        for i,p in enumerate(s.pegs,start=1):

            if p=='A':
                A.append(i)
            elif p=='B':
                B.append(i)
            else:
                C.append(i)

        print("A:",A)
        print("B:",B)
        print("C:",C)
        print("-----")

        time.sleep(0.5)