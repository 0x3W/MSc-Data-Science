require(tseries, quietly = TRUE)
require(igraph, quietly = TRUE)

#tech
aapl <- get.hist.quote(instrument="AAPL", start="2003-01-01", end="2008-01-01",
                       quote= "Close", provider="yahoo", drop=TRUE)
ibm <- get.hist.quote(instrument="IBM", start="2003-01-01", end="2008-01-01",
                      quote= "Close", provider="yahoo", drop=TRUE)
intc <- get.hist.quote(instrument="INTC", start="2003-01-01", end="2008-01-01",
                       quote= "Close", provider="yahoo", drop=TRUE)
qcom <- get.hist.quote(instrument="qcom", start="2003-01-01", end="2008-01-01",
                       quote= "Close", provider="yahoo", drop=TRUE)
txn <- get.hist.quote(instrument="txn", start="2003-01-01", end="2008-01-01",
                      quote= "Close", provider="yahoo", drop=TRUE)
#finance
gs <- get.hist.quote(instrument="GS", start="2003-01-01", end="2008-01-01",
                     quote= "Close", provider="yahoo", drop=TRUE)
db <- get.hist.quote(instrument="db", start="2003-01-01", end="2008-01-01",
                     quote= "Close", provider="yahoo", drop=TRUE)
citi <- get.hist.quote(instrument="c", start="2003-01-01", end="2008-01-01",
                       quote= "Close", provider="yahoo", drop=TRUE)
cs <- get.hist.quote(instrument="cs", start="2003-01-01", end="2008-01-01",
                     quote= "Close", provider="yahoo", drop=TRUE)
hsbc <- get.hist.quote(instrument="hsbc", start="2003-01-01", end="2008-01-01",
                       quote= "Close", provider="yahoo", drop=TRUE)
#energy
pten <- get.hist.quote(instrument="pten", start="2003-01-01", end="2008-01-01",
                       quote= "Close", provider="yahoo", drop=TRUE)
crzo <- get.hist.quote(instrument="crzo", start="2003-01-01", end="2008-01-01",
                       quote= "Close", provider="yahoo", drop=TRUE)
arlp <- get.hist.quote(instrument="arlp", start="2003-01-01", end="2008-01-01",
                       quote= "Close", provider="yahoo", drop=TRUE)
bpl <- get.hist.quote(instrument="bpl", start="2003-01-01", end="2008-01-01",
                      quote= "Close", provider="yahoo", drop=TRUE)
cog <- get.hist.quote(instrument="cog", start="2003-01-01", end="2008-01-01",
                      quote= "Close", provider="yahoo", drop=TRUE)

#public utility
tef <- get.hist.quote(instrument="tef", start="2003-01-01", end="2008-01-01",
                      quote= "Close", provider="yahoo", drop=TRUE)
usm <- get.hist.quote(instrument="usm", start="2003-01-01", end="2008-01-01",
                      quote= "Close", provider="yahoo", drop=TRUE)
kep <- get.hist.quote(instrument="kep", start="2003-01-01", end="2008-01-01",
                      quote= "Close", provider="yahoo", drop=TRUE)
hnp <- get.hist.quote(instrument="hnp", start="2003-01-01", end="2008-01-01",
                      quote= "Close", provider="yahoo", drop=TRUE)
adtn <- get.hist.quote(instrument="cog", start="2003-01-01", end="2008-01-01",
                       quote= "Close", provider="yahoo", drop=TRUE)

# Basic Industries
shlm <- get.hist.quote(instrument="shlm", start="2003-01-01", end="2008-01-01",
                       quote= "Close", provider="yahoo", drop=TRUE)
pkx <- get.hist.quote(instrument="pkx", start="2003-01-01", end="2008-01-01",
                      quote= "Close", provider="yahoo", drop=TRUE)
mlm <- get.hist.quote(instrument="mlm", start="2003-01-01", end="2008-01-01",
                      quote= "Close", provider="yahoo", drop=TRUE)
smg <- get.hist.quote(instrument="smg", start="2003-01-01", end="2008-01-01",
                      quote= "Close", provider="yahoo", drop=TRUE)
