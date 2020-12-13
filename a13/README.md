# Day 13 part I
This is mostly a math problem. Let's focus on the general problem with one bus first. Given a start time `t`, and bus ID `x`, if `t` is a multiple of `x`, then the earliest time we can board the bus is just `t`. Otherwise, at time `t`, the bus would have left `t mod x` minutes ago, thus the next bus will come after `x - (t mod x)` minutes. So the earliest time we can board bus `x` starting at time `t` would be 

<img src="https://latex.codecogs.com/svg.latex?\text{earliest}&space;=&space;\left\{\begin{matrix}&space;t&space;&&space;\text{if&space;}t\text{&space;mod&space;}x&space;\equiv&space;\text{0}\\&space;t&space;&plus;&space;x&space;-&space;(t\text{&space;mod&space;}x)&space;&&space;\text{otherwise}&space;\end{matrix}\right." title="\text{earliest} = \left\{\begin{matrix} t & \text{if }t\text{ mod }x \equiv \text{0}\\ t + x - (t\text{ mod }x) & \text{otherwise} \end{matrix}\right." />

Now back to the problem: we can safely ignore the buses with IDs 'x', as they don't affect the final answer. So to find the earliest time, we just need to run through all the bus IDs, and do the calculation above, and take the smallest. 

# Day 13 part II
This is when things get interesting. If we use the example IDs `7,13,x,x,59,x,31,19`, we need to find a `x` such that `x` is a multiple of 7, 1 less of a multiple of 13, 4 less of a multiple of 59, and so on. So if we write it out using equations, we get:

<img src="https://latex.codecogs.com/svg.latex?\\&space;\text{x}&space;\equiv&space;\text{0&space;(mod&space;7)}&space;\\&space;\text{x}&space;\equiv&space;\text{-1&space;(mod&space;13)}&space;\\&space;\text{x}&space;\equiv&space;\text{-4&space;(mod&space;59)}&space;\\&space;\text{x}&space;\equiv&space;\text{-6&space;(mod&space;31)}&space;\\&space;\text{x}&space;\equiv&space;\text{-7&space;(mod&space;19)}" title="\\ \text{x} \equiv \text{0 (mod 7)} \\ \text{x} \equiv \text{-1 (mod 13)} \\ \text{x} \equiv \text{-4 (mod 59)} \\ \text{x} \equiv \text{-6 (mod 31)} \\ \text{x} \equiv \text{-7 (mod 19)}" />

This is a classic math problem called the Chinese Remainder Theorm. There is an algorithm of finding such `x` using the Extended Euclidean Algorithm. There is a mathematical proof of correctness, but I won't go into it as it took me 1 whole semester of first year university math course to learn it (throwback to Math145 with David Jao), but you can read more about it in https://rosettacode.org/wiki/Chinese_remainder_theorem. 
