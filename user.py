from squer import squer
from graph import graph
import copy
class user:  
    def initial(self):
        
        # i=3
        # j=5
        i=11
        j=7
        a=[]
        ay1=[squer("black"),squer("black"),squer("black"),squer("black"),squer("black"),squer("black"),squer("black"),
            squer("black"),squer("whait"),squer("whait"),squer("whait"),squer("whait"),squer("blue_blue"),squer("black"),
            squer("black"),squer("whait"),squer("whait"),squer("blue"),squer("black"),squer("whait"),squer("black"),
            squer("black"),squer("red"),squer("black"),squer("whait"),squer("black"),squer("whait"),squer("black"),
            squer("black"),squer("whait"),squer("whait"),squer("red_red"),squer("black"),squer("whait"),squer("black"),
            squer("black"),squer("whait"),squer("whait"),squer("black"),squer("black"),squer("whait"),squer("black"),
            squer("black"),squer("whait"),squer("whait"),squer("whait"),squer("whait"),squer("whait"),squer("black"),
            squer("black"),squer("whait"),squer("whait"),squer("whait"),squer("whait"),squer("black"),squer("black"),
            squer("black"),squer("black"),squer("black"),squer("black"),squer("whait"),squer("whait"),squer("black"),
            squer("whait"),squer("black"),squer("whait"),squer("whait"),squer("whait"),squer("whait"),squer("black"),
            squer("whait"),squer("black"),squer("black"),squer("black"),squer("black"),squer("black"),squer("black"),]

        ay=[squer("black"),squer("black"),squer("red"),squer("black"),squer("black"),
            squer("black"),squer("whait"),squer("whait"),squer("red_red"),squer("black"),
            squer("black"),squer("black"),squer("black"),squer("black"),squer("black")]
        v=0
        for c in range(i):
            row=[]
            for f in range(j):
                row.append(ay1[v])
                v+=1
            a.append(row)
        a1=graph(a,i,j)        
        ali=[]
        # a1.print_graph() 
        nextstate=graph(a,i,j)
        arraycopy=copy.deepcopy(a1.a)
        visited=set()
        solution = a1.dfss(a1,visited)
        if solution:
            print("Solution found!")
            for step, board in enumerate(solution):
                print(f"number {step}:\n{board.print_graph()}")
        else:
            print("No solution exists.")
        # for c in range(i):
        #     for f in range(j):
        #         print((a1.nextstate(a1))[3].a[c][f].color,end=" ")
        #     print("")
        # print()

        for g in range(50):

            value=input("enter w or s or d or a")
            if(value=="d"):
                
                nextstate=a1.move_to_right(nextstate)
                nextstate.print_graph()
                if(nextstate.winner(nextstate.a,i,j)):
                    print("========================================== winner ==========================================")   
                    break 
            

            if(value=="a"):
                nextstate=a1.move_to_left(nextstate)
                nextstate.print_graph()
                if(nextstate.winner(nextstate.a,i,j)):
                    print("========================================== winner ==========================================")   
                    break 
               
            if(value=="w"):
                nextstate=a1.move_to_up(nextstate)
                nextstate.print_graph()
                if(a1.winner(nextstate.a,i,j)):
                    print("========================================== winner ==========================================")   
                    break 
               


            if(value=="s"):
                nextstate=a1.move_to_down(nextstate)
                nextstate.print_graph()
                if(nextstate.winner(nextstate.a,i,j)):
                    print("========================================== winner ==========================================")   
                    break                
             
            
            