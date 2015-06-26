#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
   setuid( 0 );
   system( "uninstall_flex.sh" );

   return 0;
}
