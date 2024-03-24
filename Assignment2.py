def colored(text, color):
    """Adds ANSI color codes to the text for colorful console output.

    Args:
        text (str): The text to colorize.
        color (str): The name of the color to use.

    Returns:
        str: The colorized text using ANSI codes.
    """
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "end": "\033[0m",
    }
    return f"{colors[color]}{text}{colors['end']}"

def merge_sort(arr, start, end, depth=0):
    """Sorts an array using the merge sort algorithm recursively.

    Args:
        arr (list): The array to sort.
        start (int): The starting index of the array segment to sort.
        end (int): The ending index of the array segment to sort.
        depth (int): The current depth in the recursion tree.
    """
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(arr, start, mid, depth + 1)  # Sort the left half
        merge_sort(arr, mid, end, depth + 1)  # Sort the right half
        merge(arr, start, mid, end, depth)  # Merge the sorted halves

def merge(arr, start, mid, end, depth):
    """Merges two sorted array segments into a single sorted segment.

    Args:
        arr (list): The array containing the segments to merge.
        start (int): The starting index of the left segment.
        mid (int): The ending index of the left segment (and start of the right).
        end (int): The ending index of the right segment.
        depth (int): The current depth in the recursion tree, for formatting.
    """
    # Displaying the segment of the array to be merged
    merge_info = f" Depth {depth}: Merging {' '.join(f'{x:2}' for x in arr[start:end])} "
    after_merge_info = f" After Merge: {' '.join(f'{x:2}' for x in arr[start:end])} "
    box_length = max(len(merge_info), len(after_merge_info))

    print(f"{' ' * depth * 4}{colored('┌' + '─' * box_length + '┐', 'cyan')}")
    print(f"{' ' * depth * 4}{colored('│', 'cyan')}{merge_info}{' ' * (box_length - len(merge_info))}{colored('│', 'cyan')}")

    left = arr[start:mid]
    right = arr[mid:end]
    k = start
    i = j = 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while start + i < mid:
        arr[k] = left[i]
        i += 1
        k += 1
    
    while k < end:
        arr[k] = right[j]
        j += 1
        k += 1

    # Displaying the segment of the array after merging
    print(f"{' ' * depth * 4}{colored('│', 'cyan')}{after_merge_info}{' ' * (box_length - len(after_merge_info))}{colored('│', 'cyan')}")
    print(f"{' ' * depth * 4}{colored('└' + '─' * box_length + '┘', 'cyan')}\n")

def main():
    """Main function to execute the merge sort algorithm."""
    arr = [int(x) for x in input("Enter numbers separated by space: ").split()]
    print("\nOriginal array:", colored(' '.join(f'{x:2}' for x in arr), 'yellow'))
    print(colored("\nStarting Merge Sort...\n", "green"))
    merge_sort(arr, 0, len(arr))
    print(colored("\nMerge Sort Completed.", "green"))
    print("Sorted array:", colored(' '.join(f'{x:2}' for x in arr), 'yellow'))

if __name__ == "__main__":
    main()