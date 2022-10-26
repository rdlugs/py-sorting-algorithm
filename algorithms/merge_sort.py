class MergeSort:

    def __init__(self, array):
        self.array = array

    def sort(self):
        array_aux = self.array.copy()
        return self.__do_merge_sort(array_aux)
        
    def __do_merge_sort(self, array):
        array_len = len(array)

        if array_len <= 1:
            return array

        mid_idx = round(array_len / 2)
        
        left_array = array[0:mid_idx]
        left_array = self.__do_merge_sort(left_array)

        right_array = array[mid_idx:array_len]
        right_array = self.__do_merge_sort(right_array)

        return self.__merge(left_array, right_array)


    def __merge(self, left_array, right_array):
        merged_array = []

        while left_array or right_array:
            if left_array and right_array:
                if left_array[0] > right_array[0]:
                    merged_array.append(right_array.pop(0))
                else:
                    merged_array.append(left_array.pop(0))
            elif not left_array or not right_array:
                if not right_array:
                    merged_array.append(left_array.pop(0))
                else:
                    merged_array.append(right_array.pop(0))

        return merged_array