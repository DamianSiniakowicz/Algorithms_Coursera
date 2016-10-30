#include <array>
#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <map>
#include <iterator>
#include <vector>
#include <fstream>

using namespace std;

class UnionFind{
public:
	map<int,int> follower_to_leader;
	map<int,vector<int>> leader_to_followers;
	UnionFind();

	bool same_leader(int first, int second);
	void merge_groups(int first, int second);
};
UnionFind::UnionFind(){}
bool UnionFind::same_leader(int first, int second){
	if (follower_to_leader[first] == follower_to_leader[second]){
		return true;
	}
	else{
		return false;
	}
}
void UnionFind::merge_groups(int first, int second){
	int leader_1 = follower_to_leader[first];
	int leader_2 = follower_to_leader[second];
	if (leader_to_followers[leader_1].size() > leader_to_followers[leader_2].size()){
		// leader 2's followers switch allegiance
		vector<int> converts = leader_to_followers[leader_2];
		for(int i = 0; i < converts.size(); i++){
			leader_to_followers[leader_1].push_back(converts[i]);
			follower_to_leader[converts[i]] = leader_1;
		}
		leader_to_followers.erase(leader_2);
	}
	else{
		// leader 1's followers switch allegiance
		vector<int> converts = leader_to_followers[leader_1];
		for(int i = 0; i < converts.size(); i++){
			leader_to_followers[leader_2].push_back(converts[i]);
			follower_to_leader[converts[i]] = leader_2;
		}
		leader_to_followers.erase(leader_1);
	}
}

string removeSpaces(string input)
{	
  input.erase(remove(input.begin(),input.end(),' '),input.end());
  return input;
}

int hammingDistance(string first, string second){
	int difference = 0;
	for (int i=0; i<24; i++){
		if (first[i] != second[i]){
			difference += 1;		
			}
		}
	return difference;
}

class Vertex_Pair
{
  public:
    Vertex_Pair() {};                                      //default constructor
    Vertex_Pair(int x, int y, int hamming) { first = x; second = y; dist = hamming; }    //constructor
    bool operator<(const Vertex_Pair&) const;              //overloaded < operator

    int get_first() const { return first; }             //accessor methods
    int get_second() const { return second; }
    int get_dist() const { return dist; }

  private:
    int first, second, dist;                                 //data fields
};

bool Vertex_Pair::operator<(const Vertex_Pair& right) const
{
	if (dist == right.dist){
		if (rand() % 2 == 0){
			return true;}
		else {
			return false;}
		}
	else {
		return (dist > right.dist);}
}



