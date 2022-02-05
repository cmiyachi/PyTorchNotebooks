# DSND - Lesson 2 - Quiz 8 / 2

# Let's say that we have a line whose equation is y = -0.6x + 4. For the point (x,y) = (-5, 3), apply the square trick to get the new equation for the line, using a learning rate of alpha = 0.01alpha=0.01.

# Report your answer in the form y = w_1x + w_2, substituting appropriate values for w_1 and w_2.

a = 0.01
w1 = -0.6
w2 = 4
p = -5
q = 3
q_ = w1 * p + w2

print(f'y = {w1 + p * a * (q - q_)}x + {w2 + a * (q - q_)}')
