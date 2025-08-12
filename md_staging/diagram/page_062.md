```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_062.jpeg
document_name: diagram
page_number: 062
page_id: diagram#page_062
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:12:30Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```csharp
{
    PrintDocument printDoc = diagram1.CreatePrintDocument();
    PrintPreviewDialog printPreviewDlg = new PrintPreviewDialog();
    printPreviewDlg.StartPosition = FormStartPosition.CenterScreen;

    printDoc.PrinterSettings.FromPage = 0;
    printDoc.PrinterSettings.ToPage = 0;
    printDoc.PrinterSettings.PrintRange = PrintRange.AllPages;

    printPreviewDlg.Document = printDoc;
    printPreviewDlg.ShowDialog(this);
}
```

![Figure 34: Print Preview Dialog Box](image.png)

## 5. Print

This option will send the diagram document to the printer.

The following code snippet can be used for sending the document for printing.

```csharp
[C#]
if (diagram1 != null)
{
    PrintDocument printDoc = diagram1.CreatePrintDocument();
    PrintDialog printDlg = new PrintDialog();
    printDlg.Document = printDoc;
}
```

## API Reference

### PrintDocument

- **Method: CreatePrintDocument**
  - **Description:** Creates a `PrintDocument` object for printing the diagram.

### PrintPreviewDialog

- **Property: StartPosition**
  - **Type:** FormStartPosition
  - **Default:** FormStartPosition.CenterScreen
  - **Description:** Specifies the starting position of the Print Preview Dialog.

### PrintSettings

- **Properties:**
  - **FromPage:** Specifies the starting page number.
  - **ToPage:** Specifies the ending page number.
  - **PrintRange:** Specifies the range of pages to print (e.g., AllPages, PageRange).

## Code Examples

### Printing a Diagram

```csharp
[C#]
if (diagram1 != null)
{
    PrintDocument printDoc = diagram1.CreatePrintDocument();
    PrintDialog printDlg = new PrintDialog();
    printDlg.Document = printDoc;
    if (printDlg.ShowDialog() == DialogResult.OK)
    {
        printDoc.Print();
    }
}
```

<!-- tags: [diagram, print, printpreviewdialog, printdialog, printdocument, windowsforms, syncfusion] keywords: [diagram printing, print options, print preview, print range, print dialog, windows forms, syncfusion winforms] -->
```