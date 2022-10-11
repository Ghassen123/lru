<h3 align="center">Design and Implement a LRU cache</h3>

<!-- ABOUT THE PROJECT -->  

## About The Project

Implement a Least Recently Used (LRU) cache and execute a given sequence of  
SET(key, value) and GET(key) operations. Return the results of all the GET operations  
from the sequence.

<!-- GETTING STARTED -->  

## Getting Started

This is an example of how you may give instructions on setting up your project locally.  
To get a local copy up and running follow these simple steps.

### Prerequisites

What you need for the project

* Python
* Docker

### Input

The input will be in a text file.

```  
Input:  
capacity = INT  
query_type = [SET, GET]  
keys = [KEY1,KEY2,KEY3]  
values = [VAL1,VAL2,VAL3]  
END INPUT  
```

### Execution

* Run Python Script

1. Clone the repo

```  
git clone https://github.com/Ghassen123/lru.git  
```  

2. Create Input file based on the following template or change the input.txt file in the input files directory:
   Example:

```  
Input:  
capacity = 1  
query_type = [SET, SET, GET, SET, GET, SET, GET]  
keys = [1, 2, 3, 4, 10, 3, 44]  
values = [11, 22, 33, 33, 1, 55, 1]  
END INPUT  
```  

3. Run LRU with the path of your added input file.
   In case you only modified the existing file, it will take it as a default.

```  
python main.py /path_to_input.txt  
```  

5. See output

* Run Docker image

1. Create Input file (INPUT_FILE.txt)
2. Run the following command line:
   To see output result of input file on the container

```  
Docker docker run --rm -it ghassentouil/lru:latest 
```  

To change the input file with your own file mount it as a volume to the container and make sure to use the absolute path
of the file in the host ($PWD/<INPUT_FILE.txt>).

``` 
docker run --rm -it -v $PWD/<INPUT_FILE.txt>:/home/app/input_files/input_file.txt ghassentouil/lru:latest  /home/app/input_files/input_file.txt
```
3. See output

## Dispaly Feature

### Report

For a better understating of the output, a report will be generated with the output detailing the input, the execution
process and the execution time .
In case of failure, an error message will be shown.

### Unit test

Create simple Unit test and Run it.

``` 
python -m unittest lru_test.py
```

### Lint

Check code quality based on sonarLint.

### Code Coverage

Run:

``` 
python -m coverage run -m unittest
```

To generate html report :

``` 
coverage report -m
```

Report :

```
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
Timer.py                     12      0   100%
lru_cache_class.py           50      0   100%
main.py                      82     12    85%   95-98, 138-139, 147-153
test_case_0_lru_test.py      19      1    95%   72
-------------------------------------------------------
TOTAL                       163     13    92%
```