from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
try:
    api.authenticate()
    print("Authentication successful!")
except Exception as e:
    print(f"Authentication failed. Error: {e}")
    print("Please check your kaggle.json file placement and permissions.")

# # Uncomment if you want to download dataset from kaggle 
# def download_kaggle_dataset(dataset_name, path='./dataset'):
#     api = KaggleApi()
#     api.authenticate()
#     api.dataset_download_files(dataset_name, path=path, unzip=True)

# # Uncomment the next line if you need to download the dataset from Kaggle
# download_kaggle_dataset(dataset_name, base_path)

dataset_name = ""  # Replace with actual dataset name if using Kaggle
base_path = ""  # Adjust if your dataset is stored elsewhere