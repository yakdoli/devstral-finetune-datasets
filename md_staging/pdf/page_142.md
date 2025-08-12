```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_142.jpeg
document_name: pdf
page_number: 142
page_id: pdf#page_142
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:33:18Z
fidelity: lossless
--> 

## Customizing Cell Styles in WinForms DataGridView

### Overview
- Learn how to specify an alternate style using the AlternateStyle property.
- Customize the appearance of odd row cells.
- Understand properties like BackgroundBrush, Border, Font, etc., for cell styling.
- Explore the Style property to specify font and appearance attributes.
- Use BeginCellLayout and EndCellLayout events for different styles.

### Properties

| Name              | Description                                                                                       | Data Type       |
|-------------------|---------------------------------------------------------------------------------------------------|-----------------|
| BackgroundBrush   | Gets or sets the brush with which the background will be drawn                                     | PdfBrush        |
| Border            | Gets or sets the pen with which the border will be drawn                                           | PdfPen          |
| Font              | Gets or sets the font                                                                            | PdfFont         |
| StringFormat      | Gets or sets the string format of the text                                                       | PdfStringFormat |
| TextBrush         | Gets or sets the brush, which will be used to draw font                                          | PdfBrush        |
| TextPen           | Gets or sets the pen, which will be used to draw text outlines                                    | PdfPen          |

### Customizing Cell Styles

The Style property enables you to specify the font along with its appearance (brush, pen, and string format), and border along with the background of cells. While there are fixed properties for styles, you can specify different styles using **BeginCellLayout** and **EndCellLayout** events.

#### C#

```csharp
PdfCellStyle altStyle = new PdfCellStyle(font, PdfBrushes.White, PdfPens.Green);
altStyle.BackgroundBrush = PdfBrushes.DarkGray;

PdfCellStyle headerStyle = new PdfCellStyle(font, PdfBrushes.White, PdfPens.Brown);
headerStyle.BackgroundBrush = PdfBrushes.Red;

pdfLightTable.Style.AlternateStyle = altStyle;
pdfLightTable.Style.HeaderStyle = headerStyle;
```

#### VB.NET

```vb
Dim altStyle As Syncfusion.Pdf.Tables.PdfCellStyle = New Syncfusion.Pdf.Tables.PdfCellStyle(Font, PdfBrushes.White, 
```

<!-- tags: [winforms, datagridview, pdf, cellstyle, table, alternatestyle, headerstyle] keywords: [customization, styling, alternate rows, backgroundbrush, border, textbrush, textpen] -->
```