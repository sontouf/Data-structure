// 41523 -> 14523 -> 14253 -> 14235 -> 12435 -> 12345 5 4 3 2 1
// 스왑 있고.
#include <stdio.h>
void bubbleSort(int* arr, int arrSize)
{
    int temp; // 스왑용
    for (size_t i = 0; i < arrSize; i++)
    {
        // 스왑을 하다보면 결국 맨뒤에 큰 수가 오게 되므로 arrsize-1 만큼만 반복하면 된다.
        for (size_t j = 0; j < (arrSize-1) - i; j++)
        {
            if (arr[j] > arr[j+1])
            {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }  
        }
    }
    
}
int main()
{
    int arr[] = {1,10,5,8,7,6,4,3,2,9};
    bubbleSort(arr, 10);
    for (size_t i = 0; i < 10; i++)
    {
        printf("%d", arr[i]);
        printf("\n");
    }
    
    return 0;
}