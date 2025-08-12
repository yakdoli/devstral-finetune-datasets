<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_023.jpeg
document_name: PDF Viewer
page_number: 023
page_id: PDF Viewer#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:51:07Z
fidelity: lossless
-->

# Essential PDF Viewer

## 4.1.4 Exporting PDF

### 4.1.4.1 Exporting PDFs as Raster Images

Essential PDF Viewer allows selected pages to be exported as raster images. Exporting can be done using the `ExportAsImage` method. This option helps to convert a PDF into an image.

```csharp
[C#]
Bitmap img = pdfViewer1.ExportAsImage(0);

// Save the image.
img.Save("Sample.png", ImageFormat.Png);
```

```vbnet
[VB.NET]
Dim img As Bitmap = pdfViewer1.ExportAsImage(0)

' Save the image.
img.Save("Sample.png", ImageFormat.Png)
```

You can also specify the page range instead of converting each page.

```csharp
[C#]
Bitmap[] img = pdfViewer1.ExportAsImage(0, 3);
```

```vbnet
[VB.NET]
Dim img() As Bitmap = pdfViewer1.ExportAsImage(0, 3)
```

### 4.1.4.2 Exporting PDFs as Vector Images

Exporting PDFs as vector images can be done using the `ExportAsMetafile` method. The following code sample demonstrates how a PDF document can be exported as a metafile.

```csharp
[C#]
Metafile img = pdfViewer1.ExportAsMetafile(0);

// Save the image
img.Save("Sample.emf", ImageFormat.Emf);
```

## API Reference

- **Method**: `ExportAsImage`
  - Converts a PDF page to a raster image.
  - Parameters:
    - `pageIndex`: Specifies the page index to be exported.
  - Returns: `Bitmap` object representing the raster image.

- **Method**: `ExportAsMetafile`
  - Converts a PDF page to a vector image in metafile format.
  - Parameters:
    - `pageIndex`: Specifies the page index to be exported.
  - Returns: `Metafile` object representing the vector image.

## Code Examples

### Exporting a PDF Page as a Raster Image (C#)

```csharp
[C#]
Bitmap img = pdfViewer1.ExportAsImage(0);
img.Save("Sample.png", ImageFormat.Png);
```

### Exporting a PDF Page as a Vector Image (C#)

```csharp
[C#]
Metafile img = pdfViewer1.ExportAsMetafile(0);
img.Save("Sample.emf", ImageFormat.Emf);
```

### Exporting a PDF Page as a Raster Image (VB.NET)

```vbnet
[VB.NET]
Dim img As Bitmap = pdfViewer1.ExportAsImage(0)
img.Save("Sample.png", ImageFormat.Png)
```

### Exporting a PDF Page as a Vector Image (VB.NET)

```vbnet
[VB.NET]
Dim img As Metafile = pdfViewer1.ExportAsMetafile(0)
img.Save("Sample.emf", ImageFormat.Emf)
```

## Cross References

See also:  
- [Working with PDF Pages](#working-with-pdf-pages)  
- [PDF Viewer Controls](#pdf-viewer-controls)

<!-- tags: [syncfusion, pdfviewer, export, winforms, conversion, raster, vector] keywords: [exportasimage, exportasmetafile, pdf, image, bitmap, metafile, pdfviewer, windowsforms, syncfusionpdfviewer] -->