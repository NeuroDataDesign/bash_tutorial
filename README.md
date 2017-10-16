# Bash Tutorial

In this tutorial, we will cover some introductory bash commands that will be of use to you throughout the semester. This tutorial should be relatively self-contained, but 

## Basics

### pwd

`pwd` will return for you the current directory you are in. For example:

```
$ pwd
/home/eric
```

Where `/home/eric` is the directory I was currently in when I ran that script.

### ls

The `ls` command lists the contents of a given directory. It can be used as follows:

```
ls [args] <path>
[args]: useful args include -l, -h, -t
<path>: an optional directory to list the contents of.
```

For example, we might call:

```
ls -l -h -t /data
```

which for me returns:

```
drwxrwxr-x  2 eric eric 4.0K Oct 13 11:20 connectome_stats
drwxrwxr-x  5 eric eric 4.0K Oct 13 09:02 fmri
drwxrwxr-x 26 eric eric 4.0K Oct 11 10:54 hive
drwxrwxr-x 14 eric eric 4.0K Oct  1 18:14 dwi
drwxrwxr-x  3 eric eric 4.0K Sep  6 18:02 paper
drwxrwxr-x  8 eric eric 4.0K Aug 25 22:32 BIDs_test
-rw-rw-r--  1 eric eric 1.5G Aug 25 22:30 test.tar.gz
```

Note that it returns all information about the files in `/data` for me (thanks to `-l`), orders them seequentially (thanks to `-t`), along with the sizes of each file in human-readable format (thanks to `-h`).

### cd

`cd` allows us to change directories as follows:

```
cd </goal/path>
# </goal/path> an optional argument to change to a specific directory. If unspecified, changes to the user's home directory.
```

### cp

This function will copy a file from one place to another. It can be used as follows:

```
cp <src/path/file.ext> <tgt/path/file.ext>
# <src/path/file.ext>: the path to a desination file to copy
# <tgt/path/file.ext>: the path to copy the file to
```

#### Useful arguments

##### Wildcard

We can copy a group of files matching a particular substring with:

```
cp <src/path/pattern1*pattern2> <tgt/path/>
# <src/path/pattern1*pattern2>: the path to a group of files to look for, where pattern1 is the first substring the files
    start with, and pattern 2 is the pattern to end with. The wildcard (*) specifies to match any number of characters in
    between. Note that if pattern1 is empty, we will match any files ending in pattern2, or vice versa. Alternatively, we
    can match all files by just specifying (*).
<tgt/path/>: the path to copy the file (s) to.
```

If we have the following hierarchy:

```
./eric/
├── testdir/
│   └── example1.ext
│   └── example2.ext
./tgt
```

We can copy both `example1.ext` and `example2.ext` to `./tgt` with:

```
cp ./eric/testdir/*.ext ./tgt
```

resulting in:

```
./eric/
├── testdir/
│   └── example1.ext
│   └── example2.ext
./tgt
└── example1.ext
└── example2.ext
```

##### Recursive

Similarly, we may want to just copy an entire folder altogether with the recursive argument:

We can copy a group of files matching a particular substring with:

```
cp -r <src/path/> <tgt/path/>
# <src/path/>: 
<tgt/path/>: the path to copy the file (s) to.
```

If we have the following hierarchy:

```
./eric/
├── testdir/
│   └── example1.ext
│   └── example2.ext
./tgt
```

We can copy all of `./eric` with:

```
cp -r ./eric/ ./tgt
```

resulting in:

```
./eric/
├── testdir/
│   └── example1.ext
│   └── example2.ext
./tgt
├── testdir/
│   └── example1.ext
│   └── example2.ext
```

##### Parent

The most useful, and under-utilized, argument for `cp` in my opinion is the `cp --parent /src /tgt`. This will copy whatever file you specified in `/src`, and copy it (with all parent paths) to the target directory. For example, if you have a file:

```
./eric/
├── testdir/
│   └── example1.ext
│   └── example2.ext
./tgt
```

and you want to retain information contained in the file hierarchy (here, just `testdir/`, but we may have many levels of directories that we want to retain). You can retain this information as follows:

