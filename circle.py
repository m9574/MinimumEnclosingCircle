import math

class Circle:
    # $(x-a)^{2} + (y - b)^{2} = r^{2}$
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r
    
    def __contains__(self, point):
        if self.a is None or self.b is None or self.r is None or point is None:
            return None
        x = point[0]
        y = point[1]
        return (x - self.a)**2 + (y - self.b)**2 <= self.r**2
    
    def make_smallest_circle_containing_points(a, b):
        # Center: $c = (\frac{a_x + b_x}{2},\frac{a_y + b_y}{2})$
        cx = (a[0] + b[0]) / 2
        cy = (a[1] + b[1]) / 2

        # Radius: $\sqrt{(c_x - a_x)^2 + (c_y - a_y)^2}$
        r = math.sqrt((cx - a[0])**2 + (cy - a[1])**2)
        return Circle(cx, cy, r)
    
    def make_circle_with_3_points(a, b, c):
        ax, ay = a
        bx, by = b
        cx, cy = c

        # MIDPOINTS
        # Midpoint (Side 1): $(\frac{a_x + b_x}{2}, \frac{a_y + b_y}{2})$
        m1 = ((a[0] + b[0])/2, (a[1] + b[1])/2)
        # Midpoint (Side 2): $(\frac{a_x + b_x}{2}, \frac{a_y + b_y}{2})$
        m2 = ((a[0] + c[0])/2, (a[1] + c[1])/2)

        # SLOPES
        # Slope (Side 1): $\frac{b_y - a_y}{b_x - a_x}$
        s1 = (b[1] - a[1]) / (b[0] - a[0])
        # Slope (Side 2): $\frac{c_y - a_y}{c_x - a_x}$
        s2 = (c[1] - a[1]) / (c[0] - a[0])

        # PERPENDICULAR BISECTOR SLOPES
        ps1 = -1 / s1
        ps2 = -1 / s2

        # CIRCUMCENTER
        # Solving $m_1(x - x_1) + y_1 = m_2(x - x_2) + y_2$ for x.
        x = (ps2 * m2[0] - ps1 * m1[0] + m1[1] - m2[1]) / (ps2 - ps1)
        # Then plugging it for the y value for one of the equations
        y = ps1 * (x - m1[0]) + m1[1]

        # RADIUS
        r = math.sqrt((x - ax)**2 + (y - ay)**2)

        return Circle (x, y, r)

            