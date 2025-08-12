```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_272.jpeg
document_name: pdf
page_number: 272
page_id: pdf#page_272
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:27Z
fidelity: lossless
-->

# Essential PDF

```vb.net
doc.ImportPage(ldDoc, page)
doc.ImportPage(ldDoc, pageindex)
doc.ImportPageRange(ldDoc, startPageIndex, endPageIndex)
```

**Note:** The first two methods in the above code are just shortcuts to the last one, which is a powerful tool appending not just pages, but annotations and forms as well.

The parameters included are as follows.

- **IdDoc**: Loaded PDF document
- **Page**: Page that should be appended (not a page itself, but its valid representation)
- **PageIndex**: Index of the page
- **StartPageIndex, endPageIndex**: Indices specifying the page range

The following code snippets illustrate how to import a page to the existing document.

### Importing a Page in C#

```csharp
PdfLoadedDocument ldDoc = new PdfLoadedDocument(filename);
int startIndex = 0;
int endIndex = ldDoc.Pages.Count - 1;
newDoc.ImportPageRange(ldDoc, startIndex, endIndex);
newDoc.Save(newFilename);
newDoc.Close();
ldDoc.Close();
```

### Importing a Page in VB.NET

```vb.net
Dim ldDoc As PdfLoadedDocument = New PdfLoadedDocument(filename)
Dim startIndex As Integer = 0
Dim endIndex As Integer = ldDoc.Pages.Count - 1
NewDoc.ImportPageRange(ldDoc, startIndex, endIndex)
NewDoc.Save(NewFilename)
NewDoc.Close()
ldDoc.Close()
```

## Implementation Note

<!-- tags: [pdf, document, import, annotation, form, append, range, control] keywords: [importPage, importPageRange, annotations, forms, pdf document, startIndex, endIndex, newDocument], [VB.NET, C#, Syncfusion, document manipulation] -->
```