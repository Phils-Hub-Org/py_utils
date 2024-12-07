def compareVersions(curr: str, prev: str) -> bool:
    """Compare two version strings."""
    # Extract prefix letters and remove them from version strings
    curr_prefix = ''.join(c for c in curr if not c.isalpha())
    prev_prefix = ''.join(c for c in prev if not c.isalpha())

    # Convert the version strings to lists of integers
    curr_components = list(map(lambda x: int(x), curr_prefix.split('.')))
    prev_components = list(map(lambda x: int(x), prev_prefix.split('.')))

    # Compare the version components
    for curr_comp, prev_comp in zip(curr_components, prev_components):
        if curr_comp > prev_comp:
            return True

    # If all components are equal, consider the versions equal
    return False

if __name__ == '__main__':
    print(compareVersions('1.0.0', '1.0.1'))