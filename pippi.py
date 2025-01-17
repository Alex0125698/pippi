#!/usr/bin/env python3 

#############################################################
# pippi: parse it, plot it
# ------------------------
# A program for operating on MCMC chains and related lists of
# samples from a function or distribution.  pippi can merge,
# parse and plot sample ensembles ('chains'), either in terms
# of the likelihood/fitness function directly, or as implied
# posterior probability densities.  With the addition of a
# user-defined function, it can also post-process ('pare')
# chains.
#
# Author: Pat Scott (patscott@physics.mcgill.ca)
# Originally developed: March 2012
# 
# Modified by A.S. Woodcock July 2021
# 
#############################################################

import sys
import os
from pippi_utils import *
from pippi_probe  import *
from pippi_merge  import *
from pippi_pare   import *
from pippi_parse  import *
from pippi_script import *
from pippi_plot   import *

def main(arguments):
  # Starting routine

  print(arguments)

  arguments = ['./pippi.py', 'example/plotRules.pip']

  commandLineOptions = { 'probe':probe, 'merge':merge, 'pare':pare, 'parse':parse, 'script':script, 'plot':plot }

  if (len(arguments) == 1):
    #Print usage info and quit if pippi is invoked without an argument
    usage()

  else:
    try:
      #Check if pippi has been invoked with one of the five known specific commands
      command = commandLineOptions[arguments[1]]
      if not command in [merge, pare]:
        print()
        print('Beginning pippi '+arguments[1]+' operation...')
      try:
        command(arguments[2:])
      except BaseException as err:
        print()
        print('Running pippi failed in '+command.__name__+' operation, due to error:')
        print(err)
        print()
        sys.exit()
      if not command in [merge, pare]:
        print()
        print('Completed sucessfully.')
        print()
    except KeyError:
      #Otherise check if it has been invoked with just a filename
      if os.path.isfile(arguments[1]):
        print()
        print('Beginning pippi parse-to-plot operation...')
        for command in [parse, script, plot]:
          command(arguments[1:])
          # try:
          #   command(arguments[1:])
          # except BaseException as err:
          #   print()
          #   print('Running pippi failed in '+command.__name__+' operation.')
          #   print(err)
          #   print()
          #   sys.exit()
        print()
        print('Completed sucessfully.')
        print()
      else:
        # Otherwise crack it and tell the user to get their shit in order
        print()
        print('Can\'t find file '+arguments[1])
        usage()

  sys.exit()

#Actual program launched on invocation
main(sys.argv)

