import os
import subprocess

# Get the current working directory
cwd = os.getcwd()

# Define paths relative to the current working directory
data_dir = os.path.join(cwd, "resources", "data")

# URLs and file paths
train_tar_url = "https://cocl.us/DL0320EN_TRAIN_TAR_PYTORCH"
train_tar_path = os.path.join(data_dir, "training_data_pytorch.tar.gz")

valid_tar_url = "https://cocl.us/DL0320EN_VALID_TAR_PYTORCH"
valid_tar_path = os.path.join(data_dir, "validation_data_pytorch.tar.gz")

test_tar_url = "https://cocl.us/DL0320EN_TEST_TAR_PYTORCH"
test_tar_path = os.path.join(data_dir, "test_data_pytorch.tar.gz")

# Create the data directory if it doesn't exist
os.makedirs(data_dir, exist_ok=True)

# Download and extract the training data
subprocess.run(["wget", "-q", "-O", train_tar_path, train_tar_url], check=True)
subprocess.run(["tar", "-xzf", train_tar_path, "-C", data_dir], check=True)

# Download and extract the validation data
subprocess.run(["wget", "-q", "-O", valid_tar_path, valid_tar_url], check=True)
subprocess.run(["tar", "-xzf", valid_tar_path, "-C", data_dir], check=True)

# Download and extract the test data
subprocess.run(["wget", "-q", "-O", test_tar_path, test_tar_url], check=True)
subprocess.run(["tar", "-xzf", test_tar_path, "-C", data_dir], check=True)