```
cp --parent eric/testdir/example tgt
```

and the resulting tree will be:

```
./eric/
├── testdir/
│   └── example
./tgt
└── eric/
    └── testdir/
        └── example
```

As we can see, we have retained the additional `eric/testdir` granularity of directories, which is incredibly powerful when combined with other commands further down, such as `find`. 

## Piping

Note: for this example, we will use the `docker ps -a` command to check running docker containers as an example:

```
docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                   PORTS               NAMES
23ff2148be0c        1e4c1dc6409f        "/bin/bash"              6 weeks ago         Exited (0) 6 weeks ago                       pensive_wozniak
3bc66ef9c99c        eb2290890e9d        "/bin/bash"              6 weeks ago         Exited (0) 6 weeks ago                       stoic_torvalds
b8dc089f0242        eb2290890e9d        "/bin/bash"              6 weeks ago         Exited (0) 6 weeks ago                       boring_wescoff
36f70e3494df        eb2290890e9d        "/bin/bash"              6 weeks ago         Exited (0) 6 weeks ago                       thirsty_hypatia

```

### Head

The `head` command allows us to retrieve the top lines of a file:

```
command | head -<n>
<n> is the number of lines you want to keep from the top of the file
```

```
docker ps -a | head -1
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                   PORTS
```

### Tail

Similarly, the `tail` command allows us to retrieve the bottom lines of a file:

```
command | tail -<n>
<n> is the number of lines to print from the bottom of the file
```

```
docker ps -a | tail -1
36f70e3494df        eb2290890e9d        "/bin/bash"              6 weeks ago         Exited (0) 6 weeks ago                       thirsty_hypatia
```


### Awk

`awk` allows us to do many things, one useful of which is to filter out a particular column of interest. For example, if we run a program that prints to console a tab-formatted list:

```
docker ps -a | head -5 | tail -4
              NAMES
23ff2148be0c        1e4c1dc6409f        "/bin/bash"              6 weeks ago         Exited (0) 6 weeks ago                       pensive_wozniak
3bc66ef9c99c        eb2290890e9d        "/bin/bash"              6 weeks ago         Exited (0) 6 weeks ago                       stoic_torvalds
b8dc089f0242        eb2290890e9d        "/bin/bash"              6 weeks ago         Exited (0) 6 weeks ago                       boring_wescoff
36f70e3494df        eb2290890e9d        "/bin/bash"              6 weeks ago         Exited (0) 6 weeks ago                       thirsty_hypatia

```
, we can extract the first column with:

```
docker ps -a | head -5 | tail -4 | awk '{print $1}'
23ff2148be0c
3bc66ef9c99c
b8dc089f0242
36f70e3494df
```

### Xargs

The `xargs` command allows us to pipe the output of a given function, which may be many lines, one line at a time into a desired second function. For example, if we build off the first example and want to kill the containers with the ids specified, we can do it en-masse with:

```
docker ps -a | head -5 | tail -4 | awk '{print $1}' | xargs docker rm -f '{}' ';'
```

### Grep

Given the following docker images:

```
docker images
REPOSITORY           TAG                 IMAGE ID            CREATED             SIZE
ericw95/mummp        0.0.1               d0ac20da4aff        5 weeks ago         4.872 GB
ericw95/fngs         0.0.10              36464a840245        6 weeks ago         4.887 GB
<none>               <none>              1e4c1dc6409f        6 weeks ago         4.887 GB
<none>               <none>              eb2290890e9d        6 weeks ago         4.887 GB
<none>               <none>              ddf728fa1b4d        6 weeks ago         945.1 MB
neurodata/fsl_1604   0.0.1               3477a235be2a        6 weeks ago         917.3 MB
neurodata/fsl_1604   latest              3477a235be2a        6 weeks ago         917.3 MB
<none>               <none>              d10891e0c12e        6 weeks ago         4.913 GB
<none>               <none>              2feaf34b8717        6 weeks ago         4.913 GB
<none>               <none>              d2f84e0df008        6 weeks ago         911.1 MB
<none>               <none>              9a0837b5c645        6 weeks ago         463.4 MB
<none>               <none>              86fd4337eb8d        6 weeks ago         4.913 GB
<none>               <none>              23181cd9c746        6 weeks ago         4.865 GB
<none>               <none>              f868cc69f88a        6 weeks ago         4.954 GB
<none>               <none>              2dfc0efee4e7        6 weeks ago         4.754 GB
ubuntu               16.04               ccc7a11d65b1        9 weeks ago         120.1 MB
neurodata/fsl_1604   <none>              b852353fa38c        10 weeks ago        915.1 MB

```

