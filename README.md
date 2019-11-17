# GTMARL-SC2EV
2019 Fall - Game theory and Multi-agent RL Termproject

__Objective__: Acheving agent(s) that plays StarCraft2 microcontrol environment __well__ as much as possible with any possible manners.
except modifying followings:
* The design of state, observation function: The state and observation function will be determined by the `SMAC StarCraft2Env`. We will use the default state, observation function when we validate the project outcomes.

## Note on modifications
Any modification will be welcomed except the design of state and obsrevation function only if the modifation is well reasoned and documented.

## Grading Policy
We will grade the project outcomes __only based on__ the average winning rate. The average winning rate will be computed through another testing code. Therefore, every trained model should work proprely without any modification of the [test code](https://github.com/Junyoungpark/GTMARL-SC2EV/blob/master/test/run_model.py) except `load_model` and `test_model`.

## Project deliverable
We expected to get `a short report` (<= 3pages) that is about 
1. the main algorithm that you used, 
2. details of tweaks that you used for improving or stabilizing the algorithm, and 
3. Test performance in the [test suite](https://github.com/Junyoungpark/GTMARL-SC2EV/blob/master/test/run_model.py) 

Also, you need to submit a `saved version` of your model and corresponding code snippet to validate the outcome. You can find the detail from [here](https://github.com/Junyoungpark/GTMARL-SC2EV/blob/master/test/run_model.py).

## Installation guide

### Install Starcraft2   
SMAC is based on the full game of StarCraft II (versions >= 3.16.1). To install the game, follow the commands bellow.  

__Linux__  
Please use the Blizzard's [repository](https://github.com/Blizzard/s2client-proto#downloads) to download the Linux version of StarCraft II. By default, the game is expected to be in `~/StarCraftII/` directory. This can be changed by setting the environment variable `SC2PATH`.  

__Windows and Mac__  
Please install StarCraft II from [Battle.net](https://starcraft2.com/). The free Starter Edition also works. PySC2 will find the latest binary should you use the default install location. Otherwise, similar to the Linux version, you would need to set the SC2PATH environment variable with the correct location of the game.


###  Install SMAC (Starcraft Multi-Agent Challenge)

```
$ pip install git+https://github.com/oxwhirl/smac.git
```

Alternatively, you can clone the SMAC repo and install `smac`
```
$ git clone https://github.com/oxwhirl/smac.git
$ pip install smac/
```

### Install SMAC Maps

Download the [SMAC Maps](https://github.com/oxwhirl/smac/releases/download/v0.1-beta1/SMAC_Maps.zip) and extract them to your `$SC2PATH/Maps` (in Windows, `C:/Program Files (x86)/StarCraft II/Maps` by default.) directory. If you installed SMAC via git, simply copy the SMAC_Maps directory from smac/env/starcraft2/maps/ into $SC2PATH/Maps directory. Make sure to have following directory structure `$SC2PATH/Maps/SMAC_Maps`


