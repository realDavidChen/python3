## how to create virtualenv

### install virtualenv

 $  sudo apt install python3-virtualenv
 
 ### create new virtualenv

 $  virtualenv -p python3 venv
 
 ### activate virtualenv venv

  $  source ./venv/bin/activate
  
  ### install package sample
  
  $  pip install Flask
  $  pip list



> note. the virtualenv only use system python verison as the working environment, if you want different version, please using the Miniconda.
