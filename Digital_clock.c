#include <stdio.h>
#include <windows.h>
int main()
{
   int hour,minute,second;
   int d = 1000; // we add a delay of 1000 milliseconds and we will use it in the function sleep
   
   printf( "Set time : \n" );
   scanf( "%d%d%d", &hour , &minute , &second );

   if(hour > 12 || minute > 60 || second > 60 )
   {
        printf( " ERROR ! \n " ) ;
        exit(0);
   }
   while(1) // this is an infinite loup and anything inside will repeat itself to infinity
   {
        second++ ;
        if(second>59)
        {
            minute++;
            second=0;
        }
        if(minute>59)
        {
            hour++;
            minute=0;
        }
        if(hour>12)
        {
            hour=1;
        }
        printf("\n Clock: ");
        printf( " \n %02d : %02d : %02d " , hour, minute, second); // this writes our time in this format 00:00:00
        Sleep(d) ; // the function sleep slows down the while loop and make it more like a real clock
        system("cls"); // this clears the screen
   }
}   