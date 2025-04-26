import json
import os

def process_json_files(source_folder, destination_folder):
	"""
	Checks for JSON files in the source folder, reads the 'config' object,
	and creates new JSON files in the destination folder with the config
	object embedded at the top level.

	Args:
		source_folder (str): Path to the folder containing the original JSON files.
		destination_folder (str): Path to the folder where new JSON files will be created.
	"""
	if not os.path.exists(destination_folder):
		os.makedirs(destination_folder)
		print(f"Created destination folder: {destination_folder}")

	for filename in os.listdir(source_folder):
		if filename.endswith(".json"):
			source_path = os.path.join(source_folder, filename)
			destination_path = os.path.join(destination_folder, filename)

			try:
				with open(source_path, 'r') as f:
					data = json.load(f)
					if 'config' in data:
						config_object = data['config']
						with open(destination_path, 'w') as outfile:
							json.dump(config_object, outfile, indent=4)
						print(f"Processed and created: {filename}")
					else:
						print(f"Warning: '{filename}' does not contain a 'config' object. Skipping.")
			except FileNotFoundError:
				print(f"Error: File not found - {source_path}")
			except json.JSONDecodeError:
				print(f"Error: Could not decode JSON in - {source_path}")
			except Exception as e:
				print(f"An unexpected error occurred while processing {filename}: {e}")

if __name__ == "__main__":
	source_directory = "lang"
	destination_directory = "json"

	process_json_files(source_directory, destination_directory)

	print("\nScript execution complete.")