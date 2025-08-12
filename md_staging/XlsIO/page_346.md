```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_346.jpeg
document_name: XlsIO
page_number: 346
page_id: XlsIO#page_346
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:09:53Z
fidelity: lossless
-->

## Overview

- Demonstrates the creation and manipulation of named ranges in spreadsheet documents using `IName` interface.
- Explains how to retrieve, enumerate, and delete named ranges from a worksheet or workbook.
- Lists the properties of the `IName` interface for reference.

## Content

```vb
Dim lname1 As IName = sheet.Names.Add("CellName")
lname1.RefersToRange = sheet.Range("C3")

' Get name.
Console.WriteLine(sheet.Names("CellName").Value)
```

You can get/read all the names from a worksheet or workbook just by enumerating the `IName` collection as follows.

### C#

```csharp
for (int i = 0; i <= workbook.Names.Count; i++)
{
    Console.WriteLine(workbook.Names[i].Name.ToString());
    Console.WriteLine(workbook.Names[i].RefersToRange.Address.ToString());
    Console.WriteLine(workbook.Names[i].Name.Value.ToString());
}
```

### VB.NET

```vb
Dim i As Integer
For i = 0 To workbook.Names.Count Step i + 1
    Console.WriteLine(workbook.Names(i).Name.ToString())
    Console.WriteLine(workbook.Names(i).RefersToRange.Address.ToString())
    Console.WriteLine(workbook.Names(i).Name.Value.ToString())
Next
```

You can also delete a name in the workbook/worksheet by using the `Delete` method of `IName`. Note that deleting the cell does not delete the name from the `Name` collection.

### Properties of `IName`

Following table lists the properties of `IName`.

| Property      | Description                                                                                                                                                                                                 |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Index         | Returns the index number of the `Name` object within the collection. This is a Read-Only property.                                                                                                           |
| IsLocal       | Indicates whether the name is local.                                                                                                                                                                        |
| Name          | Returns or sets the name of the object. Read/Write String.                                                                                                                                                  |
| NameLocal     | Returns or sets the name of the object, in the language of the user. Read/Write                                                                                                                             |

<!-- tags: [xlsio, syncedbook, worksheet, workbook, named ranges, iName, .NET, WinForms] keywords: [workbook, workbookNames, annotation, synfusion, array formula, region, crm, tex] -->
```