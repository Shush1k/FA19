library(lmtest)
require(readxl)
library(orcutt)
library(sandwich)


data <- read_xlsx("./data.xlsx")


data <- data[1:13, ]

Q <- data$Q
L <- data$L
K <- data$K

mlm <- lm('Q ~ L + K', data=data)
smlm <- summary(mlm); smlm

coef_elast <- c(
  smlm$coefficients[2] * mean(L) / mean(Q),
  smlm$coefficients[3] * mean(K) / mean(Q)
); coef_elast

b1 <- coef_elast[1]; b1
b2 <- coef_elast[2]; b2
