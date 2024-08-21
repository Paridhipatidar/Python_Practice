def cal_s_and_a(numbers):
    numbers = [float(num) for num in numbers]    
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return total_sum, average
def main():
    file_path = input("Enter the path to the text file: ")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            numbers = content.split(',')
            total_sum, average = cal_s_and_a(numbers)
            print(f"Sum of the numbers: {total_sum}")
            print(f"Average of the numbers: {average}")
    except FileNotFoundError:
        print("File not found. Please make sure you enter the correct file path.")
if __name__ == "__main__":
    main()
 