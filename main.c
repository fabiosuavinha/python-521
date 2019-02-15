#include <stdio.h>
#include <stdlib.h>

void merge_sort(int * collection, int begin, int end) {

  int mid = begin + (end-begin) / 2;
  
  if ((end-begin) > 1) {
    merge_sort(collection, begin, mid);
    merge_sort(collection, mid, end);
  }

  int * left = (int *) malloc((mid-begin) * sizeof(int));
  for (int i = 0; i < (mid-begin); i++) {
    left[i] = collection[i + begin];
  }

  int * right = (int *) malloc((end-mid) * sizeof(int));
  for (int i = 0; i < (end-mid); i++) {
    right[i] = collection[i + mid];
  }

  int i = 0;
  int j = 0;
  int k = begin;

  while (i < (mid-begin) && j < (end-mid)) {
    if (left[i] <= right[j]) {
      collection[k++] = left[i++];
    } else {
      collection[k++] = right[j++];
    }
  }

  while (i < (mid-begin)) {
    collection[k++] = left[i++];
  }

  while (j < (end-mid)) {
    collection[k++] = right[j++];
  }

  free(left);
  free(right);
}

int main() {

  int v[] = { 2, 5, 1, 3, 9, 3, 6, 4 };
  int n = sizeof(v) / sizeof(v[0]);

  merge_sort(v, 0, n);

  for (int i = 0; i < n; i++) {
    printf("%d\n", v[i]);
  }

  return 0;
}