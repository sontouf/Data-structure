#include <stdio.h>
void quickSort(int* arr, int start, int end)
{
    if (start >= end) return; // 1개 범위기 때문에 정렬된 상태.
    int pivot_index = start;
    int i = start+1;
    int j = end;
    int temp; // 스왑용
    while (i <= j) { // 엇갈릴때까지
        while (i <= end && arr[pivot_index] >= arr[i]) i++; // 피벗보다 클 때까지.
        while (arr[pivot_index] <= arr[j] && j > start) j--; // 피벗보다 작을 떄까지
        if  (i > j) // 엇갈
        {
            temp = arr[j];
            arr[j] = arr[pivot_index];
            arr[pivot_index] = temp;
        }
        else { // 안 엇갈
            temp = arr[j];
            arr[j] = arr[i];
            arr[i] = temp;       
        }
    }
    // pivot 값은 정렬됨.
    quickSort(arr, start, j-1);
    quickSort(arr, j+1, end);
}
int main()
{
    int arr[] = {1,1,1,1,1};
    quickSort(arr, 0, 4);
    for (size_t i = 0; i < 5; i++)
    {
        printf("%d", arr[i]);
        printf("\n");
    }
    
    return 0;
}