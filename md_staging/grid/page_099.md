```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_099.jpeg
document_name: grid
page_number: 099
page_id: grid#page_099
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:22:02Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This section explains how to create a data source class for a virtual grid in Windows Forms using C#.
- Demonstrates the use of public properties and a class indexer to manage data access in a grid.

## Content

The grid requires knowledge of the number of rows and columns. While this can be relaxed, knowing the number simplifies implementations. The tutorial assumes this knowledge is available.

### External Data Source

The external data source is represented by a class with:
- Two public properties: `RowCount` and `ColCount`.
- A two-parameter class indexer to retrieve integer values based on row and column indexes.

The class mechanics are simplified for this tutorial. It primarily serves to provide data as needed without detailing how the data is stored or retrieved.

### Steps to Create the DataSource Class

1. **Add the DataSource Class:**
   - Right-click the project in the Solution Explorer.
   - Point to `Add`, click `Class`, and add a class named `ExternalData`.

2. **Copy the Code into the Class File:**
   - The constructor accepts row and column counts and populates an integer array.
   - The class allows modifications to how data is stored or accessed, as long as the class indexer and `RowCount` and `ColCount` properties are defined for virtual grid access.

```csharp
public class ExternalData
{
    private int _rowCount;
    private int _colCount;
    private int[,] _data;

    public ExternalData(int rows, int cols)
    {
        // Set number of rows and number of columns.
        _rowCount = rows;
        _colCount = cols;

        // Allocate memory to store data values.
        _data = new int[_rowCount, _colCount];

        // Just set the data.
        for (int i = 0; i < RowCount; ++i)
            for (int j = 0; j < ColCount; ++j)
                _data[i, j] = 100 * i + j;
    }

    // Set Properties.
    public virtual int this[int row, int col]
    {
        get { return _data[row, col]; }
        set { _data[row, col] = value; }
    }
}
```

### Summary
This implementation provides a foundational understanding of how to create a data source class for a virtual grid, focusing on essential properties and data access mechanisms.

## API Reference

- **Namespace:** (Not explicitly mentioned but typically part of Syncfusion.Windows.Forms)
- **Class:** `ExternalData`
- **Properties:**
  - `RowCount`: Returns the number of rows.
  - `ColCount`: Returns the number of columns.
- **Indexer:** `this[int row, int col]`
  - **Get:** Retrieves the integer value at the specified row and column.
  - **Set:** Assigns a new integer value to the specified row and column.

## Code Examples

```csharp
public class ExternalData
{
    // ... constructor and properties as shown above ...
}
```

### Usage Example

```csharp
ExternalData dataSource = new ExternalData(10, 5);
// Accessing data
int value = dataSource[3, 2];
// Modifying data
dataSource[3, 2] = 200;
```

## Cross References

- See also: Other tutorials on virtual grids and custom data sources in the Syncfusion WinForms documentation.

<!-- tags: [Syncfusion, Windows Forms, Virtual Grid, DataSource, C#] keywords: [data source class, RowCount, ColCount, class indexer, virtual grid, Windows Forms, C#] -->
```