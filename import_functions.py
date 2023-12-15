import pandas

# method for reading csv
def read_users_file(file_name:str) ->  pandas.DataFrame:
    '''
    Helper for reading a csv file
    
    Params:

    * filename
    
    '''
    
    # read the csv
    df = pandas.read_csv(file_name)

    # return the list with users_first_name, last_name and e_mail
    users_first_names = df.iloc[:, 0].to_list()
    users_last_names = df.iloc[:, 1].to_list()
    users_emails = df.iloc[:, 2].to_list()

    return users_first_names, users_last_names, users_emails


    



