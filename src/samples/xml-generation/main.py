from csv_to_xml_converter_ import CSVtoXMLConverter


if __name__ == "__main__":
    #converter = CSVtoXMLConverter("/data/sample_dataset.csv")
    # Create an instance of CSVtoXMLConverter
    converter = CSVtoXMLConverter("/data/Small_job_descriptions2.csv","schema.xsd")
    """ converter = CSVtoXMLConverter("/data/sample_dataset.csv","schema.xsd") """

    # Generate the XML string and validate it against the schema
    xml_str = converter.to_xml_str_and_validate()

    # Now you can use the generated XML string as needed
    print(xml_str)
    print(converter.to_xml_str())
