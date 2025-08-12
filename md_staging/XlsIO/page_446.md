```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_446.jpeg
document_name: XlsIO
page_number: 446
page_id: XlsIO#page_446
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:16:13Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Explains how to compress directories using the `AddDirectory` method.
- Demonstrates adding all files inside a directory using the `AddItem` method.
- Provides examples in C# and VB.NET for adding files to a ZIP archive.
- Illustrates how to zip all files in subfolders using the `Syncfusion.Compression.Zip` namespace.

## Content

### Adding Files to a ZIP Archive

#### For compressing directories, you can make use of the AddDirectory method. The AddDirectory method adds an empty directory file to a ZipArchive. If you want to add all the files inside the directory, then you should manually add these files by using the AddItem method.

For example, you can use the following code to add the file from the local drive.

#### C#

```csharp
string fileName = @"C:\Form1.cs";
Syncfusion.Compression.Zip.ZipArchive zipArchive = new Syncfusion.Compression.Zip.ZipArchive();
zipArchive.DefaultCompressionLevel = Syncfusion.Compression.CompressionLevel.Best;
Stream stream = new FileStream(fileName, FileMode.Open, FileAccess.Read);
FileAttributes attributes = File.GetAttributes(fileName);
Syncfusion.Compression.Zip.ZipArchiveItem item = new Syncfusion.Compression.Zip.ZipArchiveItem("Form1.cs", stream, true, attributes);
zipArchive.AddItem(item);
zipArchive.Save(@"c:\\SyncfusionCompressFileSample.zip");
zipArchive.Close();
```

#### VB.NET

```vb
Dim fileName As String = "C:\Form1.cs"
Dim zipArchive As New Syncfusion.Compression.Zip.ZipArchive()
zipArchive.DefaultCompressionLevel = Syncfusion.Compression.CompressionLevel.Best
Dim stream As IO.Stream = New IO.FileStream(fileName, FileMode.Open, FileAccess.Read)
Dim attributes As IO.FileAttributes = File.GetAttributes(fileName)
Dim item As New Syncfusion.Compression.Zip.ZipArchiveItem("Form1.cs", stream, True, attributes)
zipArchive.AddItem(item)
zipArchive.Save("c:\\SyncfusionCompressFileSample.zip")
zipArchive.Close()
```

### How to zip all the files in subfolders using the Syncfusion.Compression.Zip namespace?

The following code example illustrates how to zip all files in subfolders in XlsIO by using the Syncfusion.Compression.Zip namespace.

## API Reference

### Zip Archive Operations
- **AddDirectory()**: Adds an empty directory to a zip archive.
- **AddItem()**: Adds specific files or streams to a zip archive.
- **Save()**: Saves the zip archive to a specified location.

### Compression Levels
- **Best**: Specifies the compression level for the zip archive.

## Code Examples

#### Zipping Files in Subfolders
- Use the `Syncfusion.Compression.Zip` namespace to zip all files in subfolders.

<!-- tags: [XlsIO, Compression, Zip, AddDirectory, AddItem, WinForms, Syncfusion Windows Forms] keywords: [AddDirectory, AddItem, ZipArchive, FileStream, CompressionLevel, Syncfusion, XlsIO] -->
```