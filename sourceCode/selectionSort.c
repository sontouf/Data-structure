// 선택정렬은 가장 작은 거 선택해서 본 범위의 왼쪽 끝 숫자랑 스왑.
// 반복할수록 범위가 하나씩 줄어들겠지.
// 41523 -> 14523 -> 12543 -> 12345
#include <stdio.h>
void selectionSort(int* arr, int arrSize)
{
    int min; // 가장 작은 데이터를 담을 거
    int min_index = 0; // 주어진 배열에서 범위 내 가장 작은 값의 위치.
    int temp; // 스왑할 떄 데이터를 담은 공간.
    // 반복(1)작은거 찾기 -> 범위의 왼쪽 값과 스왑 -> 반복(2)다음 범위로 반복

    for (size_t i = 0; i < arrSize; i++)
    {
        min = 9999;
        for (size_t j = i; j < arrSize; j++)
        {
            if (arr[j] < min)
            {
                min = arr[j];
                min_index = j;
            }
        }
        temp = arr[i];
        arr[i] = min;
        arr[min_index] = temp;
    }
}
int main()
{
    int arr[] = {1,10,5,8,7,6,4,3,2,9};
    selectionSort(arr, 10);
    for (size_t i = 0; i < 10; i++)
    {
        printf("%d", arr[i]);
        printf("\n");
    }
    
    return 0;
}