class BubbleSort:

    def __init__(self, array):
        self.array = array

    def sort(self):
        array_aux = self.array.copy()
        self.__do_bubble_sort(array_aux)
        return array_aux


    
    def __do_bubble_sort(self, array_aux):
        array_len = len(array_aux)
        for i in range(0, array_len):
            swapped = False
            for j in range(0, array_len - i -1):
                if j+1 <= array_len - 1:
                    current_val = array_aux[j]

                    if(current_val > array_aux[j+1]):
                        array_aux[j] = array_aux[j+1]
                        array_aux[j+1] = current_val
                        swapped = True

            if(not swapped): return 