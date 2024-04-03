import os
import pandas as pd

def consolidate_excel_files(folder_path):
    # Get a list of all Excel files in the specified folder
    excel_files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]

    # Initialize an empty DataFrame to store consolidated data
    consolidated_df = pd.DataFrame()

    # Read each Excel file and append its contents to the consolidated DataFrame
    for file in excel_files:
        try:
            # Read the Excel file into a DataFrame
            df = pd.read_excel(os.path.join(folder_path, file), engine='openpyxl')  # Specify engine

            # Extract the profile name from the file name
            profile_name = os.path.splitext(file)[0].split('_')[-1]

            # Add a new column for profile name
            df['Profile'] = profile_name

            # Append the DataFrame to the consolidated DataFrame
            consolidated_df = pd.concat([consolidated_df, df], ignore_index=True)
        except zipfile.BadZipFile:
            print(f"Warning: Unable to read '{file}' as it is not a valid Excel file.")

    return consolidated_df

def main():
    # Folder path containing Excel files
    folder_path = '.'  # Change this to the folder containing your Excel files

    # Consolidate Excel files into one DataFrame
    consolidated_df = consolidate_excel_files(folder_path)

    # Write the consolidated DataFrame to a new Excel file
    consolidated_excel_file = 'consolidated_ec2_instance_details.xlsx'
    with pd.ExcelWriter(consolidated_excel_file) as writer:
        consolidated_df.to_excel(writer, index=False)

    print(f"All Excel files have been consolidated into '{consolidated_excel_file}'.")

if __name__ == "__main__":
    main()
