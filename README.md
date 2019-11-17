# GTMARL-SC2EV
2019 Fall - Game theory and Multi-agent RL Termproject

__Objective__: Acheving agent(s) that plays StarCraft2 microcontrol environment __well__ as much as possible with any possible manners.

Requirements:

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

Download the [SMAC Maps] (https://github.com/oxwhirl/smac/releases/download/v0.1-beta1/SMAC_Maps.zip) and extract them to your $SC2PATH/Maps directory. If you installed SMAC via git, simply copy the SMAC_Maps directory from smac/env/starcraft2/maps/ into $SC2PATH/Maps directory.


