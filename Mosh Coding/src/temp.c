

#include <stdio.h>
#include <time.h>


int main(void)
{
    int mat1[500][500];
    int mat2[500][500];
    int mat3[500][500];
    for(int i=0; i<500; i++){
        for(int j=0; j<500; j++){
            mat1[i][j] = 10;
            mat2[i][j] = 40;
        }
    }

    long long diff;
    struct timespec start, end;

    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &start);

    for(int i=0; i<500; i++)
    {
        for(int j=0; j<500; j++)
        {
            int sum=0;
            for(int k=0; k<500; k++)
                sum = sum + mat1[i][k] * mat2[k][j];
            mat3[i][j] = sum;
        }
    }

    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &end);

    diff = end.tv_nsec - start.tv_nsec;

    printf("elapsed time = %lld nanoseconds\n", diff);
   
    // for(int i=0; i<3; i++)
    // {
    //     for(int j=0; j<3; j++)
    //         printf("%d\t", mat3[i][j]);
    //     printf("\n");
    // }
}
