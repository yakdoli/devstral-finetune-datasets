```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_445.jpeg
document_name: XlsIO
page_number: 445
page_id: XlsIO#page_445
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:18:53Z
fidelity: lossless
-->

## 5.2.5 How to zip files using the Syncfusion.Compression.Zip namespace?

You can use the AddFile method of ZipArchive object to compress files by using XlsIO. Following code example illustrates how to use this method.

```csharp
// Suppress the summary rows at the bottom.
sheet.PageSetup.IsSummaryRowBelow = False
// Suppress the summary columns to the right.
sheet.PageSetup.IsSummaryColumnRight = False
```

### Code Example

**[C#]**

```csharp
Syncfusion.Compression.Zip.ZipArchive zipArchive = new Syncfusion.Compression.Zip.ZipArchive();
zipArchive.DefaultCompressionLevel = Syncfusion.Compression.CompressionLevel.Best;

// Add the file you want to zip.
zipArchive.AddFile("..\\..Form1.cs");

// Zip file name and location.
zipArchive.Save("SyncfusionCompressFileSample.zip");
zipArchive.Close();
```

**[VB.NET]**

```vb
Dim zipArchive As New Syncfusion.Compression.Zip.ZipArchive()
zipArchive.DefaultCompressionLevel = Syncfusion.Compression.CompressionLevel.Best

' Add the file you want to zip.
zipArchive.AddFile("..\\..Form1.cs")

' Zip file name and location.
zipArchive.Save("SyncfusionCompressFileSample.zip")
zipArchive.Close()
```

<!-- tags: [product, syncfusion, winforms, compression, zip, xslio, namespace, addfile, file compression] keywords: [zipfile, addfile method, compressionlevel, best compression, syncfusion.compression.zip, zip, xslio, page setup, summary rows, summary columns] -->
```