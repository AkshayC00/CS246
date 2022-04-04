#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int global_depth;
int capacity;
int n = (1<<global_depth);

struct bucket{
    int cap;
    int local_depth;
    set<int> arr;
    bucket(){
        cap = capacity;
    }
};

vector<bucket*> dir(n);

int hf(int value)
{
    return value % (1<<global_depth);
}

// create function for bucket split and check local_depth<global_depth
void split_bucket(int i)
{
    vector<int> temp;
    for(auto it : dir[i]->arr)
    {
        // remove from the set and store in vector
        temp.push_back(it);
        dir[i]->arr.erase(it);
    }
    // put values back in correct buckets
    for(auto it : temp)
    {
        dir[hf(it)]->arr.insert(it);
    }
};

void update_directory(int i)
{
    global_depth++;
    n = (1<<global_depth);
    dir.resize(n);
    for(int j=n/2;j<n;j++)
    {
        dir[j] = dir[j-n/2];
        dir[j]->local_depth=dir[j-n/2]->local_depth;
    }
    dir[i+n/2] = new bucket;
    // split the bucket
    split_bucket(i);
    // update local depth
    dir[i]->local_depth++;
    dir[i+n/2]->local_depth++;
};


void insert(int value)
{
    int i = hf(value);
    if(dir[i]->arr.size()<capacity)
    {
        dir[i]->arr.insert(value);
    }
    else
    {
        if(dir[i]->local_depth<global_depth)
        {
            // only split the bucket
            dir[i+n/2] = new bucket;
            split_bucket(i);
            dir[i+n/2]->local_depth=n-1;
        }
        else{
            update_directory(i);
        }
    }
};

void print_status()
{
    cout << "Global Depth: ";
    cout << global_depth << endl;
    int count=0;
    // for(int i=0;i<n/2;i++)
    // {
    //     if(dir[i]->local_depth==global_depth)
    //         count+=2;
    //     else    
    //         count+=1;
    // }
    cout << "Number of buckets: ";
    cout << count << endl;
    for(int i=0;i<n;i++)
    {
        cout << hf(i) << " - ";
        cout << "Number of keys: " << dir[i]->arr.size() << " ";
        cout << "Local Depth: " << dir[i]->local_depth<< endl;
    }
}

int main()
{
    // cin >> global_depth;
    // cin >> capacity;
    global_depth=1;
    capacity=2;
    n = (1<<global_depth);
    // cout << n;
    for(int i=0;i<n;i++)
    {
        dir[i] = new bucket;
        dir[i]->local_depth=global_depth;
    }
    // cout << dir[1]->arr.empty();
    insert(4);
    insert(2);
    insert(1);
    insert(6);
    print_status();

}