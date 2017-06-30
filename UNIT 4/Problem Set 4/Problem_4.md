# Problem 4
Bookmark this page
## Problem 4-1
5.0/5.0 points (graded)  
Let's try another way to get data points and see whether we can find some evidence for global warming. We surmise, due to global warming, the average temperature should increase over time. Thus, we are going to plot the results of a linear regression on the average annual temperature of Boston.

In a similar manner to Problem 3, fill in the missing piece to the following code. The code should generate your data samples. Each sample represents a year from 1961 to 2005 and the average annual temperature in Boston in that year (again, the provided helper class is helpful). Fit your data to a linear line with <code>generate_models</code> and plot the regression results with <code>evaluate_models_on_training</code>.

```python
# Problem 4: FILL IN MISSING CODE TO GENERATE y VALUES
x1 = INTERVAL_1
x2 = INTERVAL_2
y = []
# MISSING LINES
models = generate_models(x1, y, [1])    
evaluate_models_on_training(x1, y, models)
```

```python
for year in INTERVAL_1:
    y.append(numpy.mean(raw_data.get_yearly_temp('BOSTON', year)))
```
correct


## Problem 4-2
5.0/5.0 points (graded)  
What is the R^2 value? (use 3 decimal places)

0.085
correct
