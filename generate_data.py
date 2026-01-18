import pandas as pd
import random
from datetime import datetime, timedelta

# sample data lists
names = ["Alice Smith", "Bob Jones", "Charlie Brown", "Diana Prince", "Edward Norton", "Fiona Gallagher", "George Miller", "Hannah Abbott", "Ian Wright", "Julia Roberts"
        ]

# function to generate a random birthday between 1970 and 2005
def random_birthday():
    start_date = datetime(1970,1,1)
    end_date = datetime(2005,12,31)
    days_between = (end_date - start_date).days
    random_days = random.randrange(days_between)
    return(start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

# build the dataset (using a dict - which can be used to look up keys)
data={
    "Customer Name": names, 
    "Customer ID": [f"CUST-{random.randint(1000,9999)}"for _ in range(10)],
    "Birthday": [random_birthday() for _ in range(10)]
}

#create dataframe and save to csv
df = pd.DataFrame(data)
df.to_csv("customers.csv", index=False)

print("Success! 'customer.csv' has been created in your folder.")
