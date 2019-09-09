def interface():
	print("My calculator program")
        keep_running = True
        while keep_running:
	        print("Option: ")
	        print("0 - Quit")
	        choice = input("Enter your choice: ")
	        if choice == '9':
		        return
        return

if __name__ == "__main__":
	interface()
