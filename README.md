# qosf-task-2
## The task requires us to make a 2-qubit quantum circuit which returns |01> and |10> with equal probabilites. 
- To solve this problem I propose the following circuit and apply gradient descent to optimise the parameters (details in the notebook task2.ipynb)
<img src="https://github.com/ordinaryowl/qosf-task-2/blob/master/images/circuit.png" width="40%">

- To solve the bonus question I modify the circuit (by swapping Rx and Ry) and adding an additional overlap term in the loss function for gradient descent (details in the notebook task2.ipynb)

<img src="https://github.com/ordinaryowl/qosf-task-2/blob/master/images/circuit_bonus_q.png" width="40%">

