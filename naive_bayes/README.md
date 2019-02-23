Cancer Test
------------



    ---------------------------
   |                           |  <-- All people
   |      --                   |
   |     |  |<--1%             |  1% has Cancer
   |     |  |                  |  99 % don't
   |      --                   |  90% of 1% have positive test cancer
   |                           |  10 % of 99% of Non cancer people have Positive test.
   |                           |  
   |                           |  
   |                           |
   |                           |
    ---------------------------
 
Bayes Rule
----------

prior probability * test evidence  = posterior probability


Prior:
prior probability of cancer P(c) = 0.01 1%  P(NC) = 0.99
                           P(Pos | c) = 0.9 90% 
			   P(Neg | NC) 0.9
			   P(Pos | NC) = 0.1

Posterior: --> Often called as Joint		
posterior probability given test is positive 
	P(c | pos) = P(c) * P(Pos | c)  c--> cancer
	P(NC | pos) = P(NC) * P (Pos | NC)  --> Positive test result for not cancer

	P(c|pos) = 0.009
        P(NC|Pos) = 0.099
                + --------
                    0.108

Normalize
    P(Pos) = P(c | pos) + P(NC | pos) =0.108

Posterior:
 P (c | Pos)  = P (c | pos) / P (Pos) = 0.009 / 0.108 =0.0833 
 P (NC | pos) = P (NC|pos) / P(Pos)  = 0.099 / 0.108 = 0.9166
                                                      +-------
                                                          1



P(C) Prior 
P(Pos | c) sensitivity
P(neg | nc) specitivity

pos    P(c) -- mul P (Pos|c)-->  P(Pos,c) Positive cancer hypothesis
       P(c) -- mul { (pos|nc)-->  P(Pos, nc) Positive non cancer hypothesis
                    --add--> + P (Pos) total prob. that test is what it was
      divide P(Pos,c) / P (Pos)  --> This gives posterior prob. P(C | Pos)
    and divide P(Pos, nc) /P(Pos)--> This is posterior prob . P(NC | Pos)
       if we add these up, posterior probability , it will sum to one.

This is BAYES  RULE::
Adarsh

