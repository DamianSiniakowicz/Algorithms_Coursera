#include <vector>
#include <array>
#include <map>
#include <iostream>
#include <fstream>
#include <iterator>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

/*

dynamic programming algorithm
construct 2D table : set of nodes in path, destination
base case : set of two elements, value equals the dist between them 
recurrence : shortest tour of elements in set excluding the destination plus distance from destination of shorter tour to final destination
loop over set sizes from 2 through 25
loop over all sets of the current size
loop over all destinations in the current set (the source node may not serve as the destination)
after table is filled out, loop over all problems of size 25, and add to each the distance from its destination node back to the source node.

need to generate combinations
use a map for the set/destination->distance table. (what kind of sequence objects can an array use as a key)


*/

/*
combination generating recursive algorithm
int k = 5; // k will range from 2 through 25
vector<array<int,k>> get_combos(range,choose_x){
	// only need k-1 items, then tack on 1.
	// need a forloop over 1..k-1
	vector <array<int,k>> combos;
	int start = 0;
	for (int el_id = 1; el_id < k; el_id++){
		// loop over all choices for first el
	}
}
<array<int,k> get_combo(range,choose_x,start_index){ // range = {2...25}, 
	
	for first_index 
	// choose element from range[start_index:range.size()-1]
	return {element, get_combo(range,choose_x-1,start_index = range.find(element)+1)} 			
}
*/

int main(){
	// put nodes in a vector
	ifstream infile("/home/damian/Dropbox/Algorithms/tsp_data.txt");
	vector<array<double,2>> node_coordinates;
	if (infile.good()){
		string skip_first_line;
		getline(infile,skip_first_line);
		int break_index = 10;
		for (int i = 1; i < 26; i++){
			string next_node;
			getline(infile,next_node);
			int x;
			int y;
			x = stod(next_node.substr(0,break_index));
			y = stod(next_node.substr(break_index+1));
			array<double,2> x_y = {x,y};
			node_coordinates.push_back(x_y);
		}
	}
	map<array<int,2>,double> edge_lengths;
	// put edges in a map
	for (int A = 0; A < 25; A++){
		for (int B = A+1; B < min(A+11,25); B++){
			array<double,2> first = node_coordinates[A];
			array<double,2> second = node_coordinates[B];
			array<int,2> f_s_pair = {A,B};
			array<int,2> s_f_pair = {B,A};
			double first_x = first[0];
			double first_y = first[1];
			double second_x = second[0];
			double second_y = second[1];
			double dist = sqrt(pow(first_x-second_x,2.0) + pow(first_y-second_y,2.0))
			edge_lengths[f_s_pair] = dist;
			edge_lengths[s_f_pair] = dist;
		}
	}
	// loop over set sizes
	for (int set_size = 2; set_size < 26; set_size++){
		// loop over sets of that size
			
	}
	

	// loop over destinations
}
