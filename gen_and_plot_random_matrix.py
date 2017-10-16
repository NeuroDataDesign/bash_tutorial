import numpy as np
from argparse import ArgumentParser
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot, plot
from plotly import tools
import plotly.plotly as py
from plotly.graph_objs import *


def gen_random_mtx(n, t):
    """
    A function to generate a random matrix, given the number of features n and the number of timesteps t.
    Produces a [n x t] array that is random.
    """
    # YOUR CODE HERE
    return random_mtx
    
def plot_mtx(mtx, out_name):
   """
   Plots a matrix as a timeseries in a given location.
   """
   # YOUR CODE HERE
   return   # shouldn't need to return anything after this
   

def main():
    """
    This is just python convention for how to handle the IO of a given script, and call the above methods.
    """
    parser = ArgumentParser()
    parser.add_argument("n", help="the number of features", type=int)
    parser.add_argument("t", help="the number of observations", type=int)
    parser.add_argument("out_name", help="the output filename to produce an image of a random matrix as a png")
    result = parser.parse_args()
    
    print(n)  # delete this before calling assignment "DONE", but just to show that the arguments are what you expect
    print(t)  # delete before calling your assignment "DONE""
    print(out_name)  # delete before calling "DONE"
    
    rmtx = gen_random_mtx(result.n, result.t)
    plot_mtx(rmtx, result.out_name)
    return
    
if __name__ == "__main__":
    main()
