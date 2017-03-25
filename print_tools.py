#coding=utf8

########################################################################
###                                                                  ###
### Created by Martin Genet, 2012-2017                               ###
###                                                                  ###
### University of California at San Francisco (UCSF), USA            ###
### Swiss Federal Institute of Technology (ETH), Zurich, Switzerland ###
### École Polytechnique, Palaiseau, France                           ###
###                                                                  ###
########################################################################

import sys

########################################################################

def my_print(
        verbose,
        string,
        newline=True,
        flush=True):

    if not hasattr(my_print, "initialized"):
        my_print.initialized = True
        my_print.verbose_ini = verbose
    if (verbose > 0):
        sys.stdout.write((my_print.verbose_ini - verbose)*" |  "+string)
        if (newline):
            sys.stdout.write("\n")
        if (flush):
            sys.stdout.flush()

########################################################################

def print_str(string, tab=0, newline=True, flush=True):
    sys.stdout.write(" | "*tab + string)
    if (newline): sys.stdout.write("\n")
    if (flush):   sys.stdout.flush()

def print_var(name, val, tab=0, newline=True, flush=True):
    sys.stdout.write(" | "*tab + name + " = " + str(val))
    if (newline): sys.stdout.write("\n")
    if (flush):   sys.stdout.flush()

def print_sci(name, val, tab=0, newline=True, flush=True):
    sys.stdout.write(" | "*tab + name.ljust(13) + " = " + format(val,".4e"))
    if (newline): sys.stdout.write("\n")
    if (flush):   sys.stdout.flush()

########################################################################

#class Printer:
    #def __init__(self):
        #self.cur_level = 0

    #def inc(self):
        #self.cur_level += 1

    #def dec(self):
        #self.cur_level -= 1

    #def print_str(self, string, var_level=0):
        #print  " | "*(self.cur_level+var_level) + string

    #def print_var(self, name, val, var_level=0):
        #print " | "*(self.cur_level+var_level) + name + " = " + str(val)

    #def print_sci(self, name, val, var_level=0):
        #print " | "*(self.cur_level+var_level) + name.ljust(13) + " = " + format(val,".4e")
