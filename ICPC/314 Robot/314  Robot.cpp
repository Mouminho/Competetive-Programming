#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int NORTH = 0;
const int SOUTH = 1;
const int EAST = 2;
const int WEST = 3;

struct Path
{
    int z;
    int k;
    int direction;
    int time_in_seconds;
};

const int MAXIMUM_M = 50;
const int MAXIMUM_N = 50;
bool stay[MAXIMUM_M][MAXIMUM_N];
bool wentThrough[MAXIMUM_M][MAXIMUM_N][WEST - NORTH + 1];

int movementForward(int m, int n, int step, Path p, queue<Path> &q)
{
    Path pp;
    if (p.direction == NORTH)
    {
        if (p.z - step - 1 < 0 || stay[p.z - step - 1][p.k - 1] || stay[p.z - step - 1][p.k])
        {
            return -1;
        }
        pp.z = p.z - step;
        pp.k = p.k;
    }
    else if (p.direction == SOUTH)
    {
        if (p.z + step >= m || stay[p.z + step][p.k - 1] || stay[p.z + step][p.k])
        {
            return -1;
        }
        pp.z = p.z + step;
        pp.k = p.k;
    }
    else if (p.direction == EAST)
    {
        if (p.k + step >= n || stay[p.z][p.k + step] || stay[p.z - 1][p.k + step])
        {
            return -1;
        }
        pp.z = p.z;
        pp.k = p.k + step;
    }
    else
    {
        if (p.k - step - 1 < 0 || stay[p.z][p.k - step - 1] || stay[p.z - 1][p.k - step - 1])
        {
            return -1;
        }
        pp.z = p.z;
        pp.k = p.k - step;
    }
    pp.direction = p.direction;
    if (wentThrough[pp.z][pp.k][pp.direction])
    {
        return 0;
    }
    pp.time_in_seconds = p.time_in_seconds + 1;
    wentThrough[pp.z][pp.k][pp.direction] = true;
    q.push(pp);
    return 1;
}

bool turn(bool right, Path p, queue<Path> &q)
{
    Path pp;
    if (p.direction == NORTH)
    {
        pp.direction = right ? EAST : WEST;
    }
    else if (p.direction == SOUTH)
    {
        pp.direction = right ? WEST : EAST;
    }
    else if (p.direction == EAST)
    {
        pp.direction = right ? SOUTH : NORTH;
    }
    else
    {
        pp.direction = right ? NORTH : SOUTH;
    }
    if (wentThrough[p.z][p.k][pp.direction])
    {
        return false;
    }
    pp.z = p.z;
    pp.k = p.k;
    pp.time_in_seconds = p.time_in_seconds + 1;
    wentThrough[pp.z][pp.k][pp.direction] = true;
    q.push(pp);
    return true;
}

int begining_forward_movement(int m, int n, int b_1, int b_2, int e_1, int e_2, int direction_dir)
{
    Path p;
    p.z = b_1;
    p.k = b_2;
    p.direction = direction_dir;
    p.time_in_seconds = 0;
    queue<Path> q;
    wentThrough[b_1][b_2][direction_dir] = true;
    q.push(p);
    while (!q.empty())
    {
        p = q.front();
        q.pop();
        if (p.z == e_1 && p.k == e_2)
        {
            return p.time_in_seconds;
        }
        turn(false, p, q); // turn left
        turn(true, p, q);  // turn right
        for (int step = 1; step <= 3; step++)
        {
            if (movementForward(m, n, step, p, q) == -1)
            {
                break;
            }
        }
    }
    return -1;
}

int main()
{
    while (true)
    {
        int m, n;
        cin >> m >> n;
        if (m == 0 && n == 0)
        {
            break;
        }
        for (int j = 0; j < m; j++)
        {
            for (int i = 0; i < n; i++)
            {
                wentThrough[j][i][NORTH] = wentThrough[j][i][SOUTH] = wentThrough[j][i][EAST] = wentThrough[j][i][WEST] = false;
                cin >> stay[j][i];
            }
        }
        int b_1, b_2, e_1, e_2;
        cin >> b_1 >> b_2 >> e_1 >> e_2;
        string s;
        cin >> s;
        int direction_dir;
        if (s[0] == 'n')
        {
            direction_dir = NORTH;
        }
        else if (s[0] == 's')
        {
            direction_dir = SOUTH;
        }
        else if (s[0] == 'e')
        {
            direction_dir = EAST;
        }
        else
        {
            direction_dir = WEST;
        }
        cout << begining_forward_movement(m, n, b_1, b_2, e_1, e_2, direction_dir) << endl;
    }
    return 0;
}