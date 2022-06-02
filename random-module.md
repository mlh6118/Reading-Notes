# Random Module, Risk Analysis, Test Coverage

## How to Use Random Module
* Provides access to functions that support many operations
  * `random.randint(lowest, highest)`: Random integer between a lowest and 
    highest value
  * `random.random()`: Allows for multiplying the random number by a larger 
    number
  * `random.choice( [ 'a', 'b', 'c'] )`: Chooses from the choices in the list
  * `from random import shuffle`<br>
    `shuffle(x)`: shuffles elements in a list to be in random order
  * `random.randrange(start, stop[, step])`: Generates randomly selected 
    element from range
* Allows the generation of random numbers
  * Used for anything from picking a random number to making a password 
    database more secure.

##### Source: [How to use the Random Module in Python](https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python)

## Risk Analysis in Software Testing
* Risk: Probability of any unwanted incident
* Risk analysis: Process of identifying risks in applications or software 
  and prioritizing them for testing

#### Possible Risks
* Use of new hardware
* Use of new technology
* Use of new automation tool
* Sequence of code
* Availability of test resources for the application

#### Risk Magnitude Indicators
* High: non-tolerable, company might face loss
* Medium: tolerable, not desirable, company may suffer financially
* Low: tolerable, little to no external exposure or financial loss

#### Risk Identification
* Business risks: most common risk associated with the topic.  May come from 
  company or customer, not project
* Testing risks: based on platform working on and software testing tools used
* Premature Release risk: release of unsatisfactory or untested software
* Software risks: associated with software development process

#### Risk Assessment
* Most important step in risk analysis process
* Needs to be dealt with programmatically

#### Perspective of Risk Assessment
* Effect: identify a condition, event, or action and determine it's impact
* Cause: scan the problem and determine the most probable reason for it
* Likelihood: probability a requirement won't be satisfied

#### How to Perform Risk Analysis
* Search the risk
* Analyze the impact of each risk
* Measures for the risk identified

##### Source: [What is Risk Analysis in Software Testing and how to perform it?](https://www.edureka.co/blog/risk-analysis-in-software-testing/)

## Test Coverage
* Test coverage or code coverage: useful tool for finding untested parts of 
  codebase
* Doing enough testing means:
  * Rarely get bugs that escapse into production __and__
  * Rarely hesitant to change some code for fear it will cause production bugs

##### Source: [TestCoverage](https://martinfowler.com/bliki/TestCoverage.html)