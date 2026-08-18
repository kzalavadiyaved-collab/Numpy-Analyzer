import numpy as np

array = None

while True:
    print("\nWelcome to the NumPy Analyzer!")
    print("==============================")
    print("Choose an option:")
    print("1. Create a NumPy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print("\nArray Creation:")
            print("Select the type of array to create:")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")

            ch = int(input("Enter your choice: "))

            match ch:
                case 1:
                    n = int(input("Enter the number of elements: "))
                    data = list(map(int, input(f"Enter {n} elements separated by space: ").split()))
                    array = np.array(data)
                    print("\nArray created successfully:")
                    print(array)

                case 2:
                    rows = int(input("Enter the number of rows: "))
                    cols = int(input("Enter the number of columns: "))
                    data = list(map(int, input(f"Enter {rows * cols} elements for the array separated by space: ").split()))
                    array = np.array(data).reshape(rows, cols)
                    print("\nArray created successfully:")
                    print(array)

                case 3:
                    x = int(input("Enter number of blocks: "))
                    rows = int(input("Enter number of rows: "))
                    cols = int(input("Enter number of columns: "))
                    data = list(map(int, input(f"Enter {x * rows * cols} elements separated by space: ").split()))
                    array = np.array(data).reshape(x, rows, cols)
                    print("\nArray created successfully:")
                    print(array)

                case _:
                    print("Invalid choice.")

        case 2:
            if array is None:
                print("Please create an array first.")
                continue

            print("\nMathematical Operations:")
            print("Choose a mathematical operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            op = int(input("Enter your choice: "))
            data = list(map(int, input(f"Enter {array.size} elements separated by space: ").split()))
            second = np.array(data).reshape(array.shape)

            print("\nOriginal Array:")
            print(array)
            print("\nSecond Array:")
            print(second)

            match op:
                case 1:
                    print("\nResult of Addition:")
                    print(array + second)
                case 2:
                    print("\nResult of Subtraction:")
                    print(array - second)
                case 3:
                    print("\nResult of Multiplication:")
                    print(array * second)
                case 4:
                    print("\nResult of Division:")
                    print(array / second)
                case _:
                    print("Invalid choice.")

        case 3:
            if array is None:
                print("Please create an array first.")
                continue

            print("\nCombine or Split Arrays:")
            print("Choose an option:")
            print("1. Combine Arrays")
            print("2. Split Array")

            op = int(input("Enter your choice: "))

            match op:
                case 1:
                    data = list(map(int, input(f"Enter {array.size} elements of another array to combine: ").split()))
                    second = np.array(data).reshape(array.shape)

                    print("\nOriginal Array:")
                    print(array)
                    print("\nSecond Array:")
                    print(second)
                    print("\nCombined Array (Vertical Stack):")
                    print(np.vstack((array, second)))

                case 2:
                    if array.ndim != 2:
                        print("Split is available for 2D arrays only.")
                    else:
                        parts = int(input("Enter number of parts: "))
                        print("\nSplit Array:")
                        print(np.array_split(array, parts))

                case _:
                    print("Invalid choice.")

        case 4:
            if array is None:
                print("Please create an array first.")
                continue

            print("\nSearch, Sort, and Filter:")
            print("Choose an option:")
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter values")

            op = int(input("Enter your choice: "))

            match op:
                case 1:
                    value = int(input("Enter value to search: "))
                    result = np.where(array == value)
                    print("\nSearch Result:")
                    print(result)

                case 2:
                    print("\nOriginal Array:")
                    print(array)

                    if array.ndim == 2:
                        sorted_array = np.sort(array, axis=1)
                    else:
                        sorted_array = np.sort(array)

                    print("\nSorted Array:")
                    print(sorted_array)

                case 3:
                    value = int(input("Enter threshold value: "))
                    print("\nFiltered Values:")
                    print(array[array > value])

                case _:
                    print("Invalid choice.")

        case 5:
            if array is None:
                print("Please create an array first.")
                continue

            print("\nAggregates and Statistics:")
            print("Choose an aggregate/statistical operation:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")

            op = int(input("Enter your choice: "))

            print("\nOriginal Array:")
            print(array)

            match op:
                case 1:
                    print("\nSum of Array:", np.sum(array))
                case 2:
                    print("\nMean of Array:", np.mean(array))
                case 3:
                    print("\nMedian of Array:", np.median(array))
                case 4:
                    print("\nStandard Deviation of Array:", np.std(array))
                case 5:
                    print("\nVariance of Array:", np.var(array))
                case _:
                    print("Invalid choice.")

        case 6:
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            break

        case _:
            print("Invalid choice.")
