# install.packages("MASS")
library(MASS)
options(digits=4)
num=2
set.seed(num)
sigma<-matrix(c(1,0.8,0.6,
0.8,1,0.7, 0.6,0.7,1),
nrow=3,ncol=3)
mean<-c(num*15, I(num^2), num+20)
mydata<-mvrnorm(150,mean,sigma)
mydata<-as.data.frame(mydata)
names(mydata)<-c("y","x1","x2")
#Далее можете продолжить решение в Rstudio или сохранить свой набор данных и реализовывать решение в Jupyter
write.table(mydata, file = "Baranov.txt", sep = "\t")