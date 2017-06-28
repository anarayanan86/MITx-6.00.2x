# Problem 2
Bookmark this page
## Problem 2: R^2
10.0/10.0 points (graded)  
After we create some regression models, we also want to be able to evaluate our models to figure out how well each model represents our data, and tell good models from poorly fitting ones. One way to evaluate how well the model describes the data is computing the model's R^2 value. R^2 provides a measure of how well the total variation of samples is explained by the model.

Implement the function <code>r_squared</code>. This function will take in:

- list, <code>y</code>, that represents the y-coordinates of the original data samples
- estimated, which is a corresponding list of y-coordinates estimated from the regression model

This function should return the computed R^2 value. You can compute R^2 as follows, where <math>e_i</math> is the estimated y value for the i-th data point (i.e. predicted by the regression), $y_i$ is the y value for the ith data point, and $mean$ is the mean of the original data samples.

![](https://d37djvu3ytnwxt.cloudfront.net/assets/courseware/v1/83df4c1c72ef01bd64e3ff4af2d2f60c/asset-v1:MITx+6.00.2x_7+1T2017+type@asset+block/r2.PNG)

If you are still confused about R^2 , its [wikipedia](https://en.wikipedia.org/wiki/Coefficient_of_determination) page has a good explanation about its use/how to calculate it.

Note: If you want to use numpy arrays, you should <code>import numpy as np</code> and use <code>np.METHOD_NAME</code> in your code. Unfortunately, <code>pylab</code> does not work with the grader.

```python
import numpy as np

def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    # TODO
    y, estimated = np.array(y), np.array(estimated)
    SEE = ((estimated - y)**2).sum()
    mMean = y.sum()/float(len(y))
    MV = ((mMean - y)**2).sum()
    return 1 - SEE/MV
```

correct
