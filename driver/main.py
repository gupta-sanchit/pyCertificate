import pandas as pd
from tqdm import tqdm
from generator.addName import certificate

data = pd.read_csv("../data/participantDetails.csv")

for i in tqdm(range(len(data))):

    certificateID = data['certificateID'][i]
    name = data['name'][i].rstrip().lstrip()
    gender = data['gender'][i].lower()

    try:
        certificate(name=name, gender=gender, certificateID=certificateID)

    except BaseException as e:
        print(f"Error in {certificateID}")
        print(f"error occurred: {e}")
