```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_298.jpeg
document_name: grid
page_number: 298
page_id: grid#page_298
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:07:30Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- The document explains the functions of HLOOKUP and HOUR in the context of grid data manipulation in Windows Forms.
- HLOOKUP is used to search for a value in the top row of an array and return a value in the same column from a specified row.
- HOUR is used to extract the hour from a time value as an integer.

## Content

### HLOOKUP

**Description:**
Searches for a value in the top row of the array of values and then returns a value in the same column from a row you specify in the array. Use HLOOKUP when your comparison values are located in a row across the top of a table of data and you want to look down a specified number of rows. Use VLOOKUP when your comparison values are located in a column to the left of the data you want to find.

#### Syntax

**HLOOKUP(lookup_value, table_array, row_index_num, range_lookup),** where:

- **lookup_value:** is the value to be found in the first row of the table. Lookup_value can be a value, a reference, or a text string.
- **table_array:** is a table of information in which data is looked up. Use a reference to a range or a range name.
- **row_index_num:** is the row number in table_array from which the matching value will be returned. A row_index_num of 1 returns the first row value in table_array, a row_index_num of 2 returns the second row value in table_array, and so on.
- **range_lookup:** is a logical value that specifies whether you want HLOOKUP to find an exact match or an approximate match. If True or omitted, an approximate match is returned. If False, HLOOKUP will find an exact match.

### HOUR

**Description:**
Returns the hour of a time value. The hour is given as an integer, ranging from 0 (12:00 A.M.) to 23 (11:00 P.M.).

#### Syntax

**HOUR(serial_number),** where:

## API Reference

- **HLOOKUP:** 
  - **Parameters:**
    - lookup_value
    - table_array
    - row_index_num
    - range_lookup
  - Returns the value in the specified row and column based on the lookup criteria.

- **HOUR:** 
  - **Parameters:**
    - serial_number
  - Returns the hour as an integer from a given time value.

## Code Examples

### Example for HLOOKUP:
```csharp
public void HLookupExample()
{
    // Example array
    var tableArray = new object[,] 
    {
        { "Apple", 2, 3 },
        { "Banana", 4, 5 },
        { "Cherry", 6, 7 }
    };

    // Lookup value
    var lookupValue = "Apple";

    // Row index
    var rowIndex = 2;

    // Exact match
    var rangeLookup = false;

    // Perform HLOOKUP
    var result = HLookup(lookupValue, tableArray, rowIndex, rangeLookup);

    // Output result
    Console.WriteLine($"Result: {result}");
}
```

### Example for HOUR:
```csharp
public void HourExample()
{
    // Example time value
    var timeValue = DateTime.Parse("14:30:00");

    // Get hour
    var hour = HOUR(timeValue);

    // Output hour
    Console.WriteLine($"Hour: {hour}");
}
```

## RAG Annotations
<!-- tags: [HLOOKUP, HOUR, Windows Forms, grid data, time values, match types] keywords: [HLOOKUP, HOUR, lookup, time, row_index_num, range_lookup] -->
```