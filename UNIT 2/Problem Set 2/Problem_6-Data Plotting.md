# Problem 6: Data Plotting

Now, you'll use your simulation to answer some questions about the robots' performance.

In order to do this problem, you will be using a Python tool called [PyLab](http://www.scipy.org/getting-started.html).

Below is an example of a plot. This plot does not use the same axes that your plots will use; it merely serves as an example of the types of images that the PyLab package produces. ![](https://d37djvu3ytnwxt.cloudfront.net/assets/courseware/v1/5e3b84f365c85ef9f5413b3d0d681c3c/asset-v1:MITx+6.00.2x_7+1T2017+type@asset+block/files_ps07_files_sampleplot-small.png)

<b>Note to those who did the optional visualization:</b> For problem 6, we make calls to <code>runSimulation()</code> to get simulation data and plot it. However, you don't want the visualization getting in the way. If you chose to do the visualization exercise, before you get started on problem 6 (and before you submit your code in submission boxes), <b>make sure to comment the visualization code out of <code>runSimulation()</b></code>. There should be 3 lines to comment out. If you do not comment these lines, your code will take a REALLY long time to run!!

<b>For the questions below, call the given function with the proper arguments to generate a plot using PyLab.</b>

## Problem 6-1
3/3 points (graded)

Examine <code>showPlot1</code> in <code>ps2.py</code>, which takes in the parameters _title_, _x_label_, and _y_label_. Your job is to examine the code and figure out what the plot produced by the function tells you. Try calling <code>showPlot1</code> with appropriate arguments to produce a few plots. Then, answer the following 3 questions.

1. Which of the following would be the best title for the graph?

  Time It Takes 1 - 10 Robots To Clean 80% Of A Room correct

2. Which of the following would be the best x-axis label for the graph?

  Number of Robots correct

3. Which of the following would be the best y-axis label for the graph?

  Time-steps correct

## Problem 6-2
3/3 points (graded)

Examine <code>showPlot2</code> in <code>ps2.py</code>, which takes in the parameters _title_, _x_label_, and _y_label_. Your job is to examine the code and figure out what the plot produced by the function tells you. Try calling <code>showPlot2</code> with appropriate arguments to produce a few plots. Then, answer the following 3 questions.

1. Which of the following would be the best title for the graph?

  Time It Takes Two Robots To Clean 80% Of Variously Shaped Rooms correct

  Examine <code>showPlot2</code> in <code>ps2.py</code>, which takes in the same parameters as <code>showPlot1</code>. Your job is to examine the code and figure out what the plot produced by the function tells you. Try calling <code>showPlot2</code> with appropriate arguments to produce a few plots. Then, answer the following 3 questions.

2. Which of the following would be the best x-axis label for the graph?

  Aspect Ratio correct

3. Which of the following would be the best y-axis label for the graph?

  Time-steps correct
