import numpy as np
arr = None
class numpy_analyzer():

    def create_array(self):
        try:
            print("Select the type of array to create: ")
            print("1. For 1D Array ")
            print("2. For 2D Array ")
            print("3. For 3D Array ")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                elements = input("Enter the elements: ").split()
                elements = list(map(int,elements))
                arr = np.array(elements)
                print(arr)
                return arr

            elif choice == 2:
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of cols: "))
                elements = input(f"Enter the {rows*cols} elements for the array separated by space:  ").split()
                elements = list(map(int,elements))
                arr = np.array(elements).reshape((rows,cols))
                print(arr)
                return arr

            elif choice == 3:
                layer = int(input("Enter number of layer: "))
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of cols: "))
                elements = input(f"Enter the {layer*rows*cols} elements for the array separated by space:  ").split()
                elements = list(map(int,elements))
                arr = np.array(elements).reshape((layer,rows,cols))
                print(arr)
                return arr

            else:
                print("Invalid Input!")
        except:
            print("Something went wrong!")

    def array_op(self,arr):
        try:
            print("Choose an operation: ")
            print("1. Indexing of Elements")
            print("2. Slicing of Elements")
            print("3. Go back to Main Menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                if arr.ndim == 1:
                    index = int(input("Enter the index: "))
                    print(f"Elements: {arr[index]}\n")

                elif arr.ndim == 2:
                    row = int(input("Enter the row index: "))
                    col =int(input("Enter the column index: "))
                    print(f"Elements: {arr[row,col]}\n")


                elif arr.ndim == 3:
                    layer = int(input("Enter the layer index: "))
                    row = int(input("Enter the row index: "))
                    col =int(input("Enter the column index: "))
                    print(f"Elements: {arr[layer,row,col]}\n")

            elif choice == 2:
                if arr.ndim == 1:
                    start = int(input("Enter the start index: "))
                    end = int(input("Enter the end index: "))
                    print("Sliced Array: ")
                    print(arr[start:end])

                elif arr.ndim == 2:
                    row_start = int(input("Enter the row start index: "))
                    row_end = int(input("Enter the row end index: "))
                    col_start = int(input("Enter the column start index: "))
                    col_end = int(input("Enter the column end index: "))
                    print("Sliced Array: ")
                    print(arr[row_start:row_end, col_start:col_end])

                elif arr.ndim == 3:
                    layer_start = int(input("Enter the layer start index: "))
                    layer_end = int(input("Enter the layer end index: "))
                    row_start = int(input("Enter the row start index: "))
                    row_end = int(input("Enter the row end index: "))
                    col_start = int(input("Enter the column start index: "))
                    col_end = int(input("Enter the column end index: "))
                    print("Sliced Array: ")
                    print(arr[layer_start:layer_end,row_start:row_end, col_start:col_end])

            elif choice == 3:
                print("Returning to the main menu!\n")

            else:
                print("Invalid Input")
        except:
            print("Enter a valid Indexing or (start-end) Range!")

    def math_op(self,arr):
        try:
            print("Choose a mathematical operation:")
            print("1. Addition of two arrays")
            print("2. Subtraction of two arrays")
            print("3. Multiplication of two arrays")
            print("4. Division of two arrays")

            choice = int(input("Enter your choice: "))

            if choice == 1 or choice == 2 or choice == 3 or choice == 4:
                elements = input(f"Enter the same-size array elements ({arr.size} elements separated by space): ").split()
                elements = list(map(int, elements))

                if len(elements) != arr.size:
                    print(f"Please enter exactly {arr.size} elements!")
                    return

                arr2 = np.array(elements).reshape(arr.shape)

                print("\nOriginal Array:")
                print(arr)

                print("\nSecond Array:")
                print(arr2)

                if choice == 1:
                    print("\nResult of Addition:")
                    print(np.add(arr, arr2),"\n")

                elif choice == 2:
                    print("\nResult of Subtraction:")
                    print(np.subtract(arr, arr2),"\n")

                elif choice == 3:
                    print("\nResult of Multiplication:")
                    print(np.multiply(arr, arr2),"\n")

                elif choice == 4:
                    if np.any(arr2 == 0):
                        print("Division by zero is not allowed!")
                    else:
                        print("\nResult of Division:")
                        print(np.divide(arr, arr2),"\n")

            else:
                print("Invalid Input!")

        except:
            print("Please enter valid numeric values!")

    def combine_split(self,arr):
        try:
            print("Choose an operation:")
            print("1. Combine Arrays")
            print("2. Split Array")
            print("3. Go back to Main Menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                elements = input(f"Enter the same-size array elements ({arr.size} elements separated by space): ").split()
                elements = list(map(int, elements))

                if len(elements) != arr.size:
                    print(f"Please enter exactly {arr.size} elements!")
                    return

                arr2 = np.array(elements).reshape(arr.shape)

                print("\nOriginal Array:")
                print(arr)

                print("\nSecond Array:")
                print(arr2)

                combined_array = np.vstack((arr, arr2))
                print("\nCombined Array:")
                print(combined_array)

            elif choice == 2:
                splits_num = int(input("Enter the number of splits: "))
                if splits_num <= 0 or splits_num > arr.shape[0]:
                    print("Invalid number of splits!")
                    return
                
                elements = np.array_split(arr, splits_num, axis=0)
                print("\nSplit Arrays:")
                i = 1
                for split in elements:
                    print(f"Split Array {i}:")
                    print(split)
                    i += 1
                    

            elif choice == 3:
                print("Returning to the main menu!\n")

            else:
                print("Invalid Input!")

        except:
            print("Something went wrong!")

    def search_sort_filter(self, arr):
        try:
            print("Choose an operation:")
            print("1. Search for an Element")
            print("2. Sort the Array")
            print("3. Filter the Array")
            print("4. Go back to Main Menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                element = int(input("Enter the element to search for: "))
                indices = np.argwhere(arr == element)
                if indices[0].size > 0:
                    print(f"Element {element} found at indices: {indices}\n")
                else:
                    print(f"Element {element} not found in the array.\n")

            elif choice == 2:
                sorted_array = np.sort(arr, axis=None)
                print("\nSorted Array:")
                print(sorted_array)
                print("(Sorting applied row-wise.)\n")

            elif choice == 3:
                print("\nChoose a filter condition:")
                print("1. Greater than")
                print("2. Less than")
                print("3. Equal to")

                choice = int(input("Enter your choice: "))

                value = int(input("Enter the comparison value: "))

                if choice == 1:
                    filtered = arr[arr > value]

                elif choice == 2:
                    filtered = arr[arr < value]

                elif choice == 3:
                    filtered = arr[arr == value]
                else:
                    print("Invalid filter choice!")
                    return
                print("\nOriginal Array:")
                print(arr)
                print("\nFiltered Array:")
                print(filtered)

            elif choice == 4:
                print("Returning to the main menu!\n")

            else:
                print("Invalid Input!")

        except:
            print("Something went wrong!")

    def statistics(self, arr):
        try:
            print("Choose a statistical operation:")
            print("1. Sum of Elements")
            print("2. Mean of Elements")
            print("3. Median of Elements")
            print("4. Go back to Main Menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                elements = np.sum(arr)
                print(f"\nSum of the array: {elements}\n")

            elif choice == 2:
                elements = np.mean(arr)
                print(f"\nMean of the array: {elements}\n")

            elif choice == 3:
                elements = np.median(arr)
                print(f"\nMedian of the array: {elements}\n")

            elif choice == 4:
                print("Returning to the main menu!\n")

            else:
                print("Invalid Input!")

        except:
            print("Something went wrong!")
        


obj = numpy_analyzer()
def main_menu():

        while True:
            print("Welcome to the Numpy Analyzer!")
            print("=====================================")
            print("Choose an option:")
            print("1. Create a Numpy Array")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Compute Aggregates and Statistics")
            print("6. Exit")
            
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                arr = obj.create_array()
                if arr is not None:
                    obj.array_op(arr)
                else:
                    print("Please create an Array firsts!")

            elif choice == 2:
                if arr is not None:
                    obj.math_op(arr)
                else:
                    print("Please create an Array firsts!")

            elif choice == 3:
                if arr is not None:
                    obj.combine_split(arr)
                else:
                    print("Please create an Array firsts!")

            elif choice == 4:
                if arr is not None:
                    obj.search_sort_filter(arr)
                else:
                    print("Please create an Array Firsts!")


            elif choice == 5:
                if arr is not None:
                    obj.statistics(arr)
                else:
                    print("Please create an Array firsts!")

            elif choice == 6:
                print("Thank you for using the Numpy Analyzer!")
                break

            else:
                print("Invalid Input")


if __name__ == "__main__":
    main_menu()