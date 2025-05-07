import numpy as np
import pandas as pd

# Membuat data
phone_dataset = {
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


phoneData = pd.DataFrame(phone_dataset)

