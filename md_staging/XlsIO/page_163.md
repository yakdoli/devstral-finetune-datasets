```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_163.jpeg
document_name: XlsIO
page_number: 163
page_id: XlsIO#page_163
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:58:44Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
// Method 3 to Access a Range(using defined names).
sheet.Range["Name"].Text = "Accessing a Range (Method 3)";

// Accessing a Range of cells (Method 1).
sheet.Range["A13:C13"].Text = "Accessing a Range of Cells (Method 1)";

// Accessing a Range of cells (Method 2).
sheet.Range[15, 1, 15, 3].Text = "Accessing a Range of Cells (Method 2)";

// Accessing a Range of cells (Method 3 using defined names).
sheet.Range["Name1"].Text = "Accessing a Range of Cells (Method 3)";
```

```vb.net
' Method 1 to Access a Range.
sheet.Range("A7").Text = "Accessing a Range (Method 1)"

' Method 2 to Access a Range.
sheet.Range(9, 1).Text = "Accessing a Range (Method 2)"

' Method 3 to Access a Range(using defined names).
sheet.Range("Name").Text = "Accessing a Range (Method 3)"

' Accessing a Range of cells (Method 1).
sheet.Range("A13:C13").Text = "Accessing a Range of Cells (Method 1)"

' Accessing a Range of cells (Method 2).
sheet.Range(15, 1, 15, 3).Text = "Accessing a Range of Cells (Method 2)"

' Accessing a Range of cells (Method 3 using defined names).
sheet.Range("Name1").Text = "Accessing a Range of Cells (Method 3)"
```

## Accessing Discontinuous Ranges

You can also access different discontinuous ranges and add them to the **RangesCollection**, so that the same format is applied to different ranges. Following code example explains the same.

### WinForms-specific conventions
- Methods/Events/Enums of the participating controls (e.g., Grid, TabControlAdv, or other custom controls) are referenced if visible, preserving exact names used in the context.
- Code examples show API usage with methods and properties as present in the description, with parameters, return types, and exceptions if listed.

```csharp
// Create ranges and add to RangesCollection.
IRange range1 = sheet.Range[ "A1:A2" ];
IRange range2 = sheet.Range["C1:C2" ];

RangesCollection ranges = new RangesCollection( engine.Excel, sheet );
```

<!-- tags: [Syncfusion Winforms, XlsIO, Essential XlsIO, Ranges, Accessing Ranges, Discontinuous Ranges, RangesCollection, Accessing a Range, WinForms controls] keywords: [defined names, range access, range formats, range collection, discontinuous ranges] -->
``` 
