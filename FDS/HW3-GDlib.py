import numpy as np

def descent(y, x, alpha=1e-3, itr=1e2, eps=1e-6):
    def convergence(theta, previous_theta):
        diff_norm = np.linalg.norm(theta - previous_theta, ord=1)
        new_norm = np.linalg.norm(theta, ord=1)

        if new_norm == 0:
            return False

        return diff_norm / new_norm <= eps

    # This extends the input observations to include a bias factor 1.
    X = np.hstack((np.ones((x.shape[0], 1)), x))

    # Initialize the coefficient's vector with ones.
    theta = np.zeros((x.shape[1] + 1, 1))

    for iteration in range(int(itr)):
        previous_theta = np.copy(theta)

        # Compute the gradient
        gradient = -2 * X.T.dot(y - np.dot(X, theta)[:, 0])

        theta -= alpha * gradient[:, np.newaxis] #/ X.shape[0]

        # Check if the convergence criterion is satisfied
        if convergence(theta, previous_theta):
            break

    # Return the final thetas
    return theta.ravel()
def r2(y, c, x):
    # Compute the predictions
    predictions = np.dot(np.hstack((np.ones((x.shape[0], 1)), x)), c)

    # Mean of the observed data
    ymean = np.mean(y)

    # Total sum of squares
    SStotal = np.sum(np.square(y - ymean))

    # Residual sum of squares
    SSresiduals = np.sum(np.square(y - predictions))

    return 1. - SSresiduals / SStotal


def predict(x, theta):
    X = np.hstack((np.ones((x.shape[0], 1)), x))
    return np.dot(X, theta)


