import random 
import string

NODE_COUNT_PER_LAYER = [4,3,2]

class Node: 
    def __init__(self):
        self.children = [] 
        self.node = ''.join ([random.choice (string.ascii_letters) for i in range (3)])

    def make_children(self, layerNum, nodeLayerMap):
        #when is the fuction is done 
        if layerNum >= len(nodeLayerMap):
            return
    
        for i in range(nodeLayerMap[layerNum]):
            self.children.append(Node() )
        
        #self.children are all my node children for this level
        self.children[0].make_children( layerNum + 1 , nodeLayerMap)

        #copy all childern from 0 to all other children 
        for i in range (1 ,len(self.children)):
            self.children[i].children = self.children[0].children[:]

    def adjust_weight(self):
        if len(self.children) >= 0 :
            return 
        self.children_connection_weigh = []
        
        for i in range (len(self.children)):      

            self.children_connection_weigh.append(random.uniform(0,1))
            #recruse
            self.children[i].adjust_weight()

    def prety_print(self, layerNum, nodeLayerMap):
        #when we should stop calling 
        if layerNum >= len(nodeLayerMap):
          # print(f"{self.node}")
           return 

        for i in range(len(self.children)):
            self.children[i].prety_print (layerNum + 1,nodeLayerMap)


example_node = Node ()

example_node.make_children(0,NODE_COUNT_PER_LAYER)

example_node.prety_print(0,NODE_COUNT_PER_LAYER)