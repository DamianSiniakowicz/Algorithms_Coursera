# randomized contraction algorithm for finding min cuts

min_cut_hw = read.table("~/Dropbox/Algorithms/min_cut_hw.txt",fill=TRUE,header=FALSE,col.names=(paste(1:40,"var")))

# test cases

#min_cut_hw = read.table("~/Dropbox/Algorithms/test_cases/case5.txt",fill=TRUE,header=FALSE,col.names=(paste(1:8,"var")))

print("A")

library(foreach)
library(foreach)
library(doParallel)
library(parallel)
numCores <- detectCores()
cl <- makeCluster(numCores)
registerDoParallel(cl)

print("B")

least_crossing_edges = NA
 
sol <- foreach(x=1:3000) %dopar% {
  print("HIIIII")
  print(paste("round:",x))
  print(paste("best cut so far:",least_crossing_edges))


  min_cut_copy = min_cut_hw

  vertices_sets = sapply(1:(nrow(min_cut_copy)),list)


  while(TRUE){

    while(TRUE){
      row <- sample(1:(nrow(min_cut_copy)),1)
      column <- sample(2:(ncol(min_cut_copy)),1)
      if(is.na(min_cut_copy[row,column])){
        next
      }
      else{
        vertex1 <- row
        vertex2 <- min_cut_copy[row,column]
        break
      }
    }

    min_cut_copy[row,column] <- NA
    other_column <- which(min_cut_copy[vertex2,] == vertex1)
    min_cut_copy[vertex2,other_column] <- NA

    vertex1_set_index <- which(TRUE == sapply(vertices_sets, function(x){vertex1 %in% x}))
    vertex2_set_index <- which(TRUE == sapply(vertices_sets, function(x){vertex2 %in% x}))

    vertex1_set <- vertices_sets[[vertex1_set_index]]
    vertex2_set <- vertices_sets[[vertex2_set_index]]

    for(first_vertex in vertex1_set){
      for(second_vertex in vertex2_set){
        connected <- which(second_vertex == min_cut_copy[first_vertex,])
        if(length(connected) == 1){
          min_cut_copy[first_vertex,connected] <- NA
          other_end <- which(first_vertex == min_cut_copy[second_vertex,])
          min_cut_copy[second_vertex,other_end] <- NA
        }
      }
    }

    vertices_sets[[vertex1_set_index]] <- c(vertices_sets[[vertex1_set_index]],vertices_sets[[vertex2_set_index]])
    vertices_sets[[vertex2_set_index]] <- NULL

    if(length(vertices_sets) == 2){
      crossing_edges <- sum(sapply(min_cut_copy[,2:(ncol(min_cut_copy))],function(x){sum(!is.na(x))})) / 2
      return(crossing_edges)
      if(is.na(least_crossing_edges) || least_crossing_edges > crossing_edges){
        least_crossing_edges <- crossing_edges
      }
      break
    }
  }
}
minnn <- min(sol)
write.csv(minnn,"~/Dropbox/Algorithms/solution.txt")
#return(least_crossing_edges)
