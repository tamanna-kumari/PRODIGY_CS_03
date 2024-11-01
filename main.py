# Import all functions from the module, password_entry and figlet_one
from password_entry import get_password
from password_entry import password_feedback
from password_entry import check_password_strength
from password_entry import simulate_hashcat
from figlet_one import print_title

# Protecting the main function

if name == "main":
	try:
		print_title("Password Auth", "By: Somil Kathuria")
		password = get_password()
		password_feedback(password)
		if check_password_strength(password):
			simulate_hashcat(password)
	except Exception as e:
		print(f"An Error Occurred! Please try again {e}")
	except KeyboardInterrupt:
		print("\n"+"Oops!, Interrupted. Kindly Apologise.")

