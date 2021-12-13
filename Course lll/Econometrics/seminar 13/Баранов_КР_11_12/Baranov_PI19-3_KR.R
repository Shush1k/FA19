library(lmtest)
require(readxl)

data <- read_xlsx("./Baranov.xlsx")

y <- data$y
x1 <- data$x1
x2 <- data$x2

m <- lm(data)
sm <- summary(m); sm

coeff <- sm$coefficients; coeff

n <- 150
alp <- 0.5
corr <- cor(data)

rx1x2 <- ((cor(x1, x2)^2) / (1 - cor(x1, x2)^2) * (n - 2) ) ^ alp
ryx1 <- ((cor(y, x1)^2) / (1 - cor(y, x1)^2) * (n - 2) ) ^ alp
ryx2 <- ((cor(y, x2)^2) / (1 - cor(y, x2)^2) * (n - 2) ) ^ alp
t_nabl <- sqrt(corr*corr/(1-corr*corr)*(n-2)); t_nabl

R2 <- round(sm$r.squared, 3); R2
R2_adj <- round(sm$adj.r.squared, 3); R2_adj

F <- sm$fstatistic[['value']]; F
F_table <- round(pf(sm$fstatistic[["value"]], sm$fstatistic[["numdf"]], sm$fstatistic[["dendf"]], lower.tail = FALSE), 3); F_table

approx_error <- (sum(abs(sm$residuals / y)) / length(y)) * 100; round(approx_error, 3)

coef_elast <- c(
  sm$coefficients[2] * mean(x1) / mean(y),
  sm$coefficients[3] * mean(x2) / mean(y)
); round(coef_elast, 3)

Sdy <- sd(y)
Sdx1 <- sd(x1)
Sdx2 <- sd(x2)
beta <- round(c(sm$coefficients[2] * Sdx1 / Sdy, sm$coefficients[3] * Sdx2 / Sdy), 3); beta

rx1 <- cor(x1, y)
rx2 <- cor(x2, y)
delta <- round(c(rx1 * sm$coefficients[2] / sm$r.squared, rx2 * sm$coefficients[3] / sm$r.squared), 3); delta

n <- length(y)
q <- 1
m <- 2
r_long <- sm$r.squared
r_short <- summary(lm('y ~ x2'))$r.squared
F_tracked <- ((r_long - r_short) / (1-r_long)) * ((length(y) - 2) / 1); round(F_tracked, 3)
F_tb <- pf(0.975, q, n-m); F_tb
summary(lm('y ~ x2'))


gq <- gqtest(sm); gq
round(gq[['p.value']], 3)
round(gq[['statistic']], 3)
bp <- bptest(sm); bp
round(bp[['statistic']], 3)
round(bp[['p.value']], 3)

dw <- dwtest(sm); dw
round(dw[['statistic']], 3)
round(dw[['p.value']], 3)

m1 <- lm(x1 ~ x2)
sm1 <- summary(m1); sm1

m2 <- lm(x2 ~ x1)
sm2 <- summary(m2); sm2
 
VIF <- c(1 / (1-sm1$r.squared), 1 / (1-sm2$r.squared)); VIF
 
for (i in seq_along(VIF)) {
  print(paste("В переменной", i, ":"))
  if (VIF[i] > 2) {
    print("Мультиколлинеарность есть")
  } else {
    print("Мультиколлинеарности нет")
  }
}
 