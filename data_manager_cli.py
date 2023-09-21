import argparse
import sys
from personal_data_manager import PersonalDataManager

def main():
    
    parser = argparse.ArgumentParser(description="**Personal Data Manager**")
    
    # Add separate groups for different types of arguments
    
    # Action Group: Handles adding new records
    action_group = parser.add_argument_group("Actions")
    action_group.add_argument("--add", action="store_true", help="Add a new record(Name, Address, Phone)")
    
    # Filter Group: Handles filtering records by name
    filter_group = parser.add_argument_group("Filters and Queries")
    filter_group.add_argument("--filter", help="Filter records using Glob syntax ")
    
    # Output Group: Handles serialization and display options
    output_group = parser.add_argument_group("Output Options")
    output_group.add_argument("--serialize", help="Serialize records to a file (json, yaml, csv)")
    output_group.add_argument("--display", help="Display records in a format (text, html)")
    
    # argument to specify the filename for data storage
    parser.add_argument("--filename", default="personal_data.json", help="Specify the filename to read/save records")
 
    # Execute the command-line arguments
    args = parser.parse_args()
            
    # Create an instance of PersonalDataManager using the specified filename
    data_library = PersonalDataManager(args.filename)

    # Handle the "--add" argument to add a new record
    if args.add:
        name = input("Name: ")
        address = input("Address: ")
        phone_number = input("Phone number: ")
        data_library.add_record(name, address, phone_number)

    # Handle the "--filter" argument to filter and print records
    if args.filter:
        filtered_records = data_library.filter_records(args.filter)
        if filtered_records:
            print("Filtered Records:")
            for record in filtered_records:
                print(record)
        else:
            print("No matching data was found, please try again")        

    # Handle the "--serialize" argument to serialize records and print
    if args.serialize:
        serialized_data = data_library.serialize_records(args.serialize)
        print(serialized_data)

    # Handle the "--display" argument to display records and print
    if args.display:
        display_output = data_library.display_records(args.display)
        print(display_output)
    
    # Check if no additional arguments were provided and print help
    if len(sys.argv) == 1:
        parser.print_help()

if __name__ == "__main__":
    main()
