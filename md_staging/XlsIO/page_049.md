```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_049.jpeg
document_name: XlsIO
page_number: 049
page_id: XlsIO#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:51:43Z
fidelity: lossless
-->

## Essential XlsIO

- A new workbook is created. [Equivalent to creating a new workbook in MS Excel].
- The new workbook will have 5 worksheets.

```csharp
Dim workbook As IWorkbook = application.Workbooks.Create(5)
```

### Overview

- A workbook with the mentioned number of worksheets is created in the Excel document.

### Accessing and Setting Data in the Workbook

1. **Access the workbook** in the workbook and set the data for the given Range, say "A1".

   ```csharp
   // The first worksheet object in the worksheets collection is accessed.
   IWorksheet sheet = workbook.Worksheets[0];

   // Inserting sample text into the first cell of the first worksheet.
   sheet.Range["A1"].Text = "Hello World";
   ```

   ```vbnet
   ' The first worksheet object in the worksheets collection is accessed.
   Dim sheet As IWorksheet = workbook.Worksheets(0)

   ' Inserting sample text into the first cell of the first worksheet.
   sheet.Range("A1").Text = "Hello World"
   ```

   The string "Hello World" is written to the cell A1 of the document.

2. **Save to stream and close the workbook. Also, dispose the Excel engine.**

   ```csharp
   // Save the file on to disk.
   SaveFileDialog sfd = new SaveFileDialog();
   sfd.DefaultExt = ".xls";
   sfd.Filter = "Files(*.xls)|*.xls";
   if (sfd.ShowDialog() == true)
   {
       using (Stream stream = sfd.OpenFile())
       {
           workbook.SaveAs(stream);
       }
   }
   ```

   **Note:** The engine should be disposed after completing workbook operations.

<!-- tags: [Essential XlsIO, workbook, worksheet, range, data, saving, closing, disposing] keywords: [workbook creation, setting data, hello world, saving to disk, disposing, Excel engine] -->
```