The grep command matches lines with a particular substring. For example, if we only wanted to find docker images that are a particular docker repository:

```
docker images | grep 'neurodata/fsl_1604'
neurodata/fsl_1604   0.0.1               3477a235be2a        6 weeks ago         917.3 MB
neurodata/fsl_1604   latest              3477a235be2a        6 weeks ago         917.3 MB
neurodata/fsl_1604   <none>              b852353fa38c        10 weeks ago        915.1 MB
```

## Useful Utilities

### Checking running processes

The first, most basic thing a new linux user may want to is see the statistics of processes currently running on the computer. This can be done with the ps command:

```
ps [args]
# [args]: useful args include -a (show processes started actively), -u (shows processes that are owned by the user),
    -x (shows all processes owned by root). These can be strung together with ps -aux
```

We may want to filter for a given process. For example, to see if `jupyter` is running, we can do:

```
ps -aux | grep 'jupyter'
eric      3327  0.0  0.0  21292   940 pts/17   S+   14:50   0:00 grep --color=auto jupyter
eric     21586  0.0  0.2 321516 78512 pts/2    Sl+  09:06   0:10 /home/eric/Documents/research/ndmg-repos/env-ndmg/bin/python2 /home/eric/Documents/research/ndmg-repos/env-ndmg/bin/jupyter-notebook
```

### Checking Memory Usage

We can check the memory available with `free`:

```
free -m
              total        used        free      shared  buff/cache   available
Mem:          32019       10296       14472         178        7250       20962
Swap:         32611           0       32611
```

Note that we can usefully string this together with piping to extract only the memory used:

```
free -m | grep 'Mem' | awk '{print $3}'
```

### Checking Processor Statistics

The `top` command:

```
top
top - 14:53:58 up 3 days, 20:14,  1 user,  load average: 0.17, 0.17, 0.12
Tasks: 303 total,   1 running, 302 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.3 us,  0.2 sy,  0.0 ni, 99.5 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem : 32787560 total, 14513124 free, 10819460 used,  7454976 buff/cache
KiB Swap: 33394684 total, 33394684 free,        0 used. 21173848 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                                                                                                                                 
 1253 root      20   0  500224  97688  70512 S   2.0  0.3  18:15.03 Xorg                                                                                                                                    
31732 eric      20   0 1838028 375696  90308 S   1.0  1.1  22:43.62 compiz                                                                                                                                  
32049 eric      20   0  679632  45232  29936 S   1.0  0.1   0:19.70 gnome-terminal-                                                                                                                         
  930 eric      20   0 1492772 311868  98040 S   0.3  1.0   0:44.24 chrome                                                                                                                                  
 1269 root     -51   0       0      0      0 S   0.3  0.0   9:51.93 irq/44-nvidia                                                                                                                           
 2735 eric      20   0 1257676 260904  79292 S   0.3  0.8   0:12.75 chrome                                                                                                                                  
 7404 eric      20   0 1719176 473244 149220 S   0.3  1.4  41:47.93 chrome                                                                                                                                  
11360 eric      20   0 3322856 298072 105872 S   0.3  0.9  12:04.14 rstudio                                                                                                                                 
16459 eric      20   0 1362336 476328  85884 S   0.3  1.5   1:08.01 chrome                                                                                                                                  
30208 eric      20   0 1608016 758300  70520 S   0.3  2.3   4:57.95 chrome                      
```

### Finding Files/Directories

