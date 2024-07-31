A physics engine built in python capable of simulating massive, charged, volouminous spherical objects by running a compuation for the interactions between each couple of masses. 
The engine is capable of simulating Newtonian gravitational forces, Coloumbic electrostatic forces and perfectly elastic collisions. 

As of now the simulator is in need of heavy optimisation, as some calculations are run several times more than they need to be.
Collisions are finicky under 
i) low resoulution computing due to increasing acceleration at close proximity 
ii) multiple body collisions - where kinetic energy may not be conserved. 

All calculations and processes run the engine are logged simulataniously. Minior errors will turn up only in the log files and indicate inaccurate simulation. 

Simulations are visualised using matplotlib-pyplot. 


This engine has been emulated in javascript by (a psychopathic user, who writes code of this sort in js) AshdaGrat in https://github.com/AshDaGrat/Physics-Sim . 
AshDaGrat uses different (and an agruably better) collision mechanics and also offers a UI allowing quick changes to the starting conditions. 

https://github.com/AshDaGrat