sqm <- get.hist.quote(instrument="sqm", start="2003-01-01", end="2008-01-01",
                      quote= "Close", provider="yahoo", drop=TRUE)

dataset <- cbind(aapl,ibm,intc,qcom,txn,gs,db,citi,cs,hsbc,pten,crzo,arlp,bpl,cog,tef,usm,kep,hnp,adtn,shlm,pkx,mlm,smg,sqm)
datasetRet <- diff(log(dataset))


R.hat = cor(datasetRet, method = 'pearson')
H = 1/2*log((1+R.hat)/(1-R.hat))
B = 10000
Delta = rep(NA,B)

for(idx in 1:B) {
  R.hat.boot = matrix(0, nrow = nrow(R.hat), ncol = nrow(R.hat))
  for(i in 1:(nrow(R.hat)-1)) {
    for(j in (i+1):nrow(R.hat)) {
      z.hat = rnorm(1,atanh(R.hat[i,j]),sqrt(1/(1258-3)))
      R.hat.boot[i,j] = tanh(z.hat)
    }
  }
  R.hat.boot = R.hat.boot + t(R.hat.boot)
  diag(R.hat.boot) = 1 
  Delta[idx] = sqrt(1258)*max(abs(R.hat-R.hat.boot))
}
C.low = R.hat - (quantile(Delta, prob = 0.05)/sqrt(1258))
C.upp = R.hat + (quantile(Delta, prob = 0.05)/sqrt(1258))
quantile(Delta, prob = 0.05)/sqrt(1258)

library(igraph)

eps = 0.4
g = graph.empty(n = ncol(datasetRet), directed = F)
V(g)$name = names(datasetRet)

for(i in 1:nrow(R.hat)){
  for(j in i+1:nrow(R.hat)){
    if(j<=nrow(R.hat) && (eps<C.low[i,j] || -1*eps>C.upp[i,j])){
      g = add.edges(g,c(names(datasetRet)[i],names(datasetRet)[j]))
    }
  }
}


#gAdj1  <- graph.adjacency(Rhat,weighted=TRUE)
#gAdjDF1 <- get.data.frame(gAdj1)
#gDF1 <- graph.data.frame(gAdjDF1)

gDF1 <- g
V(gDF1)$color <- "orange"
V(gDF1)[name == "aapl"]$color <- "yellow"
V(gDF1)[name == "qcom"]$color <- "yellow"
V(gDF1)[name == "intc"]$color <- "yellow"
V(gDF1)[name == "txn"]$color <- "yellow"
V(gDF1)[name == "ibm"]$color <- "yellow"

V(gDF1)[name == "pten"]$color <- "lightgreen"
V(gDF1)[name == "crzo"]$color <- "lightgreen"
V(gDF1)[name == "arlp"]$color <- "lightgreen"
V(gDF1)[name == "bpl"]$color <- "lightgreen"
V(gDF1)[name == "cog"]$color <- "lightgreen"

V(gDF1)[name == "tef"]$color <- "lightblue"
V(gDF1)[name == "usm"]$color <- "lightblue"
V(gDF1)[name == "kep"]$color <- "lightblue"
V(gDF1)[name == "hnp"]$color <- "lightblue"
V(gDF1)[name == "adtn"]$color <- "lightblue"

V(gDF1)[name == "shlm"]$color <- "pink"
V(gDF1)[name == "pkx"]$color <- "pink"
V(gDF1)[name == "mlm"]$color <- "pink"
V(gDF1)[name == "smg"]$color <- "pink"
V(gDF1)[name == "sqm"]$color <- "pink"

par(mfrow=c(1,1))
plot(gDF1, vertex.label=V(g)$name, edge.arrow.size=0.5, edge.width=1,
     main="Cluster")
legend('bottomleft',legend=c("Tech", "Fina", "Energy", "Public Util", "Basic Ind"),col='black',pch=21, 
       pt.bg=c("Yellow","Orange", "Lightgreen", "Lightblue", "Pink"), cex = 0.5)
