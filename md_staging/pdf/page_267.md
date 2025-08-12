<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_267.jpeg
document_name: pdf
page_number: 267
page_id: pdf#page_267
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:42:08Z
fidelity: lossless
-->

# Essential PDF

## Overview
- `PdfCompositeField`- Value of the field is composed of any number of other automatic fields

## Content

### PdfCreationDateField and PdfDateTimeField

PdfCreationDateField and PdfDateTimeField have the `DateFormatString` property, which defines the formatting string for the value of the field. This property uses the same formatting rules and specifiers as DateTime type of .NET. For detailed information on formatting specifiers, see [http://msdn2.microsoft.com/en-us/library/73ctwf33(VS.80).aspx](http://msdn2.microsoft.com/en-us/library/73ctwf33(VS.80).aspx).

### Drawing Automatic Fields

You can draw the Automatic Fields on the `PdfTemplate` and set them as the document template or manually draw them on the necessary pages. The values of the fields will be automatically populated on each copy of the template.

### Inserting Dynamic Fields

The following code example illustrates how to insert dynamic fields such as page number, count, datetime, composite fields, and so on, into the existing document.

### Code Example: Inserting Dynamic Fields

#### C#

```csharp
PdfLoadedDocument doc = new PdfLoadedDocument(@"../../Sample.pdf");
PdfFont font = new PdfStandardFont(PdfFontFamily.Helvetica, 12);

// Create page number field
PdfPageNumberField pageNumber = new PdfPageNumberField(font, PdfBrushes.Black);

// Create page count field
PdfPageCountField count = new PdfPageCountField(font, PdfBrushes.Black);
PdfDateTimeField datetimefield = new PdfDateTimeField(font, PdfBrushes.Black);
PdfCompositeField compositeField = new PdfCompositeField(font, PdfBrushes.Black, "Page {0} of {1}{2}", pageNumber, count, datetimefield);
compositeField.Bounds = new RectangleF(0, 0, 250, 100);
compositeField.Draw(doc.Pages[0].Graphics, new PointF(0, 0));

PdfCreationDateField datefield = new PdfCreationDateField(font, PdfBrushes.Black);
```

#### VB.NET

```vb
Dim doc As New PdfLoadedDocument("../../Sample.pdf")
Dim font As PdfFont = New PdfStandardFont(PdfFontFamily.Helvetica, 12)

' Create page number field
Dim pageNumber As New PdfPageNumberField(font, PdfBrushes.Black)
```

### Additional Notes
- Dynamic fields such as page number, count, and datetime can be easily added to documents using the provided API.
- The `PdfCompositeField` allows the creation of composite fields that combine multiple fields into a single formatted output.
- The `DateFormatString` property is used for customizing the date and time format in fields like `PdfCreationDateField` and `PdfDateTimeField`.

## Cross References
- For more information on formatting specifiers, see [http://msdn2.microsoft.com/en-us/library/73ctwf33(VS.80).aspx](http://msdn2.microsoft.com/en-us/library/73ctwf33(VS.80).aspx).

<!-- tags: [Syncfusion Winforms, Essential PDF, Automatic Fields, DateTimeFields, PageFields, C#, VB.NET] keywords: [PdfLoadedDocument, PdfPageNumberField, PdfPageCountField, PdfDateTimeField, PdfCompositeField, DateFormatString, datefield, datetimefield, page number, count, datetime] -->