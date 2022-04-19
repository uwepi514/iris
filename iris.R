
## Load Data

iris <- iris 


## IRIS Summary 
dim(iris)
str(iris)


## Iris Plots 
plot(iris)


## IRIS Regression

lm(iris$Petal.Length ~ iris$Petal.Width, data = iris)
