def read_file_with_handling():
    while True:
        filename = input("Enter the filename you want to read (or 'quit' to exit): ")
        
        if filename.lower() == 'quit':
            print("Goodbye!")
            break
        
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print("\nFile content:")
                print(content)
                break
                
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist.")
        except PermissionError:
            print(f"Error: You don't have permission to read '{filename}'.")
        except IsADirectoryError:
            print(f"Error: '{filename}' is a directory, not a file.")
        except UnicodeDecodeError:
            print(f"Error: Could not decode '{filename}' as a text file.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    read_file_with_handling()
