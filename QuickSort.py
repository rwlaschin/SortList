def quickSort(array, indexL, indexR):
   pivot = _partitioning(array, indexL, indexR, 1)
   if pivot-1 > indexL:
      quickSort(array, indexL, pivot-1)
   if pivot+1 < indexR:
      quickSort(array, pivot+1, indexR)
 
def _partitioning(array, indexL, indexR, direction):
   while indexL != indexR:
      if array[indexL] > array[indexR]:
         array[indexL], array[indexR] = array[indexR], array[indexL]
         return _partitioning(array, indexL, indexR, abs(direction-1) )
      else:
         if direction:
            indexR -= 1
         else:
            indexL += 1
   return indexL