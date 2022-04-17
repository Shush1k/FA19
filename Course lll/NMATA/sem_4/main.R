install.packages("devtools")
install.packages("statnet")
library(devtools)
library(statnet)
install_github("DougLuke/UserNetR")
library(UserNetR)
data(Moreno)
gender <- Moreno %v% "gender"
plot(Moreno, vertex.col = gender + 2, vertex.cex = 1.2)
network.size(Moreno)
summary(Moreno, print.adj = FALSE)
gden(Morenot)
components(Moreno) # выводит кол-во подгрупп, несвязанных между собой графов
lgo <- components.largest(Moreno, result="graph")
gd <- geodist(lgo)
max(gd$gdist) # за 11 шагов 

gtrans(Moreno, mode="graph")

netmat1 <-rbind(c(0,1,1,0,0),
                c(0,0,1,1,0),
                c(0,1,0,0,0),
                c(0,0,0,0,0),
                c(0,0,1,0,0))

rownames(netmat1) <- c("NOVOSIB","SPB","MOSCOW","ROSTOV","ELEC") 
colnames(netmat1) <- c("NOVOSIB","SPB","MOSCOW","ROSTOV","ELEC") 

net1 <- network(netmat1, matrix.type="adjacency") 
class(net1) 

summary(net1) 

plot(net1, vertex.col = 2, displaylabels = TRUE) 

netmat2 <- rbind(c(1,2), 
c(1,3), 
c(2,3), 
c(2,4), 
c(3,2), 
c(5,3)) 

net2 <- network(netmat2, matrix.type="edgelist") 
network.vertex.names(net2) <- c("NOVOSIB","SPB","MOSCOW","ROSTOV","ELEC") 

summary(net2) 

as.sociomatrix(net1) 

class(as.sociomatrix(net1)) 

all(as.matrix(net1) == as.sociomatrix(net1)) 

as.matrix(net1, matrix.type = "edgelist") 

set.vertex.attribute(net1, "gender", c("F", "F", "M", "F", "M")) 
net1 %v% "alldeg" <- degree(net1) 
list.vertex.attributes(net1) 

summary(net1) 

get.vertex.attribute(net1, "gender") 
net1 %v% "alldeg" 

list.edge.attributes(net1) 

set.edge.attribute(net1, "rndva1", 
runif(network.size(net1),0,1)) 
list.edge.attributes(net1) 
summary(net1 %e% "rndva1") 
summary(get.edge.attribute(net1, "rndva1")) 

netval1 <- rbind(c(0,2,3,0,0), 
c(0,0,3,1,0), 
c(0,1,0,0,0), 
c(0,0,0,0,0), 
c(0,0,2,0,0)) 

netval1 <- network(netval1, matrix.type="adjacency",ignore.eval=FALSE, names.eval="like")
network.vertex.names(netval1) <- c("A","B","C","D","E") 
list.edge.attributes(netval1) 
get.edge.attribute(netval1, "like") 


as.sociomatrix(netval1) 
as.sociomatrix(netval1, "like") 

netval2 <- rbind(c(0,2,3,0,0), 
c(0,0,3,2,0), 
c(0,3,0,0,0), 
c(0,0,0,0,0), 
c(0,0,2,0,0)) 

netval2 <- network(netval2, matrix.type="adjacency",ignore.eval=FALSE, names.eval="dislike") 
network.vertex.names(netval2) <- c("A","B","C","D","E") 
list.edge.attributes(netval2) 
get.edge.attribute(netval2, "dislike") 


as.sociomatrix(netval2) 
as.sociomatrix(netval2, "like") 
as.sociomatrix(netval2, "dislike")