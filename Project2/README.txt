CS 622
Project 2
Arunava Nag

Summary of Implementation (Code is documented inside the python files)

1.1 Perceptron Test

> Initialized weights and bias to 0
> Setup a max epoch limit
> In a loop calculate activation for each input and compare activation*label > 0 for 1 and for <= 0 returned 0
> Using that information updated weights and labels accordingly
> returned the final weights and labels after converged


1.2 Perceptrons Train

> Initialized a new array with weights and bias from previous function
> In a loop calculated activation for each input and compared activation*label > 0 for returning labels and for <=0 returned 0
> Compared the newly created label with expected existing labels
> Calculated accuracy from the difference between the expected and predicted labels 


2. Gradient Descent

> Initialized goal gradient magnitude, max epochs, counter for epochs, step size
> while checked if the gradient has reached the small set magnitude and max iterations
> calculate gradient
> calculate epochs and repeat till the precise gradient magnitude is reached

