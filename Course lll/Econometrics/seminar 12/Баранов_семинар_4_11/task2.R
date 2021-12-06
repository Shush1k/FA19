RSS_1 <- 60
RSS_2 <- 10

k1 <- 2
k2 <- 4
n <- 55

F_statistic <- (RSS_1-RSS_2) / (k2 - k1) / (RSS_2) / (n-k2); F_statistic
qf(0.95, k2-k1, n-k2)



#2
RSS <- 20.8
RSS_1 <- 14.0
RSS_2 <- 2.0
n <- 55
n1 <- 16
n2 <- 6
k <- 3

F <- ((RSS - (RSS_1 + RSS_2)) / (RSS_1 + RSS_2)) * ((n1 + n2 - 2*(k+1)) / (k + 1)); F
qf(0.95,k+1,n1+n2-2*(k+1))