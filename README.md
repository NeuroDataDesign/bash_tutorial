# Bash Tutorial

In this tutorial, we will cover some introductory bash commands that will be of use to you throughout the semester. This tutorial should be relatively self-contained, but 

## Useful Utilities

### Checking running processes

### Checking Memory Usage

### Checking Processor Statistics

### Finding Files/Directories

#### Exec

### Piping

#### Awk

#### Xargs

### Running Commands in the background

#### Nohup

##### Terminating a process

###### Pkill

###### Kill

#### Screen

## Shell-Scripts

### She-bang

### Variable Declaration

#### Saving the output of a command as a variable

#### Saving the process ID of a process run in the background

### Command Line Arguments

### For-loops

### While-loops

### Sleep Command

## Exercise

Now, it is time for you guys to attempt to code up an  example to test your knowledge of what we've gone through today. Here, your goal is as follows:

1) write a python script with the following API:

```
python gen_and_plot_random_matrix.py <n> <t> </path/to/output>
<n>: the number of observations for a random timeseries
<t>: the number of timesteps for a random timeseries
</path/to/output>: the path to place the output png images
```

+ the python script should simulate a random timeseries, plot the timeseries using plotly, and then save the timeseries as a png image, following a process similar to what we do [here](https://github.com/NeuroDataDesign/jupyter_tutorial). Note that we do not plot the timeseries as a png image in this notebook, but you should be able to get some intuition from [here](https://plot.ly/python/static-image-export/) about how that might work.

2) Write a bash script with the following API:

```
./analyze_gen_and_plot_random_matrix.sh <n> <t> </path/to/output>
<n>: the number of observations for a random timeseries
<t>: the number of timesteps for a random timeseries
</path/to/output>: the path to place the output png images
```

+ Within the bash script, you should call 3 external scripts `disklog.sh`, `memlog.sh`, and `proclog.sh` and run them in the background before calling your above `gen_and_plot_random_matrix.py`. These scripts will, on each line, log the usage of memory, processor, and disk space every second in the background while the remainder of your script executes. Then, call your `gen_and_plot_random_matrix.py` from within your bash script to produce your figure. Finally, terminate each of the jobs you started in the background at the end of your shell script. 
