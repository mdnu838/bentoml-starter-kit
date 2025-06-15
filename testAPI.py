import requests
import numpy as np

input_data = np.array([[5.1, 3.5, 1.4, 0.2]]).tolist()
response = requests.post("http://localhost:3000/classify", json=input_data)
print(response.json())
