```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_231.jpeg
document_name: edit
page_number: 231
page_id: edit#page_231
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:07:53Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
// Print the current page.
this.editControl1.PrintCurrentPage();

// Print the entire document.
this.editControl1.PrintNoDialog();

// Print the selected area.
this.editControl1.PrintPages(1, 10);

// Print the pages in the specified range.
this.editControl1.PrintSelection();
```

### [VB.NET]

```vb.net
' Print the current page.
Me.editControl1.PrintCurrentPage()

' Print the entire document.
Me.editControl1.PrintNoDialog()

' Print the selected area.
Me.editControl1.PrintPages(1, 10)

' Print the pages in the specified range.
Me.editControl1.PrintSelection()
```

## Customized Header Footer

Header and Footer can be shown / hidden while printing the document by using the `PageHeaderAndFooterVisible` property.

The following properties are used to print the contents of the editor, the document name as the header, and the page number as footer.

| Edit Control Property      | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| PrintDocument              | Gets print document, that can be used to print the contents of the editor. |
| PrintDocumentName          | Gets / sets value indicating whether the document name should be printed.   |
| PrintPageNumber            | Gets / sets value indicating whether the page number should be printed.     |

<!-- tags: [Syncfusion Winforms, Essential Edit, Print, VB.NET, Header Footer, Document Name, Page Number] keywords: [document, header, footer, print, properties, control, custom, editing] -->
```