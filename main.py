import sys
import os
from strategy.sort_strategy import SortStrategy
from algorithms.quick_sort import QuickSort
from algorithms.merge_sort import MergeSort
from algorithms.bubble_sort import BubbleSort

strategy_selected = None
array_selected = []

def display_choices():
    global strategy_selected
    global array_selected
    
    print("Select Sorting Algorithm")
    print("------------------------------------")
    print("[1] Quick Sort")
    print("[2] Merge Sort")
    print("[3] Bubble Sort")
    print("\n")

    strategy_selected = int(input("Select Sorting: "))
    range_elements = int(input("Enter Number of Elements: "))

    for i in range(0, range_elements):
        ele = int(input("Enter Element {}: ".format(i)))
        array_selected.append(ele)


def main():
    global strategy_selected
    global array_selected

    os.system('cls')
    display_choices()

    if strategy_selected == 1:
        title = "Quick Sort"
        sort = SortStrategy(QuickSort)
    elif strategy_selected == 2:
        title = "Merge Sort"
        sort = SortStrategy(MergeSort)
    elif strategy_selected == 3:
        title = "Bubble Sort"
        sort = SortStrategy(BubbleSort)
    else:
        title = "Quick Sort"
        sort = SortStrategy(QuickSort)

    sorted_array = sort.do_sort(array_selected)
    print("\nAlgorithm: {}".format(title))
    print("Unsorted List: {}".format(array_selected))
    print("Sorted List: {}".format(sorted_array))

    print("\n")
    is_continue = input("Try Another?[Y/N]: ")

    if is_continue.lower() == 'y':
        strategy_selected = None
        array_selected = []
        main()

if __name__ == '__main__':
	main()