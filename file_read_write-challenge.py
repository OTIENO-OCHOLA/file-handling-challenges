def modify_content(content):
    """Example modification function - converts text to uppercase"""
    return content.upper()

def file_read_write(input_file, output_file):
    try:
        # Read from input file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify the content
        modified_content = modify_content(content)
        
        # Write to output file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Success! Modified content written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except IOError:
        print(f"Error: Could not read {input_file} or write to {output_file}.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    input_file = "sample_files/input.txt"
    output_file = "sample_files/output.txt"
    file_read_write(input_file, output_file)
