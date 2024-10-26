#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    // function main to solve the 'Lunch in Grid City' problem
    int Case;
    // variable case that indicate the number of cases
    std::cin >> Case;
    // first line input to be the number of cases
    for (int i = 0; i < Case; i++) {
        // outer for loop to read the input
        int s, a, f;
        // variables s, a and f indicate number of streets, avenues and friends
        std::cin >> s >> a >> f;
        // assign values to variables s, a and f 
        if (s <= 1000) {
            // s must be less than 1001
            if (a <= 1000) {
                // a must be less that 1001
                if (f <= 50000 && f > 0) {
                    // f must be between 1 and 50000
                    std::vector<int> streets;
                    // vector streets
                    std::vector<int> avenues;
                    // vector avenues
                    for (int j = 0; j < f; j++) {
                        // inner for loop to isolate streets and avenues
                        int ss, aa;
                        // variables ss and aa , ss values of street coordinations, aa values of avenues coordinations
                        std::cin >> ss >> aa;
                        // assign values to ss and aa
                        streets.push_back(ss);
                        avenues.push_back(aa);
                    }
                    std::sort(streets.begin(), streets.end());
                    // sorting streets asc
                    std::sort(avenues.begin(), avenues.end());
                    // sorting avenues dec
                    if (f % 2) {
                        // we take the middle value of streets and avenues and match them together to get the wanted outputs
                        std::cout << "(Street: " << streets[f / 2] << ", Avenue: " << avenues[f / 2] << ")" << std::endl;
                    } else {
                        // we take the middle value of streets and avenues and match them together to get the wanted outputs
                        std::cout << "(Street: " << streets[(f - 1) / 2] << ", Avenue: " << avenues[(f - 1) / 2] << ")" << std::endl;
                    }
                }
            }
        }
    }
    return 0;
}