#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   Takahiro Oshima <tarotora51@gmail.com>
# License:  MIT License
# Created:  2017-10-01
#
from graphillion import GraphSet
import graphillion.tutorial as tl

def countGridGraphSet(num):
    universe = tl.grid(num, num)
    GraphSet.set_universe(universe)
    start = 1
    goal = (num + 1) ** 2
    paths = GraphSet.paths(start, goal)
    return len(paths)

if __name__ == "__main__":
    print("8 x 8 : ",countGridGraphSet(8))
    #print("9 x 9 : ",countGridGraphSet(9))
