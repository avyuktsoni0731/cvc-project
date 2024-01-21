#include<iostream>
using namespace std;
int main()
{
	int count = 0, num, a = 0, b = 0 , c ;
	while (count < 100)
	{
		cout << "Enter a no. ";
		cin >> num;
		if (num >= a)
		{    
		if (num > a)
		{
		    b = a;
			a = num;
			count = count + 1 ;
		}
		else if ( num = a)
		{
			a = a;
			count = count + 1 ;
		}
		
		}
		 else if ( num < a)
	    {
	    	if( num > b)
	    	{
	    	b = num;
	    	count = count + 1;
	        }
			else  
	        count = count + 1;
	        
        }  
	}
	cout << "The first highest no. is ";
	cout << a << endl;
	cout << "The second highest no. is " << b << endl;
	return 0;
}

