class SelectionSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        array_aux = self.array.copy()
        self.__do_selection_sort(array_aux)
        return array_aux

    def __do_selection_sort(self, array):
        array_len = len(array)

        for i in range(0, array_len):
            current_val = array[i]
            smallest_val = array[i]
            smallest_index = None

            for j in range(i+1, array_len):
                if array[j] <= current_val:
                    if array[j] < smallest_val:
                        smallest_val = array[j]
                        smallest_index = j

            if smallest_index:
                array[i] = array[smallest_index]
                array[smallest_index] = current_val