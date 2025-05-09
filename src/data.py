import numpy as np
import pandas as pd

phoneData = {
    "Case": [1, 2, 3, 4],
    "Budget $": [400, 300, 500, 450],
    "Screen Size (inch)": [6.1, 5.5, 6.5, 6.0],
    "Battery Capacity (mAh)": [4000, 3500, 4500, 4000],
    "Preferred Brand": ["Samsung", "Xiaomi", "OnePlus", "Samsung"],
    "Recommended Phone": [
        "Samsung Galaxy A32",
        "Xiaomi Redmi 9",
        "OnePlus Nord N10",
        "Samsung Galaxy A52"
    ]
}


laptopData = {
     "Model": [
        "Laptop A",
        "Laptop B",
        "Laptop C",
        "Laptop D",
        "Laptop E"
    ],
    "Budget $": [600,750,500,700,650],
    "Ram": [8,16,8,16,12],
    "Storage": [256,512,128,256,512],
    "Processor": ["Intel i5", "Intel i7", "Intel i5", "Amd Ryzen 5","Intel i5"],
    "Battery Life": [10,8,12,9,7],
}


phoneData = pd.DataFrame(phoneData)
laptopData = pd.DataFrame(laptopData)
