from squer import squer
import copy
# import numpy
# import matplotlib
# import tensorflow
class graph:

    def __init__(self,a,i,j):
       self.a=a
       self.i=i
       self.j=j
    #    self.a=[]
    
    def print_graph(self):
        for c in range(self.i):
            for f in range(self.j):
                print(self.a[c][f].color,end=" ")
            print("")

    # def init_array(self):
    #     v=0
    #     for c in range(self.i):
    #         row=[]
    #         for f in range(self.j):
    #             row.append(self.array[v].color)
    #             v+=1
    #         self.a.append(row)

    def chick_if_right(self):
        for c in range(self.i):
            for f in range(self.j):
                if (self.a[c][f].color!="black" and self.a[c][f].color!="whait" and self.j!=f+1 and self.chick_if_goal(self.a[c][f].color)==False):
                    if ( self.a[c][f+1].color=="whait" or self.chick_if_goal(self.a[c][f+1].color)):
                        return True
        return False
    
    def chick_if_left(self):
        for c in range(self.i):
            for f in range(self.j):
                if (self.a[c][f].color!="black" and self.a[c][f].color!="whait" and f!=0 and self.chick_if_goal(self.a[c][f].color)==False):
                    if ( self.a[c][f-1].color=="whait" or self.chick_if_goal(self.a[c][f-1].color)):
                        return True
        return False
                
    def chick_if_up(self):
        for c in range(self.i):
            for f in range(self.j):
                if (self.a[c][f].color!="black" and self.a[c][f].color!="whait"and c!=0 and self.chick_if_goal(self.a[c][f].color)==False):
                    if ( self.a[c-1][f].color=="whait"or self.chick_if_goal(self.a[c-1][f].color)):
                        return True
        return False
                               
    def chick_if_down(self):
        for c in range(self.i):
            for f in range(self.j):
                if (self.a[c][f].color!="black" and self.a[c][f].color!="whait"and self.i!=c+1 and self.chick_if_goal(self.a[c][f].color)==False):
                    if ( self.a[c+1][f].color=="whait"or self.chick_if_goal(self.a[c+1][f].color)):
                        return True
        return False

                    
                       
    def  chick_right(self,a,i,j):
            if ( a[i][j+1].color=="whait" or self.chick_if_goal(a[i][j+1].color) ):
                return True
            return False 
    def  chick_left(self,a,i,j):
            if ( a[i][j-1].color=="whait" or self.chick_if_goal(a[i][j-1].color) ):
                return True
            return False    

    def  chick_up(self,a,i,j):
            if ( a[i-1][j].color=="whait" or self.chick_if_goal(a[i-1][j].color) ):
                return True
            return False
    def  chick_dwon(self,a,i,j):
            if ( a[i+1][j].color=="whait" or self.chick_if_goal(a[i+1][j].color) ):
                return True
            return False
    def  chick_if_goal(self,a):
        v=0
        for c in range(len(a)):
            if ( a[c]=='_' ):
                v+=1
        if(v==1):
            return True  
        return False        

    def  chick_if_goal_correct(self,a,b):
        v=0
        # print(a,b)

        for c in range(len(a)):
            if ( a[c]==b[c] ):
                v+=1
        if(v== len(a)):
            return True  
        return False 
           
    def  separted(self,a):
        v=0
        str=""
        for c in range(len(a)):   
            if ( a[c]=='_' and v==1  ):
                for f in range(c+1,len(a)):
                    str+=a[f] 
            if ( a[c]=='_' and v!=1 ):
                v+=1
        return str
    
    def  separted_two(self,a):
        v=0
        str=""
        for c in range(len(a)):
               
            if ( a[c]=='_' and v==1  ):
                return str
                    
            if ( a[c]=='_' and v!=1 ):
                v+=1
            str+=a[c]    

    
    def  chick_if_two__(self,a):
        v=0
        for c in range(len(a)):                  
            if ( a[c]=='_'  ):
                v+=1
        if(v>=2):
             return True
        return False
    
    def  winner(self,a,i,j):

        v=0
        for c in range(i):
            for f in range(j):             
                if(a[c][f].color!="whait" and a[c][f].color!="black"):
                    return False
        return True
    def equals(self,obj1,obj2):
        for c in range(obj1.i):
            for d in range(obj1.j):
                if(obj1.a[c][d].color!=obj2.a[c][d].color):
                    return False
        return True        


    def move_to_right(self,obj):
        change=copy.deepcopy(obj)
        arraycopy=copy.deepcopy(obj.a)
        if(change.chick_if_right()):
            for c in range(change.i):
                for d in range(change.j-2,-1,-1):
                    if (change.a[c][d].color!="black" and change.a[c][d].color!="whait" and change.chick_if_goal(change.a[c][d].color)==False and change.chick_right(arraycopy,c,d)==True ):
                        for h in range(d,change.j-1):
                            if(change.chick_if_two__(change.a[c][h].color)):
                                if(change.chick_right(change.a,c,h)):
                                    if( change.chick_if_goal(change.a[c][h+1].color)==False):
                                        change.a[c][h+1].color=change.separted(change.a[c][h].color)
                                        change.a[c][h].color=change.separted_two(change.a[c][h].color)
                                    elif (change.chick_if_goal_correct(change.separted(change.a[c][h].color),change.a[c][h+1].color)):
                                        change.a[c][h+1].color="whait"
                                        change.a[c][h].color=change.separted_two(change.a[c][h].color)
                                    else:
                                        change.a[c][h+1].color=change.a[c][h+1].color+"_"+change.separted(change.a[c][h].color)
                                        change.a[c][h].color=change.separted_two(change.a[c][h].color)
                            if(change.chick_right(change.a,c,h) and not change.chick_if_two__(change.a[c][h].color)and change.a[c][h].color!="black" and change.a[c][h].color!="whait"):
                                if( change.chick_if_goal(change.a[c][h+1].color)==False):    
                                    change.a[c][h+1].color=change.a[c][h].color
                                    change.a[c][h].color="whait"
                                elif (change.chick_if_goal_correct(change.a[c][h].color,change.a[c][h+1].color)):
                                    change.a[c][h].color="whait"
                                    change.a[c][h+1].color="whait"
                                else:
                                    change.a[c][h+1].color=change.a[c][h+1].color+"_"+change.a[c][h].color
                                    change.a[c][h].color="whait"                            
        return graph(change.a,change.i,change.j) 
         
    def move_to_up(self,obj):
        change=copy.deepcopy(obj)
        arraycopy=copy.deepcopy(change.a)
        if(change.chick_if_up()):
            for c in range(1,change.i):
                for d in range(change.j):
                    if (change.a[c][d].color!="black" and change.a[c][d].color!="whait" and change.chick_if_goal(change.a[c][d].color)==False and change.chick_up(arraycopy,c,d)==True ):
                        for h in range(c,0,-1):
                            if(change.chick_if_two__(change.a[h][d].color)):
                                if(change.chick_up(change.a,h,d)):
                                    if( change.chick_if_goal(change.a[h-1][d].color)==False):
                                        change.a[h-1][d].color=change.separted(change.a[h][d].color)
                                        change.a[h][d].color=change.separted_two(change.a[h][d].color)
                                    elif (change.chick_if_goal_correct(change.separted(change.a[h][d].color),change.a[h-1][d].color)):
                                        change.a[h-1][d].color="whait"
                                        change.a[h][d].color=change.separted_two(change.a[h][d].color)                                                
                                    else:
                                        change.a[h-1][d].color=change.a[h-1][d].color+"_"+change.separted(change.a[h][d].color)
                                        change.a[h][d].color=change.separted_two(change.a[h][d].color)
                            if(change.chick_up(change.a,h,d) and not change.chick_if_two__(change.a[h][d].color)and change.a[h][d].color!="black" and change.a[h][d].color!="whait"):
                                if( change.chick_if_goal(change.a[h-1][d].color)==False):    
                                    change.a[h-1][d].color=change.a[h][d].color
                                    change.a[h][d].color="whait"
                                elif (change.chick_if_goal_correct(change.a[h][d].color,change.a[h-1][d].color)):
                                    change.a[h][d].color="whait"
                                    change.a[h-1][d].color="whait"
                                else:
                                    change.a[h-1][d].color=change.a[h-1][d].color+"_"+change.a[h][d].color
                                    change.a[h][d].color="whait"
        return graph(change.a,change.i,change.j) 
                        

    def move_to_left(self,obj):
        change=copy.deepcopy(obj)
        arraycopy=copy.deepcopy(change.a)
        if(change.chick_if_left()):
            for c in range(change.i):
                for d in range(1,change.j):
                    if (change.a[c][d].color!="black" and change.a[c][d].color!="whait" and change.chick_if_goal(change.a[c][d].color)==False and change.chick_left(arraycopy,c,d)==True ):
                        for h in range(d,0,-1):
                            if(change.chick_if_two__(change.a[c][h].color) ):
                                if(change.chick_left(change.a,c,h)):
                                    if( change.chick_if_goal(change.a[c][h-1].color)==False):
                                        change.a[c][h-1].color=change.separted(change.a[c][h].color)
                                        change.a[c][h].color=change.separted_two(change.a[c][h].color)
                                    elif (change.chick_if_goal_correct(change.separted(change.a[c][h].color),change.a[c][h-1].color)):
                                        change.a[c][h-1].color="whait"
                                        change.a[c][h].color=change.separted_two(change.a[c][h].color)                                                
                                    else:
                                        change.a[c][h-1].color=change.a[c][h-1].color+"_"+change.separted(change.a[c][h].color)
                                        change.a[c][h].color=change.separted_two(change.a[c][h].color)
                            if(change.chick_left(change.a,c,h) and not change.chick_if_two__(change.a[c][h].color)and change.a[c][h].color!="black"and change.a[c][h].color!="whait" ):
                                if( change.chick_if_goal(change.a[c][h-1].color)==False):    
                                    change.a[c][h-1].color=change.a[c][h].color
                                    change.a[c][h].color="whait"
                                elif (change.chick_if_goal_correct(change.a[c][h].color,change.a[c][h-1].color)):
                                    change.a[c][h].color="whait"
                                    change.a[c][h-1].color="whait"
                                else:
                                    change.a[c][h-1].color=change.a[c][h-1].color+"_"+change.a[c][h].color
                                    change.a[c][h].color="whait"      
        return graph(change.a,change.i,change.j) 

    def move_to_down(self,obj):
        change=copy.deepcopy(obj)
        arraycopy=copy.deepcopy(change.a)
        if(change.chick_if_down()):
            for c in range(change.i-2,-1,-1):
                for d in range(change.j):
                    if (change.a[c][d].color!="black" and change.a[c][d].color!="whait" and change.chick_if_goal(change.a[c][d].color)==False and change.chick_dwon(arraycopy,c,d)==True ):
                        for h in range(c,change.i-1):
                            if(change.chick_if_two__(change.a[h][d].color)):
                                if(change.chick_dwon(change.a,h,d)):
                                    if( change.chick_if_goal(change.a[h+1][d].color)==False):
                                        change.a[h+1][d].color=change.separted(change.a[h][d].color)
                                        change.a[h][d].color=change.separted_two(change.a[h][d].color)
                                    elif (change.chick_if_goal_correct(change.separted(change.a[h][d].color),change.a[h+1][d].color)):
                                        change.a[h+1][d].color="whait"
                                        change.a[h][d].color=change.separted_two(change.a[h][d].color)                                                
                                    else:
                                        change.a[h+1][d].color=change.a[h+1][d].color+"_"+change.separted(change.a[h][d].color)
                                        change.a[h][d].color=change.separted_two(change.a[h][d].color)
                            if(change.chick_dwon(change.a,h,d) and not change.chick_if_two__(change.a[h][d].color) and change.a[h][d].color!="black" and change.a[h][d].color!="whait"):
                                if( change.chick_if_goal(change.a[h+1][d].color)==False):    
                                    change.a[h+1][d].color=change.a[h][d].color
                                    change.a[h][d].color="whait"
                                elif (change.chick_if_goal_correct(change.a[h][d].color,change.a[h+1][d].color)):
                                    change.a[h][d].color="whait"
                                    change.a[h+1][d].color="whait"
                                else:
                                    change.a[h+1][d].color=change.a[h+1][d].color+"_"+change.a[h][d].color
                                    change.a[h][d].color="whait"
        return graph(change.a,change.i,change.j) 
    
    def nextstate(self,obj):
        list=[]
        if obj.chick_if_right():
            right=self.move_to_right(obj)
            list.append(right)
        if obj.chick_if_left():
            left=self.move_to_left(obj)
            list.append(left)
        if obj.chick_if_up():
            up=self.move_to_up(obj)
            list.append(up)
        if obj.chick_if_down():
            down=self.move_to_down(obj)
            list.append(down)
        return list
    
    def dfs(self,start_board):
        o=0
        v=0
        stack = [(start_board, [])]  
    
        visited = set()  
    
        while stack:
            v=0
            current, path = stack.pop() 
            if current.winner(current.a,current.i,current.j):

                return path + [current]
        
            for t in visited:
                if self.equals(current,t):
                    v+=1
            if v>=1 :
                continue       
            current.print_graph()
            o+=1
            print(f"Visited nodes: {o}")
            visited.add(current)
          
            for next_state in self.nextstate(current):
                stack.append((next_state, path + [current]))   
        return None

    def bfs(self, start_board):
        o = 0  
        queue = [(start_board, [])]  
        visited = set()  

        while queue:
            current, path = queue.pop(0)  
        
            if current.winner(current.a, current.i, current.j):
                print("Goal reached")
                return path + [current]  

            if any(self.equals(current, t) for t in visited):
                continue

            current.print_graph()
            o += 1
            print(f"Visited nodes: {o}")

            visited.add(current)

            for next_state in self.nextstate(current):
                queue.append((next_state, path + [current]))

        return None  
