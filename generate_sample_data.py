import pandas as pd

def create_sample_data(complete_data_file, sample_data_file, sample_size):
    # Read the complete data
    complete_data = pd.read_csv(complete_data_file, header=None)
    
    # Randomly sample the data
    sample_data = complete_data.sample(n=sample_size, random_state=1)
    
    # Save the sampled data to sample_data.csv
    sample_data.to_csv(sample_data_file, index=False, header=False)

# Example usage
complete_data_file = 'complete_data.csv'
sample_data_file = 'sample_data.csv'
sample_size = 100  # Change this to the desired number of samples
create_sample_data(complete_data_file, sample_data_file, sample_size)
