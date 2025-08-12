```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_347.jpeg
document_name: XlsIO
page_number: 347
page_id: XlsIO#page_347
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:11:37Z
fidelity: lossless
-->

## Named Range Properties and Scope

### Named Range Properties

| Property       | Description                                                                                      |
|----------------|--------------------------------------------------------------------------------------------------|
|                | String for Name.                                                                                |
| RefersToRange | Gets/sets the Range associated with the Name object.                                         |
| Value         | For the Name object, a string containing the formula that the name is defined to is referred. <br> The string is in A1-style notation in the language of the macro, without an equal sign. |
| ValueR1C1     | Gets named range Value in R1C1 style. This is a Read-Only property.                           |
| Visible       | Determines whether the object is visible. Read/Write Boolean.                                 |
| Scope         | Returns the scope of the name range.                                                             |

### Scope of Named Range

The scope of the named range can be accessed as follows.

#### [C#]

```csharp
IName name = workbook.Names.Add("Name1");
name.RefersToRange = sheet.Range["A1"];
Console.WriteLine(name.Scope);
```

#### [VB.NET]

```vb
Dim name As IName = workbook.Names.Add("Name1")
name.RefersToRange = sheet.Range("A1")
Console.WriteLine(name.Scope)
```

## Formula Auditing

### Overview

- Excel provides an option to find and quickly identify any cell containing an error on the active worksheet.
- The Error Checking dialog box allows users to ignore errors shown with green indicators.
- This dialog box provides various options to gather information about the error, how the formula is evaluated, its trace, and an option to ignore the error by changing its data type.

### 4.4.4 Formula Auditing

Excel has an option to find the quickest way to identify any cell that contains an error on the active worksheet, and ignore the error that is showed with green indicator, through the Error Checking dialog box. This dialog box provides various options to get information on the error, how a formula is evaluated, its trace, and an option to ignore the error by changing its data type.

<!-- tags: [product, XlsIO, named range, formula auditing, error checking, scope, Excel, Range, IName, Read/Write, A1-style notation, R1C1 style] keywords: [named range properties, scope, formula auditing, error checking dialog, formula evaluation, trace, data type change] -->
```