int main(){
	
	srand(static_cast<int>(time(0)));
	/*
	Vertex_Pair A = Vertex_Pair(1,2,8);
	Vertex_Pair B = Vertex_Pair(2,3,6);
	Vertex_Pair C = Vertex_Pair(3,4,6);

	if (A < B){
		cout << "good" << endl; }
	else {
		cout << "something's wrong" << endl;}
	
	if (B < A){
		cout << "bad" << endl;}
	else {
		cout << "good" << endl;}
	
	int count = 100;
	int C_won = 0;
	int B_won = 0;
	while (count > 0){
		if (C < B){
			B_won++;}
		else{
			C_won++;}
		count--;
	} 
	cout << C_won << " C" << endl;
	cout << B_won << " B" << endl;


	priority_queue <Vertex_Pair> pair_heap; 

	pair_heap.push(B);
	pair_heap.push(A);
	pair_heap.push(C);

	for(int i = 0; i < 3; i++){
		cout << pair_heap.top().get_first() << endl;
		pair_heap.pop();
	}

	*/
	ifstream infile("/home/jan/Dropbox/Algorithms/cluster_2_data.txt");

	//ifstream infile("/home/damian/Dropbox/Algorithms/cluster_test_data.txt");

	int num_vertices;
	int representation_length;

	if (infile.good())
	{
		string sLine;
		getline(infile, sLine);

		int break_point;
		break_point = sLine.find(' ');
		num_vertices = stoi(sLine.substr(0,break_point));
		representation_length = stoi(sLine.substr(break_point));


	}

	string vertex_array[num_vertices];

	for (int i = 0; i < num_vertices; i++){
		string next_line;
		getline(infile,next_line);
		next_line = removeSpaces(next_line);
		vertex_array[i] = next_line;
		}
	infile.close();

	priority_queue <Vertex_Pair> pair_heap;

	vector<array<int,2>> zero_neigh, one_neigh, two_neigh;

	unsigned long long int counter = 0;
	for (int i = 0; i<(num_vertices-1); i++){
		for (int j=i+1; j<num_vertices; j++){
			int dist = hammingDistance(vertex_array[i],vertex_array[j]);
			/*
			if (dist < 3){
				Vertex_Pair v_pair = Vertex_Pair(i,j,dist);
				pair_heap.push(v_pair);
			}
			*/
			if (dist == 2){
				array<int,2> edge = {i,j};
				two_neigh.push_back(edge);}
			else if (dist == 1){
				array<int,2> edge = {i,j};
				one_neigh.push_back(edge);}
			else if (dist == 0){
				array<int,2> edge = {i,j};
				zero_neigh.push_back(edge);}
			if (counter % 1000000000 == 0){ // 100000000 needs to be changed depending on the input file.
				cout << "pair: " << counter << endl;}
			counter++;
			}
		}


	UnionFind nodes;
	for(int i = 0; i < num_vertices; i++){
		nodes.follower_to_leader[i] = i;
		vector<int> followers = {i};
		nodes.leader_to_followers[i] = followers;
	}

	ofstream answer;
	answer.open("/home/jan/Dropbox/answer.txt");
	
	for (int i = 0; i < zero_neigh.size(); i++){
		int first = zero_neigh[i][0];
		int second = zero_neigh[i][1];
		if (not nodes.same_leader(first,second)){
			nodes.merge_groups(first,second);}}
        for (int i = 0; i < one_neigh.size(); i++){ 
                int first = one_neigh[i][0]; 
                int second = one_neigh[i][1]; 
                if (not nodes.same_leader(first,second)){
                        nodes.merge_groups(first,second);}}
        for (int i = 0; i < two_neigh.size(); i++){ 
                int first = two_neigh[i][0]; 
                int second = two_neigh[i][1]; 
                if (not nodes.same_leader(first,second)){
                        nodes.merge_groups(first,second);}}


	/*
	while(pair_heap.size() > 0){
		Vertex_Pair edge = pair_heap.top();
		pair_heap.pop();
		int first = edge.get_first();
		int second = edge.get_second();
		if (not nodes.same_leader(first,second)) {
			nodes.merge_groups(first,second);		
		}
	}
	*/
	answer << nodes.leader_to_followers.size();
	answer.close();
	return 0;


	// union-find TIME
	// need to put all vertices into a union-find as their own leader
	// while we're popping off edges with length < 3. (as soon as we hit an edge of length 3, return number of clusters)
	// check if both vertices have the same leader, if not, merge their groups
	
	
	return 0;	
	}

	/*
	for (int i = 0; i < num_edges; i++){
		string next_line;
		getline(infile,next_line);
		next_line = removeSpaces(next_line);
		for (int i = 0; i<23; i++){
			cout << (next_line[i] != next_line[i+1]) << endl;}*/

	
	
	
	/*
	char alfred[6] = {'a','l','f','r','e','d'};
	char joseph[6] = {'j','o','s','e','p','h'};
	for (int i=0; i<6; i++){
		if (joseph[i] == alfred[i]){
			cout << "ssame" << endl;}
		else {
			cout << "diff" << endl;}
	}
	string first = "10";
	string second = "01";
	//cout << (first ^ second) << endl;	*/
	
/*
Need to make a union-find data structure and throw all the vertices in there.
Then start popping stuff off the heap and merging groups in the UF.
When we pop off a pair with length > 2, stop


Need to get a priority queue working and store all pairs,distance in the queue

Strategy : make an array, store character arrays inside it.

three possible representations for each vertex
	an integer array	
	a string
	a binary string
of course, all three would be stored in an array together with the rest of the vertices

choose the representation with the fastest hamming distance computations

double loop over the array, get all edge lengths. store in a heap.
put all vertices in a union-find df
etc.
*/

/*
		cout << "gonna get the first vertex" << endl;
		string first_vertex;
		getline(infile,first_vertex);
		cout << first_vertex << endl;
		string clean_up = removeSpaces(first_vertex);
		cout << clean_up << endl;
		*/
