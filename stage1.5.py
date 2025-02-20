def hamming_distance(str1, str2):
    # Pad the shorter string with spaces to match the length of the longer string
    max_length = max(len(str1), len(str2))
    str1 = str1.ljust(max_length)
    str2 = str2.ljust(max_length)
    
    return sum(1 for a, b in zip(str1, str2) if a != b)

# Example usage
slack_username = "BioChemGuy"
twitter_handle = "MolecularAce"

distance = hamming_distance(slack_username, twitter_handle)
print(f"Hamming distance between '{slack_username}' and '{twitter_handle}': {distance}")
