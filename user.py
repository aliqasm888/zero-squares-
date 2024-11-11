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

        ay=[squer("black"),squer("black"),squer("black"),squer("black"),squer("black"),squer("black"),squer("red"),squer("whait"),squer("red_red"),squer("black"),squer("black"),squer("black"),squer("black"),squer("black"),squer("black")]
        v=0
        for c in range(i):
            row=[]
            for f in range(j):
                row.append(ay1[v])
                v+=1
            a.append(row)
        a1=graph(a,11,7)
        a1.print_graph() 
        nextstate=graph(a,11,7)
        arraycopy=copy.deepcopy(a1.a)
        for g in range(50):    
            value=input("enter w or s or d or a")
            if(value=="d"):
                
                nextstate=a1.move_to_right(nextstate)
                nextstate.print_graph()
                if(a1.winner(a,i,j)):
                    print("========================================== winner ==========================================")   
                    break 
            

            if(value=="a"):
                nextstate=a1.move_to_left(nextstate)
                nextstate.print_graph()
                if(a1.winner(a,i,j)):
                    print("========================================== winner ==========================================")   
                    break 
               
            if(value=="w"):
                nextstate=a1.move_to_up(nextstate)
                nextstate.print_graph()
                if(a1.winner(a,i,j)):
                    print("========================================== winner ==========================================")   
                    break 
               


            if(value=="s"):
                nextstate=a1.move_to_down(nextstate)
                nextstate.print_graph()
                if(a1.winner(a,i,j)):
                    print("========================================== winner ==========================================")   
                    break                
             
            
            if(value=="q"):
                print("right")
                arraycopy=copy.deepcopy(a)
                if(a1.chick_if_right()):    
                    for c in range(i):
                        for d in range(j-2,-1,-1):
                            if (a[c][d].color!="black" and a[c][d].color!="whait" and a1.chick_if_goal(a[c][d].color)==False and a1.chick_right(arraycopy,c,d)==True ):
                                for h in range(d,j-1):
                                    if(a1.chick_if_two__(a[c][h].color)):
                                        if(a1.chick_right(a,c,h)):
                                            if( a1.chick_if_goal(a[c][h+1].color)==False):
                                                a[c][h+1].color=a1.separted(a[c][h].color)
                                                a[c][h].color=a1.separted_two(a[c][h].color)
                                            elif (a1.chick_if_goal_correct(a1.separted(a[c][h].color),a[c][h+1].color)):
                                                a[c][h+1].color="whait"
                                                a[c][h].color=a1.separted_two(a[c][h].color)

                                            else:
                                                a[c][h+1].color=a[c][h+1].color+"_"+a1.separted(a[c][h].color)
                                                a[c][h].color=a1.separted_two(a[c][h].color)
                                    if(a1.chick_right(a,c,h) and not a1.chick_if_two__(a[c][h].color)):
                                        if( a1.chick_if_goal(a[c][h+1].color)==False):    
                                            a[c][h+1].color=a[c][h].color
                                            a[c][h].color="whait"
                                        elif (a1.chick_if_goal_correct(a[c][h].color,a[c][h+1].color)):
                                            a[c][h].color="whait"
                                            a[c][h+1].color="whait"
                                        else:
                                            a[c][h+1].color=a[c][h+1].color+"_"+a[c][h].color
                                            a[c][h].color="whait"
                a1=graph(a,i,j)
                a1.print_graph()
                print("left")
                arraycopy=copy.deepcopy(a)
                if(a1.chick_if_left()):
                                        
                    for c in range(i):
                        for d in range(1,j):
                            if (a[c][d].color!="black" and a[c][d].color!="whait" and a1.chick_if_goal(a[c][d].color)==False and a1.chick_left(arraycopy,c,d)==True ):
                                for h in range(d,0,-1):
                                    if(a1.chick_if_two__(a[c][h].color)):
                                        if(a1.chick_left(a,c,h)):
                                            if( a1.chick_if_goal(a[c][h-1].color)==False):
                                                a[c][h-1].color=a1.separted(a[c][h].color)
                                                a[c][h].color=a1.separted_two(a[c][h].color)
                                            elif (a1.chick_if_goal_correct(a1.separted(a[c][h].color),a[c][h-1].color)):
                                                a[c][h-1].color="whait"
                                                a[c][h].color=a1.separted_two(a[c][h].color)                                                
                                            else:
                                                a[c][h-1].color=a[c][h-1].color+"_"+a1.separted(a[c][h].color)
                                                a[c][h].color=a1.separted_two(a[c][h].color)
                                    if(a1.chick_left(a,c,h) and not a1.chick_if_two__(a[c][h].color)):
                                        if( a1.chick_if_goal(a[c][h-1].color)==False):    
                                            a[c][h-1].color=a[c][h].color
                                            a[c][h].color="whait"
                                        elif (a1.chick_if_goal_correct(a[c][h].color,a[c][h-1].color)):
                                            a[c][h].color="whait"
                                            a[c][h-1].color="whait"
                                        else:
                                            a[c][h-1].color=a[c][h-1].color+"_"+a[c][h].color
                                            a[c][h].color="whait"              
                a1=graph(a,i,j)
                a1.print_graph()
                
                                            
                print("up")
                arraycopy=copy.deepcopy(a)
                if(a1.chick_if_up()):
                    
                    for c in range(1,i):
                        for d in range(j):
                            if (a[c][d].color!="black" and a[c][d].color!="whait" and a1.chick_if_goal(a[c][d].color)==False and a1.chick_up(arraycopy,c,d)==True ):
                                for h in range(c,0,-1):
                                    if(a1.chick_if_two__(a[h][d].color)):
                                        if(a1.chick_up(a,h,d)):
                                            if( a1.chick_if_goal(a[h-1][d].color)==False):
                                                a[h-1][d].color=a1.separted(a[h][d].color)
                                                a[h][d].color=a1.separted_two(a[h][d].color)
                                            elif (a1.chick_if_goal_correct(a1.separted(a[h][d].color),a[h-1][d].color)):
                                                a[h-1][d].color="whait"
                                                a[h][d].color=a1.separted_two(a[h][d].color)                                                
                                            else:
                                                a[h-1][d].color=a[h-1][d].color+"_"+a1.separted(a[h][d].color)
                                                a[h][d].color=a1.separted_two(a[h][d].color)
                                    if(a1.chick_up(a,h,d) and not a1.chick_if_two__(a[h][d].color)):
                                        if( a1.chick_if_goal(a[h-1][d].color)==False):    
                                            a[h-1][d].color=a[h][d].color
                                            a[h][d].color="whait"
                                        elif (a1.chick_if_goal_correct(a[h][d].color,a[h-1][d].color)):
                                            a[h][d].color="whait"
                                            a[h-1][d].color="whait"
                                        else:
                                            a[h-1][d].color=a[h-1][d].color+"_"+a[h][d].color
                                            a[h][d].color="whait"
                a1=graph(a,i,j)
                a1.print_graph()
                print("down")
                arraycopy=copy.deepcopy(a)
                if(a1.chick_if_down()):
                    
                    for c in range(i-2,-1,-1):
                        for d in range(j):
                            if (a[c][d].color!="black" and a[c][d].color!="whait" and a1.chick_if_goal(a[c][d].color)==False and a1.chick_dwon(arraycopy,c,d)==True ):
                                for h in range(c,i-1):
                                    if(a1.chick_if_two__(a[h][d].color)):
                                        if(a1.chick_dwon(a,h,d)):
                                            if( a1.chick_if_goal(a[h+1][d].color)==False):
                                                a[h+1][d].color=a1.separted(a[h][d].color)
                                                a[h][d].color=a1.separted_two(a[h][d].color)
                                            elif (a1.chick_if_goal_correct(a1.separted(a[h][d].color),a[h+1][d].color)):
                                                a[h+1][d].color="whait"
                                                a[h][d].color=a1.separted_two(a[h][d].color)                                                
                                            else:
                                                a[h+1][d].color=a[h+1][d].color+"_"+a1.separted(a[h][d].color)
                                                a[h][d].color=a1.separted_two(a[h][d].color)
                                    if(a1.chick_dwon(a,h,d) and not a1.chick_if_two__(a[h][d].color)):
                                        if( a1.chick_if_goal(a[h+1][d].color)==False):    
                                            a[h+1][d].color=a[h][d].color
                                            a[h][d].color="whait"
                                        elif (a1.chick_if_goal_correct(a[h][d].color,a[h+1][d].color)):
                                            a[h][d].color="whait"
                                            a[h+1][d].color="whait"
                                        else:
                                            a[h+1][d].color=a[h+1][d].color+"_"+a[h][d].color
                                            a[h][d].color="whait"
                a1=graph(a,i,j)
                a1.print_graph()



          

            
