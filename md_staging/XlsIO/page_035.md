```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_035.jpeg
document_name: XlsIO
page_number: 035
page_id: XlsIO#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:50:20Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
Dim application As IApplication = excelEngine.Excel
```

An Excel document is created.

### Creating a Workbook

1. Create a workbook. A newly created workbook has three worksheets by default. You can change the number of worksheets using the **Create** method of **IWorkBook** as shown in the following code.

   **C#**
   ```csharp
   // A new workbook is created. [Equivalent to creating a new workbook in MS Excel].
   // The new workbook will have 5 worksheets.
   IWorkbook workbook = application.Workbooks.Create(5);
   ```

   **VB.NET**
   ```vb.net
   ' A new workbook is created. [Equivalent to creating a new workbook in MS Excel].
   ' The new workbook will have 5 worksheets.
   Dim workbook As IWorkbook = application.Workbooks.Create(5)
   ```

A workbook with the mentioned number of worksheets is created in the Excel document.

**Note:** See **Workbook** and **Worksheet**, for more details.

### Accessing and Setting Data in a Worksheet

2. Access the worksheet in the workbook and set the data for the given range, say "A1".

   **C#**
   ```csharp
   // The first worksheet object in the worksheets collection is accessed.
   IWorksheet sheet = workbook.Worksheets[0];

   // Inserting sample text into the first cell of the first worksheet.
   sheet.Range["A1"].Text = "Hello World";
   ```

   **VB.NET**
   ```vb.net
   ' The first worksheet object in the worksheets collection is accessed.
   Dim sheet As IWorksheet = workbook.Worksheets(0)
   ```

## API Reference

### Methods and Properties
- **application.Workbooks.Create(int worksheetsCount)**: Creates a new workbook with the specified number of worksheets.
- **workbook.Worksheets[0]**: Accesses the first worksheet in the workbook.
- **sheet.Range[string cellAddress].Text**: Sets the text value of the specified cell.

## Code Examples

### C# Example
```csharp
// Initialize Excel
Dim application As IApplication = excelEngine.Excel
IWorkbook workbook = application.Workbooks.Create(5)
IWorksheet sheet = workbook.Worksheets[0]
sheet.Range["A1"].Text = "Hello World"
' Save the workbook
workbook.Save("output.xlsx")
application.Exit()
```

### VB.NET Example
```vb.net
' Initialize Excel
Dim application As IApplication = excelEngine.Excel
Dim workbook As IWorkbook = application.Workbooks.Create(5)
Dim sheet As IWorksheet = workbook.Worksheets(0)
sheet.Range("A1").Text = "Hello World"
' Save the workbook
workbook.Save("output.xlsx")
application.Exit()
```

<!-- tags: [essential xlsio, workbook, worksheet, data manipulation] keywords: [workbook creation, worksheet access, cell value setting, excel engine, text insertion] -->
```