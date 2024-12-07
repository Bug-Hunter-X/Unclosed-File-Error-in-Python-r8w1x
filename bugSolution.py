def function_with_closed_file(filename):
    try:
        f = open(filename, 'r')
        # ... some code that processes the file ...
        for line in f:
            print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        f.close() # Always close the file using finally to guarantee closure even if exceptions occur