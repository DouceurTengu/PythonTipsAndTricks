'''
:param: birthdayDate: Date of birth
:param: today: the date you wish to compare to the birth date to compute age
:return: returns an integer value representing the difference of the two dates

NOTE: if you want to use this function with a pandas dataframe, you'd apply it as follows:

today = df.columns.get_loc('today_column')
birthDate = df.columns.get_loc('birthDate_column')
df['Age'] = df.apply(lambda x: calculate_age(x[today], x[birthDate], axis=1)

You can also save yourself the trouble of writing the three lines above by writing
a simple function that takes in the dataframe as a variable and uses the function below to compute age
then returns the new dataframe with the added column ['Age']

This function is not limited to computing age. You can use it to compute the difference between any two dates.
I just usually use it for Age computations ;).
'''
from datetime import date

def calculate_age(birthdayDate, today):
    if pd.isnull(birthdayDate):
        return np.nan
    else:
        return today.year - birthdayDate.year - ((today.month, today.day) < (birthdayDate.month, birthdayDate.day))
