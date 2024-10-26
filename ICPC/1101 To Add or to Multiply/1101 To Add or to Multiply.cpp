#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

const int MAX_vlaue = 100;
// MAX_value as in the problem definition ees less than 100
const int LIM = 1000000000;
int adjazent_Matrix[MAX_vlaue][MAX_vlaue];
// Adjacent Matrix to represent the graph
int N;
// number of cities
int R;
// number of root sigments
int S;
// starting city
int D;
// destination city 
int T;
// number of tourists

void Max_Of_Min() {
    // Dynamic prog to find the maximum smallest edge weight
    for(int i = 0; i < N; i++) {
        for(int ii = 0; ii < N; ii++) {
            for(int iii = 0; iii < N; iii++) {
                adjazent_Matrix[ii][iii] = max(adjazent_Matrix[ii][iii], min(adjazent_Matrix[ii][i], adjazent_Matrix[i][iii]));
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int c = 0;
    while(true) {
        cin >> N >> R;
        // read first line with 2 argument namely N and R
        if(N + R == 0) break;
        // break case directly after line when N and R are equal to 0
        
        for(int i = 0; i < N; i++) {
            // read and set the R lines after the first line in the adjazent matrix, these lines indicat the max passengers between 2 nodes
            for(int ii = 0; ii < N; ii++) {
                adjazent_Matrix[i][ii] = -LIM;
            }
            adjazent_Matrix[i][i] = 0;
        }
        
        for(int i = 0; i < R; i++) {
            // read and set last line that includes the  start city, destination city and number of tourists
            int j;
            int jj;
            int jjj;
            cin >> j >> jj >> jjj;
            j--; jj--; jjj--;
            adjazent_Matrix[j][jj] = jjj;
            adjazent_Matrix[jj][j] = jjj;
        }
        
        cin >> S >> D >> T;
        S--; D--;
        
        Max_Of_Min();
        
        cout << "Scenario #" << (++c) << "\n";
        // print number of Scenarios
        cout << "Minimum Number of Trips = " << ceil(1.0 * T / adjazent_Matrix[S][D]) << "\n\n";
        // print the Minimum number of trips to solve the current case
    }
    
    return 0;
}