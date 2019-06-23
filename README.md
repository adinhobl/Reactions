# Reactions
Vizualization of concentration curves for chemical reactions. Solved using a finite difference approximation and plotted to show the concentration curves over the course of the reaction. This package could be extended to visualize 'any' set of first order differential equations - e.g. population dynamics.


## Requirements
This package only requires `plotly` and `numpy` and is written in jupyter notebooks.

## How to Use
For the system of chemical reactions below:
* A + 2B &rarr; C 
* C &rarr; A + 2B
* A + C &rarr; D

The input to liquid_react would be as follows:
```python
liquid_react([(-1,-2,1,0),(1,2,-1,0),(-1,0,-1,1)], # Stoichiometric breakdown of reactants and products
             [(1,1,0,0),(0,0,1,0),(1,0,1,0)],      # Powers of each component (A,B,C,D) for the rate equations
             [10,5,0,0],                           # Initial concetrations of each component
             [0.05,0.02,0.03]                      # Reaction rate (k) constant for each reaction
            )
```
Tuples are required for each set of stoichiometric and exponential parameters to demarcate separate reactions.

```
concs, times = liquid_react([(-1,-2,1,0),(1,2,-1,0),(-1,0,-1,1)],
                            [(1,1,0,0),(0,0,1,0),(1,0,1,0)],
                            [10,5,0,0],
                            [0.05,0.02,0.03],
                           duration=30)
```
```
plot_concs(concs,times)
```