```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_276.jpeg
document_name: DocIo
page_number: 276
page_id: DocIo#page_276
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:46:24Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates the creation and population of a `DataTable` for mail merge operations.
- Discusses the integration of `DataTable` data with document templates for personalized content generation.

## Content

### Creating a DataTable for Mail Merge

#### Overview
This section focuses on creating a `DataTable` object and populating it with sample data. The `DataTable` is used to provide dynamic content for mail merge operations in Word documents.

#### Code Example

```csharp
/// <summary>
/// Create DataTable and fill it with data.
/// </summary>
private static DataTable GetDataTable()
{
    DataTable dataTable = new DataTable("Employee");

    dataTable.Columns.Add("EmpName");
    dataTable.Columns.Add("EmpNumber");

    for (int i = 0; i < 20; i++)
    {
        DataRow datarow = dataTable.NewRow();

        dataTable.Rows.Add(datarow);

        datarow[0] = "Emp" + i.ToString();
        datarow[1] = "Emp" + i.ToString();
    }

    return dataTable;
}
```

Explanation:
- A `DataTable` named "Employee" is created.
- Two columns, `EmpName` and `EmpNumber`, are added to the table.
- A `for` loop populates the table with 20 rows, each containing the same values for `EmpName` and `EmpNumber`.

### Executing Mail Merge with Groups

#### Overview
This section demonstrates how to perform a mail merge operation using a `DataTable` and a Word document template. The process involves loading the template and executing the mail merge with grouped data.

#### Code Example

```vb
[VB]
Public Sub MailMerge()

    ' Load the template.
    Dim document As WordDocument = New WordDocument("Template.doc")

    ' Execute Mail Merge with groups.
End Sub
```

Explanation:
- A Word document template is loaded using the `WordDocument` class.
- The next step involves executing the mail merge operation to replace placeholder fields in the template with data from the `DataTable`.

## API Reference

### Methods
#### `GetDataTable()`
- **Returns:** `DataTable`
- **Description:** Creates a `DataTable` with two columns (`EmpName` and `EmpNumber`) and populates it with 20 rows of sample data.

#### `MailMerge()`
- **Description:** Executes a mail merge operation using a Word document template and grouped data from a `DataTable`.

## Code Examples

### C# Example

```csharp
private static DataTable GetDataTable()
{
    DataTable dataTable = new DataTable("Employee");

    dataTable.Columns.Add("EmpName");
    dataTable.Columns.Add("EmpNumber");

    for (int i = 0; i < 20; i++)
    {
        DataRow datarow = dataTable.NewRow();

        dataTable.Rows.Add(datarow);

        datarow[0] = "Emp" + i.ToString();
        datarow[1] = "Emp" + i.ToString();
    }

    return dataTable;
}
```

### VB Example

```vb
Public Sub MailMerge()
    Dim document As WordDocument = New WordDocument("Template.doc")
End Sub
```

## Page-level Navigation/TOC (if applicable)
- [Getting Started]
- [Creating a DataTable for Mail Merge]
- [Executing Mail Merge with Groups]

## Cross References
- Refer to the "Mail Merge Overview" for a comprehensive understanding of the process.
- For more details on working with `DataTable`, see the .NET Framework documentation.

## RAG Annotations
<!-- tags: [mail merge, dataTable, document template, word merge, syncfusion winforms, data population] keywords: [DataTable, WordDocument, mail merge, template, grouped data, dynamic content] -->
```