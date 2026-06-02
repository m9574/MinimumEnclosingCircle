import numpy as np
import matplotlib.pyplot as plt
import random
from circle import *

def min_circle_with_2_points(P, p_i, p_j):
    random_permutation_of_P = random.sample(P, len(P))
    C = Circle.make_smallest_circle_containing_points(p_i, p_j)
    for k in range(0, len(P)):
        p_k = random_permutation_of_P[k]
        if p_k not in C:
            C = Circle.make_circle_with_3_points(p_i, p_j, p_k)
    return C

def min_circle_with_1_point(P, p_i):
    random_permutation_of_P = random.sample(P, len(P))
    C = Circle.make_smallest_circle_containing_points(P[0], p_i)
    for j in range(1, len(P)):
        p_j = random_permutation_of_P[j]
        if p_j not in C:
            C = min_circle_with_2_points(random_permutation_of_P[:j], p_j, p_i) 
    return C

def min_circle(P):
    random_permutation_of_P = random.sample(P, len(P))
    p1 = random_permutation_of_P[0]
    p2 = random_permutation_of_P[1]
    C = Circle.make_smallest_circle_containing_points(p1,p2)
    for i in range(2, len(P)):
        p_i = random_permutation_of_P[i]
        if p_i not in C:
            C = min_circle_with_1_point(random_permutation_of_P[:i], p_i)
    return C

def main():
    points = [(1, 2), (3, 4), (5, 1), (2, 6), (4, 3)]
    
    C = min_circle(points)
    
    # Plot points
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    plt.scatter(xs, ys, color='blue', zorder=5)
    
    # Plot circle
    theta = np.linspace(0, 2 * np.pi, 300)
    cx = C.a + C.r * np.cos(theta)
    cy = C.b + C.r * np.sin(theta)
    plt.plot(cx, cy, color='red')
    
    plt.axis('equal')  # important — prevents circle from looking like an ellipse
    plt.show()

if __name__ == "__main__":
    main()
