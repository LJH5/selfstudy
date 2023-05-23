# include <iostream>

using namespace std;

void def(double *ptr)
{
     if (ptr != nullptr)
    {
        cout << *ptr << endl;
    }
    else
    {
        cout << "Null Pointer" << endl;
    }
    
}

int main()
{
    double *ptr{ nullptr };

    def(ptr);
    def(nullptr);

    double d = 3.14;
    def(&d);

    return 0;
}