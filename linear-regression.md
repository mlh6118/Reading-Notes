# Linear Regression in Python

"Linear regression is a basic and commonly used type of predictive analysis. 
The overall idea of regression is to eamine two things: (1) does a set of 
predictor variables do a good job in predicting an outcome (dependent) 
variable?  (2) Which variables in particular are significant predictors of 
the oucome variable, and in what way do they impact the outcome variable?"  

"Three major uses for regression analysis are (1) determining the strength 
of predictors, (2) forecasting an effect, and (3) trend forecasting."

Source: [What is Linear Regression](https://www.statisticssolutions.com/free-resources/directory-of-statistical-analyses/what-is-linear-regression/)

There are 6 major types of linear regression.  The one that the rest of this 
README will focus on is how to perform a simple linear regression using 
Python and additional libraries.

The steps required are:
1. Import the required Python libraries into the Notebook being used, such 
   as kaggle.com.
   ```
   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   import sklearn
   ```
   Instead of `import sklearn`, one can use
   ```
   from sklearn.linear_model import LinearRegression
   from sklearn.model_selection import train_test_split
   ```
2. Import the dataset.  In kaggle.com, this is done using the +Add Data button.
3. Convert the data into a pandas data frame.
   ```
   dataname = pd.read_csv('<file path>')
   print(dataname)
   ```
4. If there are lots of different data categories within the same data set, it 
   might be advantageous to use `print dataname.DESCR` to get information 
   about the data set and its various categories.
5. Select the X and y features from the data set.
6. Reshape the data as a 2D array.
    ```
    X = X.reshape(-1, 1)
    print(X)
    ```
7. Set up the train and test variables.  The sizes are the percent of the 
   data you want to use.  The random_state is also a percentage.
    ```
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.8, test_size=.2, random_state=100)

    print(f'X_training shape[{X_train.shape}]')
    print(f'X_test shape [{X_test}]')
    print(f'y_training shape[{y_train}]')
    print(f'y_test shape [{y_test}]')
    ```
8. Run a scatter plot.
    ```
    plt.scatter(X_train, y_train)
    plt.xlabel('<x-axis label>')
    plt.ylabel('<y-axis label>')
    plt.title('<chart title>')
    plt.show()
    ```
9. Run the linear regression.
    ```
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_predict = lr.predict(X_test)
    ```
10. Get the training accuracy.
    ```
    print(f'Training Acc {round(lr.score(X_train, y_train) * 100, 2)}%')
    print(f'Testing Acc {round(lr.score(X_test, y_test) * 100, 2)}%')
    ```
11. Add the linear regression line to the scatter plot.
    ```
    plt.scatter(X_train, y_train)
    plt.plot(X_test, y_predict)
    plt.xlabel('<x-axis label>')
    plt.ylabel('<y-axis label>')
    plt.title('<chart title>')
    plt.show()
    ```
    
Sources: 
1. [How to run Linear regression in Python scikit-Learn](https://www.crayondata.com/how-to-run-linear-regression-in-python-scikit-learn/)  
2. Lab Lecture - 06/27/22