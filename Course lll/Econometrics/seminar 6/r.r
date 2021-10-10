setwd('/Users/user/Documents/GitHub/FA19/Course lll/Econometrics/seminar 6')
getwd()
library(lmtest)
require(readxl)
data <- read_xlsx("./GAM.xlsx")
print(data)
y <- data$y
x1 <- data$x1
x2 <- data$x2
x3 <- data$x3
x4 <- data$x4

#линейная модель 
m<-lm(y ~ x1 + x2 + x3 +x4, data = data)
m
sm<-summary(m)
sm
A1 <- (sum(abs(sm$residuals/y))/length(y))*100

print(sm$sigma)
print(sm$r.squared)
print(sm$fstatistic)
print(A1)

sm = summary(m);sm
e=sm$residuals;e


#GQtest
gq = gqtest(m, order.by= ~y, fraction=0, data=data);gq
# pv<a => присутствует проблема гетероскедастичности

#BPtest
bp = bptest(m, data=data);bp
# pv<a => присутствует проблема гетероскедастичности

#DWtest
dw = dwtest(m);dw
# pv>a => H0 принимается, автокорреляция первого порядка отсутствует

#BGtest
bg = bgtest(m,order = 1);bg
bgF = bgtest(m,order = 1,type = "F");bgF
# pv>a => H0 принимается, автокорреляция первого порядка отсутствует

e2 = e^2
plot(data$x1, e2)
plot(data$x2, e2)
plot(data$x3, e2)
plot(data$x4, e2)