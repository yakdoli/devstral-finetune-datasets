```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_200.jpeg
document_name: XlsIO
page_number: 200
page_id: XlsIO#page_200
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:02:10Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
sheet.Move(2);
```

## Convert To Image

### Overview
- Essential XlsIO can convert a worksheet to an image of type bitmap or metafile based on the input range of rows and columns.
- All basic formats are preserved during conversion.
- The sheet can be converted and saved to disk or stream.
- The converted image can be inserted into a PDF by using Essential PDF.

### Content

Essential XlsIO can convert a worksheet to an image of type bitmap or metafile based on the input range of rows and columns with all basic formats preserved. The sheet can be converted and saved to disk or stream. The converted image can be inserted in a pdf by using Essential PDF.

For more information on insertion of images in PDF, refer the following link:

> http://help.syncfusion.com/ug_82sp/Reporting_XlsIO/defaultWPF.html

### C#

```csharp
// Convert as bitmap.
Image img = sheet.ConvertToImage(1, 1, 10, 20);
img.Save("Sample.png", ImageFormat.Png);

// Converts to Metafile.
Image img = sheet.ConvertToImage(1, 1, 10, 20, ImageType.Metafile, null);
img.Save("Sample.emf", ImageFormat.Emf);

// Converts and save as stream.
MemoryStream stream = new MemoryStream();
sheet.ConvertToImage(1, 1, 10, 20, ImageType.Metafile, stream);
```

### VB

```vb
' Convert as bitmap.
Dim img As Image = sheet.ConvertToImage(1, 1, 10, 20)
img.Save("Sample.png", ImageFormat.Png)

' Converts to Metafile.
Dim img As Image = sheet.ConvertToImage(1, 1, 10, 20, ImageType.Metafile, Nothing)
img.Save("Sample.emf", ImageFormat.Emf)

' Converts and save as stream.
Dim stream As MemoryStream = New MemoryStream()
sheet.ConvertToImage(1, 1, 10, 20, ImageType.Metafile, stream)
```

## Cross References
- For more information on insertion of images in PDF, see the link provided:
  > http://help.syncfusion.com/ug_82sp/Reporting_XlsIO/defaultWPF.html

<!-- tags: [Essential XlsIO, Conversion, Image, Bitmap, Metafile, PDF, Syncfusion Winforms, Reporting_XlsIO]
keywords: [convert, worksheet, image, bitmap, metafile, preserve formats, disk, stream, Essential PDF, insertion, images, pdf, reporting, syncfusion, winforms] -->
```