library(lmtest)
require(readxl)
library(orcutt)
library(sandwich)
library(gap)

data <- read_xlsx("Баранов_семинар_20_11/tema7.xlsx")

y <- data$y
x1 <- data$x1
x2 <- data$x2
x3 <- data$x3
x4 <- data$x4


y_c <- y[1:20]
y_l <- y[21:22]

x1_c <- x1[1:20]
x1_l <- x1[21:22]

x2_c <- x2[1:20]
x2_l <- x2[21:22]

x3_c <- x3[1:20]
x3_l <- x3[21:22]

x4_c <- x4[1:20]
x4_l <- x4[21:22]


data_control <- data[1:20, ]
data_learning <- data[21:22, ]

lm_control <- lm(y ~ x1+x2+x3+x4, data=data_control)
summary(lm_control)


predict(lm_control, newdata = data_learning, interval = "confidence")

predict(lm_control, newdata = data_learning, interval = "prediction")

cor(data_control)


### Без x3 ###
lm_without_x3 <- lm(y ~ x1+x2+x4)
summary(lm_without_x3)


predict(lm_without_x3, newdata = data_learning, interval = "confidence")

predict(lm_without_x3, newdata = data_learning, interval = "prediction")


lm_c <- lm(y_c ~ x1_c + x2_c + x3_c + x4_c)
slm_c <- summary(lm_c); slm_c


# train <- data[1:20,]
# test <- data[21:22, ]
#
# m <- lm(y ~ x1 + x2 + x3 + x4, data=train)

c <- data.frame(y_l, x1_l, x2_l, x3_l, x4_l)
colnames(c) <- c("y", "x1_c", "x2_c", "x3_c", "x4_c"); c

predict(lm_c, newdata = c, interval = "confidence")

predict(lm_c, newdata = c, interval = "prediction")


#correl
model_control <- data[1:20,]; model_control
cor(model_control)


# model_control$x3 <- NULL; model_control
# summary(lm(y_c~x1_c+x2_c+x4_c))


### Без x3 ###
wox3 <- data.frame(y_c,x1_c,x2_c,x4_c)
lm_wox3 <- lm(wox3)
summary(lm(wox3))

predict(lm_wox3, newdata = c, interval = "confidence")

predict(lm_wox3, newdata = c, interval = "prediction")


### Без x2 и x3 ###
wox2 <- data.frame(y_c,x1_c,x4_c)
lm_wox2 <- lm(wox2)
summary(lm_wox2)

predict(lm_wox2, newdata = c, interval = "confidence")

predict(lm_wox2, newdata = c, interval = "prediction")


#Парная модель
parn <- data.frame(y_c, x4_c)
lm_parn <- lm(parn)
summary(lm_parn)

predict(lm_parn, newdata = c, interval = "confidence")

predict(lm_parn, newdata = c, interval = "prediction")


#Тест Чоу
# library(qpcR)
o <- data[1:20,]
o1 <- o[1:10, ]
o2 <- o[11:20, ]
m <- lm(y~x1+x2+x3+x4, data = o)
m1 <- lm(y~x1+x2+x3+x4, data = o1)
m2 <- lm(y~x1+x2+x3+x4, data = o2)

RSS <- deviance(m)
RSS_1 <- deviance(m1)
RSS_2 <- deviance(m2)

n <- 22
n1 <- 10
n2 <- 10
k <- 4

F <- ((RSS - (RSS_1 + RSS_2)) / (RSS_1 + RSS_2)) * ((n1 + n2 - 2*(k+1)) / (k + 1)); F
qf(0.95,k+1,n1+n2-2*(k+1))

# H0 - верна
# выборки однородны