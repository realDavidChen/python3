# conda environments manage

## create conda new environments

$ conda create --name py36 python=3.6 pip numpy

## conda env list

$ conda env list

## activate py36 env

$ conda activate py36

 you will see: (py36)$  in terminal

$ python 

 into conda python 3.6 env

$ exit()  

exit

## packages manages, list\search\and install, example:

**package list**

$ conda list

**search pages**

$ conda search kivy

or 

$ pip search kivy

 note: pip can get more package

**install package**

$ pip install kivy==1.11.1


## copy project env

### 1.check package explicit link

$ conda list --explicit

export explicit to txt file

$ conda list --explicit > py3.6_reqs.txt

### 2. create new project and copy explicit package list

$ conda deactivate

$ conda create -n project2 --file py3.6_reqs.txt

$ conda env list

new env: project2 in list

$ get help

$ conda activate project2

$ conda list

you can see the same package list in the project2

## conda remove env

$ conda env list

$ conda remove -n *** --all

## get help

conda -h

**More specific help**

$ conda create -h

$ conda remove -h

