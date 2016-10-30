# main
data <- read.table('~/Dropbox/Algorithms/Djikstra_Data.txt',sep = "\t", col.names = paste(0:30,"vertex_distance"),fill=TRUE)
data <- data[,-1]
master_split <- lapply(names(data),function(x){ strsplit(as.character(data[,x]),split=",") }) # 30 lists, each of length 200, 2 entries in each
doubled_data <- data.frame(row.names = 1:200)
num_pair <- ncol(data)
num_vertices <- nrow(data)

# test_1

# data <- read.table('~/Dropbox/Algorithms/Djikstra_Test/test_1.txt',sep=" ",col.names = paste(0:4,"vertex_distance"),fill=TRUE)
# data <- data[,-1]
# master_split <- lapply(names(data),function(x){ strsplit(as.character(data[,x]),split=",") })
# num_pair <- ncol(doubled_data)
# num_vertices <- nrow(doubled_data)


# loop over each list in master list, loop over each vertex and distance in each list, get that stuff and cbind it to doubled_data
for (pair in 1:num_pair) {
	one_col <- master_split[[pair]]
	for (vertex_distance in 1:2) {
		col <- sapply(one_col,function(x){if(length(x)!=0){as.numeric(x[vertex_distance])}else{NA}})
		doubled_data <- cbind(doubled_data,col)		
		}	
	}



explored_vertices <- numeric()

shortest_paths <- numeric(num_vertices)

reached_new_node <- TRUE

# initialize
shortest_paths[1] <- 0
explored_vertices <- c(explored_vertices,1)

iter <- 1

while( length(explored_vertices) < num_vertices && reached_new_node){ # if vertex unreachable, set distance to 1,000,000.... source vertex is 1 

	iter <- iter + 1

	# main loop : loop over all explored nodes, and all their connections to nodes outside the explored space
	closest_new_node <- NA
	shortest_distance_to_new_node <- 1000000
	for (explored_node in explored_vertices){
		for (connection in seq(1,(num_pair*2),2)) {
			new_node <- doubled_data[explored_node,connection]
			if(is.na(new_node)){
				break
				}
			edge_length <- doubled_data[explored_node,connection+1]
			path_length <- edge_length + shortest_paths[explored_node]
			if(path_length < shortest_distance_to_new_node && !(new_node %in% explored_vertices)){
				shortest_distance_to_new_node <- path_length
				closest_new_node <- new_node}
			}
		}
	if (!is.na(closest_new_node)){
		shortest_paths[closest_new_node] <- shortest_distance_to_new_node
		explored_vertices <- c(explored_vertices,closest_new_node)
		}
	else {
		reached_new_node <- FALSE}

}

for (i in 2:num_vertices){
	if(shortest_paths[i] == 0){
		shortest_paths[i] <- 1000000
	}
}

print(c(shortest_paths[7],shortest_paths[37],shortest_paths[59],shortest_paths[82],shortest_paths[99],shortest_paths[115],shortest_paths[133],shortest_paths[165],shortest_paths[188],shortest_paths[197]))
