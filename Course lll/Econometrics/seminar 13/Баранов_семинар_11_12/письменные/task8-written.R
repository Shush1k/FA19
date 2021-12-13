#Task 1
R_1 <- cbind(
  c(2.9, -1.045, -1.633),
  c(-2.232, 2.683, -0.131),
  c(-0.142, -1.415, 1.96)
)

n <- 100
k <- 3

det_r <- det(solve(R_1))

FG <- -(n-1-1/6*(2*k+5)) * log(det_r); FG

Fx1 <- (R_1[1,1] - 1) * ((n-k-1)/k)

Fx <- NULL
for (i in 1:3) {
  Fx <- c(Fx, ((R_1[i,i] - 1) * ((n-k-1)/k)))
}

FX <- matrix(Fx,nrow = 3,ncol = 3); FX
Fx < qf(0.95,k,n-k-1)


Rx <- c()

for (i in 1:3) {
  for (j in 1:3) {
    Rx <- c(Rx, c(-R_1[i, j] / (R_1[i, i] * R_1[j, j])^0.5))
  }
}; Rx

Rx <- matrix(Rx,nrow = 3,ncol = 3); Rx
Rx <- c(Rx[2,1], Rx[3,2], Rx[3,1]); Rx

t_m <- matrix(1:9, nrow=3)
# for (i in 1:3) {
#   for (j in 1:3) {
#     t_m[i, j] <- Rx[i, j] * (n-k-1)^0.5 / (1 - Rx[i,j]^2)^0.5
#   }
# }; t_m


#Task 2
n <- 200
k <- 3
R_sqr <- c(0.6, 0.55, 0.66)

VIF <- 1 / (1-R_sqr); VIF

for (i in 1:3) {
  if (VIF[i] > 1) {
    print(paste("Мультиколлинеарность для",VIF[i],"есть"))
  }
}

#Task 3
n <- 200
k <- 3
det_r <- 0.562

FG <- -(n-1-1/6*(2*k+5)) * log(det_r); FG

xxx <- 1/2 * k * (k-1); xxx
xi <- 0.35185

# Мультиколлинеарности нету
if (FG < xi) {
  print("Мультиколлинеарности нету")
}