// 41523 -> 14523 -> 14523 -> 14253 -> 12453 -> 12435 -> 12345
#include <stdio.h>
void quickSort(int* arr, int start, int end)
{
    if (start == end) return;
    int pivot_index = start;
    while (start < end)
    {
        while (arr[pivot_index] >= arr[start]) start++;
        while (arr[pivot_index] <= arr[end]) end--;
        
    }
    quickSort(arr, )
}
int main()
{
    int arr[] = {1,10,5,8,7,6,4,3,2,9};
    quickSort(arr, 0, 10);
    for (size_t i = 0; i < 10; i++)
    {
        printf("%d", arr[i]);
        printf("\n");
    }
    
    return 0;
}