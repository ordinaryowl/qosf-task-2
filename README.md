# qosf-task-2
## The task requires us to make a 2-qubit quantum circuit which returns |01> and |10> with equal probabilites. 
## Solution can be found in the notebook "task2.ipynb".
- To solve this problem I propose the following circuit and apply gradient descent to optimise the parameters (details in the notebook task2.ipynb)
<img src="https://github.com/ordinaryowl/qosf-task-2/blob/master/images/circuit.png" width="40%">

- To solve the bonus question I modify the circuit (by swapping Rx and Ry) and adding an additional overlap term in the loss function for gradient descent (details in the notebook task2.ipynb)
<img src="https://github.com/ordinaryowl/qosf-task-2/blob/master/images/circuit_bonus_q.png" width="40%">

## Comments/Discussion about the results:
- The circuit proposed for the bonus question can as well solve the entire question.
- The results for n=1 measurement per step suggests that the post-measurement state hops between |01> or |10> with probability 1. This is because the full wavefunction is an equal superposition of the two states, hence single measurement only gives one of the two as output with probability 1.
- The results for n=1,10,100,1000 suggest that with more measurements, the algorithm takes longer (more steps to converge to the solution with fixed error). The n=1000 case estimates the true probability distribution of the state better than say n=10 measurements. I suppose this is why, the gradient steps which depend on the probability distribution gets smaller for n=1000, hence requiring more steps to converge (to a more accurate fit to the desired wavefuntion).
- I noticed that the probabilities P0,P1,P2 and P3 for the output state to collapse into |00>,|01>,|10> and |11> are independent of the order of Rx,Ry in the top branch of the circuit. This is why we see that both a (parameter for Rx) and b (parameter for Ry) both converge to about pi/2 (although the loss landscape figure for a=1.5 seems to indicate that b could take any value). It is the symmetry (of probability) between Rx,Ry which fixes b~pi/2.
