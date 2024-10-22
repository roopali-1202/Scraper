import csv
import os
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Function to generate fake social media profiles
def generate_fake_profiles(platform, num_unique, num_duplicates):
    """
    Generate unique and duplicate profiles for a given social media platform.

    :param platform: The name of the platform (e.g., 'instagram', 'twitter')
    :param num_unique: The number of unique profiles to generate
    :param num_duplicates: The number of duplicate profiles (identity theft data)
    :return: A list of dictionaries representing the profiles
    """
    profiles = []

    # Generate unique profiles
    for _ in range(num_unique):
        profile = {
            'Name': fake.name(),
            'Username': fake.user_name(),
            'Email': fake.email(),
            'Bio': fake.sentence(nb_words=10),
            'Location': fake.city(),
            'Profile URL': f'https://{platform}.com/{fake.user_name()}'
        }
        profiles.append(profile)
    
    # Generate duplicate profiles to simulate identity theft
    duplicate_profile = {
        'Name': fake.name(),
        'Username': fake.user_name(),
        'Email': fake.email(),
        'Bio': fake.sentence(nb_words=10),
        'Location': fake.city(),
        'Profile URL': f'https://{platform}.com/{fake.user_name()}'
    }
    
    # Add the same duplicate profile multiple times
    for _ in range(num_duplicates):
        profiles.append(duplicate_profile)

    return profiles

# Function to write profiles to a CSV file in the same directory
def write_profiles_to_csv(profiles, platform):
    """
    Write the list of profiles to a CSV file for a given platform.

    :param profiles: List of dictionaries representing the profiles
    :param platform: The name of the platform (used in the filename)
    """
    filename = f"{platform}_profiles.csv"  # File will be saved in the same folder as the script
    
    # Open the CSV file in write mode
    with open(filename, mode='w', newline='') as file:
        # Define the CSV column names based on the dictionary keys
        writer = csv.DictWriter(file, fieldnames=profiles[0].keys())
        
        # Write the header (column names)
        writer.writeheader()
        
        # Write all profiles (rows) to the CSV
        writer.writerows(profiles)
        
    print(f"Exported {platform} profiles to {filename}")

# Number of profiles to generate
num_unique_profiles = 450  # Unique profiles
num_duplicate_profiles = 50  # Duplicate (identity theft) profiles
total_profiles = num_unique_profiles + num_duplicate_profiles  # Total should be 500

# Generate profiles for different platforms
instagram_profiles = generate_fake_profiles('instagram', num_unique_profiles, num_duplicate_profiles)
twitter_profiles = generate_fake_profiles('twitter', num_unique_profiles, num_duplicate_profiles)
threads_profiles = generate_fake_profiles('threads', num_unique_profiles, num_duplicate_profiles)
facebook_profiles = generate_fake_profiles('facebook', num_unique_profiles, num_duplicate_profiles)

# Export profiles to CSV files in the same folder
write_profiles_to_csv(instagram_profiles, 'instagram')
write_profiles_to_csv(twitter_profiles, 'twitter')
write_profiles_to_csv(threads_profiles, 'threads')
write_profiles_to_csv(facebook_profiles, 'facebook')
