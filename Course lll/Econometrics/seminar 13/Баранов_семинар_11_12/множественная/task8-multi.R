library(lmtest)
require(readxl)
library(orcutt)
library(sandwich)


data <- read_xlsx("./data.xlsx")


data <- data[1:29, ]

y <- data$Q
x1 <- data$I
x2 <- data$M
x3 <- data$P

m <- lm(data)
sm <- summary(m); sm


coef_elast <- c(
  sm$coefficients[2] * mean(x1) / mean(y),
  sm$coefficients[3] * mean(x2) / mean(y),
  sm$coefficients[4] * mean(x3) / mean(y)
); coef_elast

# Анализ матрицы парных корреляций
correl <- cor(data); correl

# вспомогательных регрессий
m1 <- lm(x1 ~ x2 + x3)
sm1 <- summary(m1); sm1

m2 <- lm(x2 ~ x1 + x3)
sm2 <- summary(m2); sm2

m3 <- lm(x3 ~ x1 + x2)
sm3 <- summary(m3); sm3

Fm <- c(sm1$fstatistic[["value"]], sm2$fstatistic[["value"]], sm3$fstatistic[["value"]]); Fm
Fm_pv <- c(
   pf(sm1$fstatistic[["value"]], sm1$fstatistic[["numdf"]], sm1$fstatistic[["dendf"]], lower.tail = FALSE),
   pf(sm2$fstatistic[["value"]], sm2$fstatistic[["numdf"]], sm2$fstatistic[["dendf"]], lower.tail = FALSE),
   pf(sm3$fstatistic[["value"]], sm3$fstatistic[["numdf"]], sm3$fstatistic[["dendf"]], lower.tail = FALSE)
); Fm_pv

for (i in length(Fm_pv)) {
  if (Fm_pv[i] < 0.05) {
    print(paste("Фактор", i, "свидетельствует о мультиколлинеарности"))
  }
}


# коэффициентов вздутия VIF
VIF <- c(1 / (1-sm1$r.squared), 1 / (1-sm2$r.squared), 1 / (1-sm3$r.squared)); VIF

for (i in seq_along(VIF)) {
  print(paste("В переменной", i, ":"))
  if (VIF[i] > 2) {
    print("Мультиколлинеарность есть")
  } else {
    print("Мультиколлинеарности нету")
  }
}

# Тест Фаррара-Глоубера
R_1 <- cor(data); R_1
n <- 29
k <- 3
FG <- -(n-1-1/6*(2*k+5)) * log(det(R_1)); FG

if (FG > qchisq(p = 0.95, 0.5*k*(k-1))) {
  print("При 5% уровне значимости H0 отвергается - в массиве объясняющих переменных существует мультиколлинеарность")
} else {
  print("При 5% уровне значимости H0 принимается - в массиве объясняющих переменных нету мультиколлинеарности")
}




# анализа матрицы парных корреляций
cor(data)


# t-статистик
sm
# у переменной x3 наименьшая t-статистика => устраняем x3
m4 <- lm('y ~ x1 + x2')
sm4 <- summary(m4); sm4


# критерий AIC
aic <- data.frame(
            AIC(lm('y ~ x1 + x2')),
            AIC(lm('y ~ x2 + x3')),
            AIC(lm('y ~ x1 + x3')),
            AIC(lm('y ~ x1')),
            AIC(lm('y ~ x2')),
            AIC(lm('y ~ x3')))

min(aic)
# => y ~ x1 + x2