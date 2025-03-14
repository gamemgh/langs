import os
import zipfile

def zip_folders_in_directory(directory):
	directory = os.path.abspath(directory)
	if not os.path.exists(directory):
		print("Directory does not exist.")
		return

	for folder in os.listdir(directory):
		folder_path = os.path.join(directory, folder)
		
		if os.path.isdir(folder_path):  # Check if it's a folder
			zip_filename = os.path.join(directory, f"{folder}.zip")
			
			with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
				for root, _, files in os.walk(folder_path):
					for file in files:
						file_path = os.path.join(root, file)
						arcname = os.path.relpath(file_path, start=directory)
						zipf.write(file_path, arcname)
			
			print(f"Created: {zip_filename}")

if __name__ == "__main__":
	target_directory = "lang"
	zip_folders_in_directory(target_directory)