import json
import yaml
import glob

class PersonalDataManager:

    def __init__(self, filename):
        """
        Initialize the PersonalDataManager.

        Args:
            filename (str): The name of the file to load and save data records.
        """
        self.records = []
        self.filename = filename
        self.load_from_file()

    def load_from_file(self):
        """
        Load data records from the specified file.
        """
        try:
            with open(self.filename, "r") as f:
                self.records = json.load(f)
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Starting with an empty dataset.")

    def save_to_file(self):
        """
        Save data records to the specified file.
        """
        with open(self.filename, "w") as f:
            json.dump(self.records, f, indent=4)
            print(f"Records saved to '{self.filename}'.")

    def add_record(self, name, address, phone_number):
        """
        Add a new record to the dataset and save it to the file.

        Args:
            name (str): The name of the person.
            address (str): The address of the person.
            phone_number (str): The phone number of the person.
        """
        self.records.append({"name": name, "address": address, "phone_number": phone_number})
        self.save_to_file()

    def filter_records(self, search_query):
        """
        Filter records based on the given search query.

        Args:
            search_query (str): The search query for filtering records.

        Returns:
            list: List of filtered records.
        """
        filtered_records = []

        for record in self.records:
            if self.match_record(record, search_query):
                filtered_records.append(record)

        return filtered_records

    def match_record(self, record, search_query):
        """
        Check if a record matches the given search query.

        Args:
            record (dict): The record to match against.
            search_query (str): The search query for matching.

        Returns:
            bool: True if the record matches the query, False otherwise.
        """
        for condition in search_query.split(","):
            attr, pattern = condition.split("=")
            if attr.strip() in record and glob.fnmatch.fnmatch(record[attr.strip()].lower(), pattern.strip().lower()):
                continue
            else:
                return False
        return True

    def serialize_records(self, format):
        """
        Serialize records into the specified format.

        Args:
            format (str): The serialization format (json, yaml, or csv).

        Returns:
            str: The serialized records.
        """
        if format == "json":
            return json.dumps(self.records, indent=4)
        elif format == "yaml":
            return yaml.dump(self.records)
        elif format == "csv":
            output = "name,address,phone_number\n"
            for record in self.records:
                output += f"{record['name']},{record['address']},{record['phone_number']}\n"
            return output

    def display_records(self, format):
        """
        Display records in the specified format.

        Args:
            format (str): The display format (text or html).
        """
        if format == "text":
            output = ""
            for record in self.records:
                output += f"Name: {record['name']}\n"
                output += f"Address: {record['address']}\n"
                output += f"Phone_number: {record['phone_number']}\n\n"
            return output
        elif format == "html":
            html_data = '<html>\n<body>\n'
            for record in self.records:
                html_data += '<h3>Name: {}</h3>\n'.format(record['name'])
                html_data += '<p>Address: {}</p>\n'.format(record['address'])
                html_data += '<p>Phone_number: {}</p>\n'.format(record['phone_number'])
                html_data += '<hr/>\n'
            html_data += '</body>\n</html>'
            print(html_data)
        else:
            return "Unsupported output format."
