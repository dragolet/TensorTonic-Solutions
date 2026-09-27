def grad(a, b, x):
    return 2*a*x + b

def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    for i in range(steps):
        dev = grad(a, b, x0)
        x0 = x0 - lr*dev

    return x0