from squer import squer
import copy

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
                if (self.a[c][f].color!="black" and self.a[c][f].color!="whait" and self.j!=f+1 ):
                    if ( self.a[c][f+1].color=="whait" or self.chick_if_goal(self.a[c][f+1].color)):
                        return True
        return False
    
    def chick_if_left(self):
        for c in range(self.i):
            for f in range(self.j):
                if (self.a[c][f].color!="black" and self.a[c][f].color!="whait" and f!=0):
                    if ( self.a[c][f-1].color=="whait"):
                        return True
        return False
                
    def chick_if_up(self):
        for c in range(self.i):
            for f in range(self.j):
                if (self.a[c][f].color!="black" and self.a[c][f].color!="whait"and c!=0):
                    if ( self.a[c-1][f].color=="whait"):
                        return True
        return False
                               
    def chick_if_down(self):
        for c in range(self.i):
            for f in range(self.j):
                if (self.a[c][f].color!="black" and self.a[c][f].color!="whait"and self.i!=c+1):
                    if ( self.a[c+1][f].color=="whait"):
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
                if(obj1.a[c][d]!=obj2.a[c][d]):
                    return False        


    def move_to_right(self,obj):
        arraycopy=copy.deepcopy(obj.a)
        if(obj.chick_if_right()):
            for c in range(obj.i):
                for d in range(obj.j-2,-1,-1):
                    if (obj.a[c][d].color!="black" and obj.a[c][d].color!="whait" and obj.chick_if_goal(obj.a[c][d].color)==False and obj.chick_right(arraycopy,c,d)==True ):
                        for h in range(d,obj.j-1):
                            if(obj.chick_if_two__(obj.a[c][h].color)):
                                if(obj.chick_right(obj.a,c,h)):
                                    if( obj.chick_if_goal(obj.a[c][h+1].color)==False):
                                        obj.a[c][h+1].color=obj.separted(obj.a[c][h].color)
                                        obj.a[c][h].color=obj.separted_two(obj.a[c][h].color)
                                    elif (obj.chick_if_goal_correct(obj.separted(obj.a[c][h].color),obj.a[c][h+1].color)):
                                        obj.a[c][h+1].color="whait"
                                        obj.a[c][h].color=obj.separted_two(obj.a[c][h].color)
                                    else:
                                        obj.a[c][h+1].color=obj.a[c][h+1].color+"_"+obj.separted(obj.a[c][h].color)
                                        obj.a[c][h].color=obj.separted_two(obj.a[c][h].color)
                            if(obj.chick_right(obj.a,c,h) and not obj.chick_if_two__(obj.a[c][h].color)):
                                if( obj.chick_if_goal(obj.a[c][h+1].color)==False):    
                                    obj.a[c][h+1].color=obj.a[c][h].color
                                    obj.a[c][h].color="whait"
                                elif (obj.chick_if_goal_correct(obj.a[c][h].color,obj.a[c][h+1].color)):
                                    obj.a[c][h].color="whait"
                                    obj.a[c][h+1].color="whait"
                                else:
                                    obj.a[c][h+1].color=obj.a[c][h+1].color+"_"+obj.a[c][h].color
                                    obj.a[c][h].color="whait"                            
        return graph(obj.a,obj.i,obj.j) 
         
    def move_to_up(self,obj):
        arraycopy=copy.deepcopy(obj.a)
        if(obj.chick_if_up()):
            for c in range(1,obj.i):
                for d in range(obj.j):
                    if (obj.a[c][d].color!="black" and obj.a[c][d].color!="whait" and obj.chick_if_goal(obj.a[c][d].color)==False and obj.chick_up(arraycopy,c,d)==True ):
                        for h in range(c,0,-1):
                            if(obj.chick_if_two__(obj.a[h][d].color)):
                                if(obj.chick_up(obj.a,h,d)):
                                    if( obj.chick_if_goal(obj.a[h-1][d].color)==False):
                                        obj.a[h-1][d].color=obj.separted(obj.a[h][d].color)
                                        obj.a[h][d].color=obj.separted_two(obj.a[h][d].color)
                                    elif (obj.chick_if_goal_correct(obj.separted(obj.a[h][d].color),obj.a[h-1][d].color)):
                                        obj.a[h-1][d].color="whait"
                                        obj.a[h][d].color=obj.separted_two(obj.a[h][d].color)                                                
                                    else:
                                        obj.a[h-1][d].color=obj.a[h-1][d].color+"_"+obj.separted(obj.a[h][d].color)
                                        obj.a[h][d].color=obj.separted_two(obj.a[h][d].color)
                            if(obj.chick_up(obj.a,h,d) and not obj.chick_if_two__(obj.a[h][d].color)):
                                if( obj.chick_if_goal(obj.a[h-1][d].color)==False):    
                                    obj.a[h-1][d].color=obj.a[h][d].color
                                    obj.a[h][d].color="whait"
                                elif (obj.chick_if_goal_correct(obj.a[h][d].color,obj.a[h-1][d].color)):
                                    obj.a[h][d].color="whait"
                                    obj.a[h-1][d].color="whait"
                                else:
                                    obj.a[h-1][d].color=obj.a[h-1][d].color+"_"+obj.a[h][d].color
                                    obj.a[h][d].color="whait"
        return graph(obj.a,obj.i,obj.j) 
                        

    def move_to_left(self,obj):
        arraycopy=copy.deepcopy(obj.a)
        if(obj.chick_if_left()):
            for c in range(obj.i):
                for d in range(1,obj.j):
                    if (obj.a[c][d].color!="black" and obj.a[c][d].color!="whait" and obj.chick_if_goal(obj.a[c][d].color)==False and obj.chick_left(arraycopy,c,d)==True ):
                        for h in range(d,0,-1):
                            if(obj.chick_if_two__(obj.a[c][h].color)):
                                if(obj.chick_left(obj.a,c,h)):
                                    if( obj.chick_if_goal(obj.a[c][h-1].color)==False):
                                        obj.a[c][h-1].color=obj.separted(obj.a[c][h].color)
                                        obj.a[c][h].color=obj.separted_two(obj.a[c][h].color)
                                    elif (obj.chick_if_goal_correct(obj.separted(obj.a[c][h].color),obj.a[c][h-1].color)):
                                        obj.a[c][h-1].color="whait"
                                        obj.a[c][h].color=obj.separted_two(obj.a[c][h].color)                                                
                                    else:
                                        obj.a[c][h-1].color=obj.a[c][h-1].color+"_"+obj.separted(obj.a[c][h].color)
                                        obj.a[c][h].color=obj.separted_two(obj.a[c][h].color)
                            if(obj.chick_left(obj.a,c,h) and not obj.chick_if_two__(obj.a[c][h].color)):
                                if( obj.chick_if_goal(obj.a[c][h-1].color)==False):    
                                    obj.a[c][h-1].color=obj.a[c][h].color
                                    obj.a[c][h].color="whait"
                                elif (obj.chick_if_goal_correct(obj.a[c][h].color,obj.a[c][h-1].color)):
                                    obj.a[c][h].color="whait"
                                    obj.a[c][h-1].color="whait"
                                else:
                                    obj.a[c][h-1].color=obj.a[c][h-1].color+"_"+obj.a[c][h].color
                                    obj.a[c][h].color="whait"      
        return graph(obj.a,obj.i,obj.j) 

    def move_to_down(self,obj):
        arraycopy=copy.deepcopy(obj.a)
        if(obj.chick_if_down()):
            for c in range(obj.i-2,-1,-1):
                for d in range(obj.j):
                    if (obj.a[c][d].color!="black" and obj.a[c][d].color!="whait" and obj.chick_if_goal(obj.a[c][d].color)==False and obj.chick_dwon(arraycopy,c,d)==True ):
                        for h in range(c,obj.i-1):
                            if(obj.chick_if_two__(obj.a[h][d].color)):
                                if(obj.chick_dwon(obj.a,h,d)):
                                    if( obj.chick_if_goal(obj.a[h+1][d].color)==False):
                                        obj.a[h+1][d].color=obj.separted(obj.a[h][d].color)
                                        obj.a[h][d].color=obj.separted_two(obj.a[h][d].color)
                                    elif (obj.chick_if_goal_correct(obj.separted(obj.a[h][d].color),obj.a[h+1][d].color)):
                                        obj.a[h+1][d].color="whait"
                                        obj.a[h][d].color=obj.separted_two(obj.a[h][d].color)                                                
                                    else:
                                        obj.a[h+1][d].color=obj.a[h+1][d].color+"_"+obj.separted(obj.a[h][d].color)
                                        obj.a[h][d].color=obj.separted_two(obj.a[h][d].color)
                            if(obj.chick_dwon(obj.a,h,d) and not obj.chick_if_two__(obj.a[h][d].color)):
                                if( obj.chick_if_goal(obj.a[h+1][d].color)==False):    
                                    obj.a[h+1][d].color=obj.a[h][d].color
                                    obj.a[h][d].color="whait"
                                elif (obj.chick_if_goal_correct(obj.a[h][d].color,obj.a[h+1][d].color)):
                                    obj.a[h][d].color="whait"
                                    obj.a[h+1][d].color="whait"
                                else:
                                    obj.a[h+1][d].color=obj.a[h+1][d].color+"_"+obj.a[h][d].color
                                    obj.a[h][d].color="whait"
        return graph(obj.a,obj.i,obj.j) 
