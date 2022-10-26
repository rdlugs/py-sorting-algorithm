class QuickSort:

    def __init__(self, array):
        self.array = array

    def sort(self):
        array_aux = self.array.copy()
        
        self.__do_quick_sort(array_aux, 0, len(self.array) - 1)
        return array_aux

    def __do_quick_sort(self, array, start, end):
        if start < end:
            partition = self.__partition(array, start, end)
            self.__do_quick_sort(array, start, partition - 1)
            self.__do_quick_sort(array, partition + 1, end)
            

    def __partition(self, array, start, end):
        pivot = array[end]
        low = start

        for x in range(start, end):
            if array[x] <= pivot:
                temp = array[low]
                array[low] = array[x]
                array[x] = temp

                low += 1

        array[end] = array[low]
        array[low] = pivot

        return low