The `find` command:

```
find <src/path> [args]
<src/path>: the path to a directory to find.
[args]: optional arguments to match files with. Useful arguments include -name "*name*", -wholename "*name*", -type [f for
    file or d for directory], -maxdepth <i> to match to a directory-depth of at most i, -mindepth <i> to match to a 
    directory-depth of at least i
```

#### Exec

### Running Commands in the background

#### Nohup

Run a command in the background as follows:

```
nohup <my command> &
```

For example, to run the python script, "example.py" with input arguments for "n1", we would run as follows:

```
nohup python example.py n1 &
```

nohup puts the command to the background, and the `&` means to ignore output from the command. Note that the nohup command spits back the process id, which you can later use to kill the process if need be later. 

If you are using bash and want to save the process id as a variable for `<my command>`, it can be done as follows:

```
nohup <my command> &
pid=$!
```

`$!` essentially is an intermediate that holds the process information for the preceding line in `bash`.
##### Terminating a process

###### Pkill

We can kill a process with a string:

```
pkill -f <string>
<string> the name of a process we wnat to kill.
```

For example, to kill `RStudio` when it inevitably hangs, we can do:

```
pkill -f RStudio
```

and RStudio will be killed.

###### Kill

To kill a process given the process id (from nohup, or by crossreferencing from `ps`):

```
kill <pid>
```

## Shell-Scripts

A shell-script, or bash-script, is a program written in the language of your terminal session.

### She-bang

A shebang tells the interpreter what language to use for a script to be run. This allows users to 

### Variable Declaration

Variables in bash are declared as follows:

```
variable1=<something>
```

where `<something>` can be a string, integer, filepath, etc.

#### Saving the output of a command as a variable

From within a bash script, you can save the output of a command-line command as follows:

```
information=$(<command>)
```

For example, to get the current directory you are in from within a shell-script, you could do it as follows:

```
current_dir=$(pwd)
```

### Command Line Arguments

In a `bash`-script, command line arguments are passed as follows. If your command was run as:

```
./my_script.sh <arg1> <arg2> <arg3> ...
```

You can access these arguments within your script very simply:

```
# note this is within your bash script!

arg1=$1
arg2=$2
arg3=$3
...
```

and the arguments will be saved as strings.

## Exercise

Now, it is time for you guys to attempt to code up an  example to test your knowledge of what we've gone through today. Here, your goal is as follows:

1) write a python script with the following API:

```
python gen_and_plot_random_matrix.py <n> <t> </path/to/output.png>
<n>: the number of observations for a random timeseries
<t>: the number of timesteps for a random timeseries
</path/to/output>: the path to place the output png image
```

+ the python script should simulate a random timeseries, plot the timeseries using plotly, and then save the timeseries as a png image, following a process similar to what we do [here](https://github.com/NeuroDataDesign/jupyter_tutorial). Note that we do not plot the timeseries as a png image in this notebook, but you should be able to get some intuition from [here](https://plot.ly/python/static-image-export/) about how that might work.

2) Write a bash script with the following API:

```
./analyze_gen_and_plot_random_matrix.sh <n> <t> </path/to/output.png>
<n>: the number of observations for a random timeseries
<t>: the number of timesteps for a random timeseries
</path/to/output>: the path to place the output png image
```

+ Within your bash script, you should call your above `gen_and_plot_random_matrix.py`. Skeleton code will be provided [bash skeleton code](https://github.com/NeuroDataDesign/bash_tutorial/blob/master/gen_and_plot_random_mtx.sh) and [python skeleton code](https://github.com/NeuroDataDesign/bash_tutorial/blob/master/gen_and_plot_random_matrix.py). You should begin by downloading these two files, and then running the script with both in the same folder to test. 

For reference, the above assignment is known as a `wrapper function`. This means that we have an existing program in one language that we may want to be generalized to another language without reimplementing the entire script. This is useful, for instance, if we want to use a particular library (such as `plotly` in this case) that we cannot access from the language we are using to wrap (in this case `bash`).  This procedure is extremely common in data science.
