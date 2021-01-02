## Optimization algorithms
<br>

_Correct answers are in **bold**._
<br>


**Question 1**. Which notation would you use to denote the 3rd layer’s activations when the input is the 7th example from the 8th minibatch?

* a[3]{7}(8)

* a[8]{7}(3)

* **a[3]{8}(7)**

* a[8]{3}(7)


**Question 2**. Which of these statements about mini-batch gradient descent do you agree with?

* You should implement mini-batch gradient descent without an explicit for-loop over different mini-batches, so that the algorithm processes all mini-batches at the same time (vectorization). 

* Training one epoch (one pass through the training set) using mini-batch gradient descent is faster than training one epoch using batch gradient descent.

* **One iteration of mini-batch gradient descent (computing on a single mini-batch) is faster than one iteration of batch gradient descent.**


**Question 3**. Why is the best mini-batch size usually not 1 and not m, but instead something in-between?

* If the mini-batch size is 1, you lose the benefits of vectorization across examples in the mini-batch.

If the mini-batch size is m, you end up with stochastic gradient descent, which is usually slower than mini-batch gradient descent. 

If the mini-batch size is m, you end up with batch gradient descent, which has to process the whole training set before making progress. 
Correct

If the mini-batch size is 1, you end up having to process the entire training set before making any progress. 
4.
Question 4

Suppose your learning algorithm’s cost JJJ, plotted as a function of the number of iterations, looks like this: 

Which of the following do you agree with?

1 / 1 point

If you’re using mini-batch gradient descent, this looks acceptable. But if you’re using batch gradient descent, something is wrong.

Whether you’re using batch gradient descent or mini-batch gradient descent, something is wrong. 

Whether you’re using batch gradient descent or mini-batch gradient descent, this looks acceptable. 

If you’re using mini-batch gradient descent, something is wrong. But if you’re using batch gradient descent, this looks acceptable. 
Correct
5.
Question 5

Suppose the temperature in Casablanca over the first three days of January are the same:

Jan 1st: θ1=10oC\theta_1 = 10^o Cθ1​=10oC

Jan 2nd: θ210oC\theta_2 10^o Cθ2​10oC

(We used Fahrenheit in lecture, so will use Celsius here in honor of the metric world.) 

Say you use an exponentially weighted average with β=0.5\beta = 0.5β=0.5 to track the temperature: v0=0v_0 = 0v0​=0, vt=βvt−1+(1−β)θtv_t = \beta v_{t-1} +(1-\beta)\theta_tvt​=βvt−1​+(1−β)θt​. If v2v_2v2​ is the value computed after day 2 without bias correction, and v2correctedv_2^{corrected}v2corrected​ is the value you compute with bias correction. What are these values? (You might be able to do this without a calculator, but you don't actually need one. Remember what is bias correction doing.)
1 / 1 point

v2=10v_2 = 10v2​=10, v2corrected=10v_2^{corrected} = 10v2corrected​=10

v2=7.5v_2 = 7.5v2​=7.5, v2corrected=7.5v_2^{corrected} = 7.5v2corrected​=7.5

v2=10v_2 = 10v2​=10, v2corrected=7.5v_2^{corrected} = 7.5v2corrected​=7.5

v2=7.5v_2 = 7.5v2​=7.5, v2corrected=10v_2^{corrected} = 10v2corrected​=10
Correct
6.
Question 6

Which of these is NOT a good learning rate decay scheme? Here, t is the epoch number. 
1 / 1 point

α=11+2∗tα0\alpha = \frac{1}{1+2*t} \alpha_0α=1+2∗t1​α0​

α=etα0 \alpha = e^t \alpha_0 α=etα0​

α=1tα0\alpha = \frac{1}{\sqrt{t}} \alpha_0α=t

​1​α0​

α=0.95tα0 \alpha = 0.95^t \alpha_0 α=0.95tα0​
Correct
7.
Question 7

You use an exponentially weighted average on the London temperature dataset. You use the following to track the temperature: vt=βvt−1+(1−β)θtv_{t} = \beta v_{t-1} + (1-\beta)\theta_tvt​=βvt−1​+(1−β)θt​. The red line below was computed using β=0.9\beta = 0.9β=0.9. What would happen to your red curve as you vary β\betaβ? (Check the two that apply)

1 / 1 point

Decreasing β\betaβ will shift the red line slightly to the right.

Increasing β\betaβ will shift the red line slightly to the right.
Correct

True, remember that the red line corresponds to β=0.9\beta = 0.9β=0.9. In lecture we had a green line $$\beta = 0.98) that is slightly shifted to the right. 

Decreasing β\betaβ will create more oscillation within the red line.
Correct

True, remember that the red line corresponds to β=0.9\beta = 0.9β=0.9. In lecture we had a yellow line $$\beta = 0.98 that had a lot of oscillations.

Increasing β\betaβ will create more oscillations within the red line.
8.
Question 8

  Consider this figure:

These plots were generated with gradient descent; with gradient descent with momentum (β\betaβ = 0.5) and gradient descent with momentum (β\betaβ = 0.9). Which curve corresponds to which algorithm? 
1 / 1 point

(1) is gradient descent. (2) is gradient descent with momentum (large β\betaβ) . (3) is gradient descent with momentum (small β\betaβ)

(1) is gradient descent with momentum (small β\betaβ), (2) is gradient descent with momentum (small β\betaβ), (3) is gradient descent

(1) is gradient descent. (2) is gradient descent with momentum (small β\betaβ). (3) is gradient descent with momentum (large β\betaβ)

(1) is gradient descent with momentum (small β\betaβ). (2) is gradient descent. (3) is gradient descent with momentum  (large β\betaβ)
Correct
9.
Question 9

Suppose batch gradient descent in a deep network is taking excessively long to find a value of the parameters that achieves a small value for the cost function J(W[1],b[1],...,W[L],b[L])\mathcal{J}(W^{[1]},b^{[1]},..., W^{[L]},b^{[L]})J(W[1],b[1],...,W[L],b[L]). Which of the following techniques could help find parameter values that attain a small value forJ\mathcal{J}J? (Check all that apply) 

1 / 1 point

Try tuning the learning rate α\alphaα
Correct

Try initializing all the weights to zero

Try better random initialization for the weights
Correct

Try using Adam
Correct

Try mini-batch gradient descent 
Correct
10.
Question 10

Which of the following statements about Adam is False?
1 / 1 point

The learning rate hyperparameter α\alphaα in Adam usually needs to be tuned.

We usually use “default” values for the hyperparameters β1,β2\beta_1, \beta_2β1​,β2​ and ε\varepsilonε in Adam (β1=0.9\beta_1 = 0.9β1​=0.9, β2=0.999\beta_2 = 0.999β2​=0.999, ε=10−8\varepsilon = 10^{-8}ε=10−8)

Adam combines the advantages of RMSProp and momentum

Adam should be used with batch gradient computations, not with mini-batches.
