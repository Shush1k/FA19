library(lmtest)

data <- read.table("/Users/user/Documents/GitHub/FA19/Course lll/Econometrics/seminar 6/Baranov.txt")

y <- data$y
x1 <- data$x1
x2 <- data$x2
x3 <- data$x3

# 1
correl <- cor(data)
correl

rx <- correl[1, ]

rx1 <- cor(x1, y)
rx2 <- cor(x2, y)
rx3 <- cor(x3, y)

cor.test(y, x1+x2+x3, method = "pearson") # 0.3326248 => очень слабая взаимосвязь между переменными

cor.test(y, x1+x2+x3, method = "spearman")

# Hmisc::rcorr(as.matrix(data))

plot(y, x1) # Слабая положительная корреляция
plot(y, x2) # Отсутствие корреляции
plot(y, x3) # Слабая отрицательная корреляция



#2
lm1 <- lm(y ~ x1)
slm1 <- summary(lm1)
slm1


m <- lm(y ~ x1 + x3)
sm <- summary(m)
sm

# Тест на длинную и короткую регрессию
r_long <- summary(lm(y ~ x1+x2+x3))$r.squared
r_short <- sm$r.squared
F_see <- ((r_long - r_short) / (1-r_long)) * ((length(y) - 4) / 1)
F_see < 3.87


#3
slm1_r_squared <- slm1$r.squared
slm1_r_squared
slm1_std_error <- slm1$sigma
slm1_std_error
slm1_approx_error <- sum(abs(slm1$residuals/y)) / length(y) * 100
slm1_approx_error


smlm_r_squared <- sm$r.squared
smlm_r_squared
smlm_std_error <- sm$sigma
smlm_std_error
smlm_approx_error <- sum(abs(sm$residuals/y)) / length(y) * 100
smlm_approx_error


#4
# t-критерий Стьюдента для проверки значимости коэффициента корреляции
t1_p <- sqrt((rx1 ^ 2) / (1 - rx1 ^ 2) * (length(y) - slm1$fstatistic[["numdf"]]))
t_table1_p <- qt(0.975, df = slm1$fstatistic[["numdf"]])
t1_p < t_table1_p # корреляции между каждым фактором и зависимой переменной значимо отличаются от 0

t1 <- c(
  sqrt((rx1 ^ 2) / (1 - rx1 ^ 2) * (length(y) - sm$fstatistic[["numdf"]])),
  sqrt((rx3 ^ 2) / (1 - rx3 ^ 2) * (length(y) - sm$fstatistic[["numdf"]]))
)
t_table1 <- qt(0.975, df = sm$fstatistic[["numdf"]])
t1 < t_table1 # корреляции между каждым фактором и зависимой переменной значимо отличаются от 0


# t-критерий Стьюдента для оценки значимости параметров модели линейной регрессии
t2_p <- slm1$coefficients[, 1] / slm1$coefficients[, 2]
t_table2_p <- qt(0.975, df = slm1$fstatistic[["dendf"]])
t2_p < t_table2_p # Все коэфы незначимы

t2 <- sm$coefficients[, 1] / sm$coefficients[, 2]
t_table2 <- qt(0.975, df = sm$fstatistic[["dendf"]])
t2 < t_table2 # Все коэфы незначимы


# Тест Фишера
F_statistic_p <- slm1$fstatistic["value"][[1]]
F_table_p <- 2.64
F_statistic_p < F_table_p # Модель в целом значима

F_statistic <- sm$fstatistic["value"][[1]]
F_table <- 2.64
F_statistic < F_table # Модель в целом значима


#5
B_p <- slm1$coefficients[, 1]
di_lower_p <- B_p - slm1$coefficients[, 2] * t_table2_p
di_upper_p <- B_p + slm1$coefficients[, 2] * t_table2_p


B <- sm$coefficients[, 1]
di_lower <- B - sm$coefficients[, 2] * t_table2
di_upper <- B + sm$coefficients[, 2] * t_table2


#6
elastichnost_p <- c(
  slm1$coefficients[2] * mean(x1) / mean(y)
)

elastichnost <- c(
  sm$coefficients[2] * mean(x1) / mean(y),
  sm$coefficients[3] * mean(x3) / mean(y)
)

# Бета-коэф.
Sdy <- sd(y)
Sdx1 <- sd(x1)
Sdx2 <- sd(x2)
Sdx3 <- sd(x3)

beta_p <- slm1$coefficients[2] * Sdx1/Sdy

beta <- c(sm$coefficients[2] * Sdx1/Sdy, sm$coefficients[3] * Sdx3/Sdy) #

# Дельта-коэф.
delta_p <- rx1 * slm1$coefficients[2] / slm1$r.squared

delta <- c(rx1 * sm$coefficients[2] / sm$r.squared,
           rx3 * sm$coefficients[3] / sm$r.squared)


#7
xi <- qchisq(p = 0.95, df = 2)

dw_p <- dwtest(lm1)
dw_p


bg_p <- bgtest(lm1, order = 1, order.by = NULL, type = c("Chisq", "F"))
bg_p$statistic < xi
bg_p

gq_p <- gqtest(lm1, order.by = x1, fraction = 0.5)

n <- length(y)
c <- 1
F_table_gq_p <- 1.18
gq_p$statistic < F_table_gq_p
gq_p
bp_p <- bptest(lm1, studentize = TRUE)
bp_p$statistic < xi
bp_p




dw <- dwtest(m)

bg <- bgtest(m, order = 1, order.by = NULL, type = c("Chisq", "F"))
qchisq(p = 0.95, df = 2)

gq <- gqtest(m, order.by = x1, fraction = 0.5)

bp <- bptest(m, studentize = TRUE)
