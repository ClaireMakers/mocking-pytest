### Today's objectives: 
Covering: 

- What mocks are, and how they fit in the context of unit and integrations tests.
- How to identify what needs to be mocked in a multi-class system.
- How to implement the mocking logic and write unit tests with them.

### Quick refresher: unit vs integration tests: 

Unit tests: Testing a contained unit of your code in isolation - for instance, testing a single function/method. 

Integration tests: Testing two pieces of code that depend on each other to function and making sure they integrate well together. For instance, testing a multi-class system where methods from different clases need to work together. 

Dependencies: reliance on an other piece of code in order to function - can be within your own multi-class system, or can be reliance on external libraries or frameworks. 

### What is mocking, and what do we use it for? 

Testing unit without having to rely on external factors - we want to sever any dpendencies and test a unit in isolation again, even though it normally relies on an external piece of code in order to function. 

To achieve this, we want to create a "fake" version of that dependency, which has similar properties to the real thing, but is created by us to control the test environment. 

### Looking at some examples - mapping out dependencies are where mocking would be useful: 

--> miro board: https://miro.com/app/board/uXjVNLp71mY=/

### Implementing mocks in Python: 
