```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_092.jpeg
document_name: XlsIO
page_number: 092
page_id: XlsIO#page_092
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:54:47Z
fidelity: lossless
-->

## Reducing size of Excel 2007 & Excel 2010 files

### Overview
- The default compression technique, using .NET compression, is replaced with a new technique to reduce the size of XLSX files.
- The reduced file size leads to decreased data transfer between applications.
- The Compression level can be set at the IApplication interface to apply to all workbooks created using the same instance of Excel Engine.

### Content

#### 3.7.2.1 Reducing size of Excel 2007 & Excel 2010 files

The default compression technique, using which Essential XlsIO compresses files uses .NET compression. A new compression technique has been implemented that will considerably reduce the size of the compressed XLSX files.

##### Use Case Scenarios

The reduced size of the compressed file will result in reduced data transfer between applications.

##### How Compression level can be set

The Compression level can be set at IApplication interface. This will set the level for all the workbooks created using the same instance of Excel Engine.

##### C# Code Example

```csharp
ExcelEngine excelEngine = new ExcelEngine();
IApplication application = excelEngine.Excel;

application.DefaultVersion = ExcelVersion.Excel2007; // or ExcelVersion.Excel2010;
application.CompressionLevel = Syncfusion.Compression.CompressionLevel.Best;

workbook.SaveAs(fileName);
workbook.Close();
excelEngine.Dispose();
```

##### VB.NET Code Example

```vb
Dim excelEngine As New ExcelEngine()
Dim application As IApplication = excelEngine.Excel
application.DefaultVersion = ExcelVersion.Excel2007 ' or ExcelVersion.Excel2010
application.CompressionLevel = Syncfusion.Compression.CompressionLevel.Best

workbook.SaveAs(fileName)
```

## API Reference

- **Namespace**: Syncfusion.Compression
- **Enum**: CompressionLevel
  - **Members**:
    - **Best**: Indicates the highest level of compression.
    - **Fast**: Indicates faster compression with less data reduction.
    - **High**: Indicates higher compression with more data reduction.
    - **Normal**: Indicates standard compression.
  
## Code Examples

### C# Example

The provided C# example demonstrates setting the Compression level to `Best` and saving the workbook.

### VB.NET Example

The provided VB.NET example mirrors the C# example, setting the Compression level to `Best` and saving the workbook.

### See also

- Excel 97 to 2003
- SpreadsheetML
- CSV format

<!-- tags: [product, module, control, api, version?] keywords: [compression, xlsx, file size, data transfer, excel engine, syncfusion] -->
```