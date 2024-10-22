import csv
from collections import defaultdict

# Function to load profiles from a CSV file
def load_profiles_from_csv(file_path):
    """
    Load profiles from a CSV file and return a list of dictionaries.
    
    :param file_path: Path to the CSV file
    :return: List of profiles (dictionaries)
    """
    profiles = []
    
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        
        # Add each row (profile) to the profiles list
        for row in reader:
            profiles.append(row)
    
    return profiles

# Function to find duplicate profiles (potential fake profiles)
def find_duplicate_profiles(profiles):
    """
    Find duplicate profiles based on Name, Username, and Email.
    
    :param profiles: List of profiles (dictionaries)
    :return: List of duplicate profiles
    """
    profile_lookup = defaultdict(list)  # Dictionary to hold profiles by key attributes
    
    # Define key attributes for checking duplicates
    key_attributes = ['Name', 'Username', 'Email']
    
    for profile in profiles:
        # Create a unique key based on key attributes (Name, Username, and Email)
        profile_key = tuple(profile[attr] for attr in key_attributes)
        
        # Store the profile using the key
        profile_lookup[profile_key].append(profile)
    
    # Find keys that have more than one profile (duplicates)
    duplicates = [profiles for profiles in profile_lookup.values() if len(profiles) > 1]
    
    return duplicates

# Function to export fake profiles to a new CSV file
def export_fake_profiles(fake_profiles, output_file):
    """
    Export the list of fake profiles to a new CSV file.
    
    :param fake_profiles: List of fake profiles (dictionaries)
    :param output_file: The output CSV file path
    """
    if not fake_profiles:
        print("No fake profiles found.")
        return
    
    # Get the headers (column names) from the first fake profile
    headers = fake_profiles[0][0].keys()
    
    # Open the output file and write the fake profiles
    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        
        # Write the header row
        writer.writeheader()
        
        # Write all fake profiles to the CSV
        for profile_list in fake_profiles:
            for profile in profile_list:
                writer.writerow(profile)
    
    print(f"Exported {len(fake_profiles)} fake profiles to {output_file}")

# Main function to filter and export fake profiles from an existing CSV file
def display_fake_profiles(file_path, output_file):
    """
    Display fake profiles in the given CSV file and export them to a new CSV file.
    
    :param file_path: Path to the input CSV file with all profiles
    :param output_file: Path to the output CSV file for fake profiles
    """
    # Load profiles from the CSV file
    profiles = load_profiles_from_csv(file_path)
    
    # Find duplicate profiles
    fake_profiles = find_duplicate_profiles(profiles)
    
    # Export the fake profiles to a new CSV file
    export_fake_profiles(fake_profiles, output_file)

# Example usage
# Path to the CSV file with all social media profiles
file_path = 'all_instagram_profiles.csv'  # Change this to the actual CSV file path

# Path to the output file where fake profiles will be exported
output_file = 'fake_profiles_only.csv'

# Display and export fake profiles
display_fake_profiles(file_path, output_file)
