library(lmtest)
library(binom)
require(readxl)
library(forecast)
library(tseries)

data <- read_xlsx('./data/data.xlsx')


x <- data$"Год"
y <- data$GDP
GDP <- c(data$GDP)

t <- c(1:40)
d1 <- rep(c(1, 0, 0, 0), times = 10)
d2 <- rep(c(0, 1, 0, 0), times = 10)
d3 <- rep(c(0, 0, 1, 0), times = 10)

plot(y, x)


lm <- lm(y~t+d1+d2+d3)
slm <- summary(lm)
slm
GDP1 <- ts(data = GDP, start = c(2009), frequency = 4, name = "GDP")

pred <- data.frame(c(41, 42, 43), c(1, 0, 0), c(0, 1, 0), c(0, 0, 1))
colnames(pred) <- c("t", "d1", "d2", "d3")
predictedGDP <- predict(lm, newdata = pred)


dw <- dwtest(lm);dw

bg <- bgtest(lm, order = 1, order.by = NULL, type = c("Chisq", "F")); bg
# qchisq(p = 0.95, df = 2)

gq <- gqtest(lm, order.by = x, fraction = 0.5); gq

bp <- bptest(lm, studentize = TRUE); bp

acf(GDP1, plot=FALSE)

pacf(GDP1, plot=FALSE)

tsdisplay(GDP1)

adf.test(GDP1) # стационарый
PP.test(GDP1) # стационарынй
Box.test(GDP1)







