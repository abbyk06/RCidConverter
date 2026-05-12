CSVEntry.py reads an input CSV file, converts a Primary Card Number from Konica byte order to Canon byte order, and writes the result as a Secondary Card Number to a new CSV file.

OneEntry.py reads a singular id, converts from Konica byte order to Canon byte order. 

### CSV Requirements
- Input file must contain a column named Primary Card Number
- Leave numbers untouched (do not open/save in Excel before converting)
- Output file is generated entirely in-browser

### Notes
- Commas in numbers are automatically ignored
- Invalid or missing numbers are skipped
- No data is uploaded or stored

