# import pandas as pd

# my_dataset = {
#      "cars":["BMW","volvo","Ford"],
#     "passings":[3,7,2]
# }
# myvar= pd.DataFrame(my_dataset)
# print(myvar)




# import pandas as pd

# a = [1,7,2]

# myvar = pd.Series(a)
# print(myvar)



# import pandas as pd

# a = [1,7,2]

# myvar = pd.Series(a,index =["x","y","z"])
# print(myvar)

# import pandas as pd

# my_dataset = {
#     "calories":  [420,380,390],
#     "duration":  [2,3,5]
# }
# myvar= pd.DataFrame(my_dataset)
# print(myvar)

import pandas as pd 
df = read_csv("housing.csv")
print(df.head())

print("Average priceL",df["price"],mean())

df[df["price"]>10000]

#groupy code
df.groupby("furnishingstatus").mean(numeric_only=True)

#numeric only code
df.groupby("numeric_only=True")