'''
Created on Dec 11, 2013

@author: yongpili
'''

import pygraphviz as pyg


if __name__ == '__main__':
    A = pyg.AGraph()
    
    A.add_node('feeeeee');
    
    A.add_edge('a','b')
    
    
    A.layout('dot') # layout with dot
    A.draw('foo.png') # write to file