#!/bin/bash
#Understanding STDOUT and STDERR
ls
ls > listoffiles
ls 1> listoffiles
#The symbol > automatically redirects any non-error output of the
screen to listoffiles.
#The 1 > means that the standard output in particular to the
listoffiles. Now try the following command where the directory called
newdir does not exist.
ls -l . newdir
ls -l . newdir 1>presentfiles 2>filesnotpresent

#1> redirects STDOUT (i.e., successful listing of .) to presentfiles.
#2> redirects STDERR (i.e., error for missing newdir) to filesnotpresent.
#we just split the files into 2 parts, since new dir is not present

