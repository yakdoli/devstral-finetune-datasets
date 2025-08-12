```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_359.jpeg
document_name: pdf
page_number: 359
page_id: pdf#page_359
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:48:08Z
fidelity: lossless
-->

# Essential PDF

If CrossReferenceType property is specified by CrossReferenceStream, the cross-reference is represented by cross-reference stream. It may reduce the file size, especially if compression is turned on, but increases the file generation time.

## 5.1.2.5 How To Insert a Table In The Header?

- **PDFLightTable model of Essential PDF** provides an option to insert tables in headers by using page templates.

The following steps illustrate how to insert tables in the header:

1. Create a table with some datasource by using the PdfLightTable class.
2. Create a Page template where the table has to be placed.
3. Draw the table in the template.

You can also insert images and other graphical objects in the table cell and render it in the header.

### Code Example

```csharp
[C#]

//Create page template
PdfPageTemplateElement top = new PdfPageTemplateElement(rect);

//Create a table
PdfLightTable table = new PdfLightTable();
table.DataSource = dataTable;
table.Style.CellPadding = 16;

//Draw the table in template
table.Draw(top.Graphics);

//Place the template at the top.
doc.Template.Top = top;
```

<!-- tags: [pdf, header, table, page template] keywords: [essential pdf, table, header, page template, pdflighttable, cellpadding, graphics, template tops] -->
```