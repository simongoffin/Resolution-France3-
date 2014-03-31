# -*-coding:utf-8 -*
#!/usr/bin/python
import sys
import os
import time

root = os.path.dirname(__file__)
rel_path = os.path.join("", "aima-python")
abs_path = os.path.join(root, rel_path)
sys.path.append(abs_path)
from search import *

class ChiffresProblem(Problem):


    def __init__(self,init,goal):
        self.proche=0
        self.dico={}
        self.symetrie=0
        Problem.__init__(self, init, goal)

    
    def goal_test(self, state):
        for result in state:
            if abs(self.proche-self.goal)>abs(result-self.goal):
                self.proche=result
                if result==self.goal:
                    return True
        return False
            
    def successor(self, state):
        for valeur1 in state:
            temp=state[:]
            temp=temp[0:temp.index(valeur1)]+temp[temp.index(valeur1)+1:len(temp)]
            for valeur2 in temp:
                for operation in [1,2,3,4]:
                    check=possible(valeur1,valeur2,operation)
                    if check[0]:
                        newmove=temp[:]
                        newmove=newmove[0:newmove.index(valeur2)]+newmove[newmove.index(valeur2)+1:len(newmove)]
                        newmove=newmove+(check[1],)
                        #print newmove
                        etape=str(valeur1)+' '+check[2]+' '+str(valeur2)+' '+'='+' '+str(check[1])
                        if not newmove in self.dico:
                            yield (etape,newmove)
                            self.dico[newmove]=1
                        else: 
                            self.symetrie+=1
                            continue
                    else: continue
                    
def possible(valeur1,valeur2,operation):
    #1==+
    if operation==1:
        return [True,valeur1+valeur2,'+']
    #2==-
    elif operation==2:
        return [valeur1-valeur2>0,valeur1-valeur2,'-']
    #3==*
    elif operation==3:
        return [True,valeur1*valeur2,'*']
    #4==/
    elif operation==4:
        return [valeur1%valeur2==0,valeur1/valeur2,'/']
        
def run(tuple,solution):
    v=[]
    for i in range(5):
        v.append('---')
    problem=ChiffresProblem(tuple,solution)
    #example of bfs search
    #debut=time.time()
    node=breadth_first_graph_search(problem)
    sol=problem.proche
    if node==None:
        problem=ChiffresProblem(tuple,sol)
        node=breadth_first_graph_search(problem)
    #fin=time.time()
    path=node.path()
    path.reverse()
    compte=0
    for n in path:
        if compte>0:
            v[compte-1]=n.action
        compte+=1
    return v

