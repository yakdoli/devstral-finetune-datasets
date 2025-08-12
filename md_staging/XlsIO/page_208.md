```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_208.jpeg
document_name: XlsIO
page_number: 208
page_id: XlsIO#page_208
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:02:39Z
fidelity: lossless
-->

# Essential XlsIO

It supports the insertion of **Scalar** and **Vector** images in a worksheet. It is also possible to position and set the properties for the image at the desired location. `IPictureShape` is used for inserting and formatting pictures.

## Code Examples

### Inserting and Formatting Images

The following examples demonstrate how to insert an image into a worksheet and set its position and dimensions using `IPictureShape` in both C# and VB.NET.

#### C#
```csharp
// Inserting image
IPictureShape shape = sheet.Pictures.AddPicture(1, 1, "sample.jpg");
shape.Top = 1157;
shape.Height = 808;
shape.Left = 1417;
shape.Width = 1121;
```

#### VB.NET
```vb.net
' Inserting image
Dim shape As IPictureShape = sheet.Pictures.AddPicture(1, 1, "sample.jpg")
shape.Top = 1157
shape.Height = 808
shape.Left = 1417
shape.Width = 1121
```

<!-- tags: [Syncfusion, Winforms, XlsIO, IPictureShape, Image Insertion, C#, VB.NET] keywords: [Scalar, Vector, Images, Worksheet, Position, Formatting, IPictureShape, AddPicture, C#, VB.NET] -->
```