```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_948.jpeg
document_name: grid
page_number: 948
page_id: grid#page_948
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:51:24Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
void converter_QueryExportPreviewRowInfo(object sender, GroupingGridExportPreviewRowQueryInfoEventArgs e)
{
}
```

### [VB.NET]

```vb
Dim converter As GroupingGridExcelConverter = New GroupingGridExcelConverter()

AddHandler converter.QueryExportPreviewRowInfo, AddressOf converter_QueryExportPreviewRowInfo

Private Sub converter_QueryExportPreviewRowInfo(ByVal sender As Object, ByVal e As GroupingGridExportPreviewRowQueryInfoEventArgs)
End Sub
```

## Implementation

Here is an example that illustrates the conversion of a grouping grid to an Excel file.

1. Include the required namespaces.

### [C#]

```csharp
using Syncfusion.XlsIO;
using Syncfusion.GridExcelConverter;
using Syncfusion.GroupingGridExcelConverter;

using Syncfusion.Grouping;
using Syncfusion.Windows.Forms.Grid;
using Syncfusion.Windows.Forms.Grid.Grouping;
```

### [VB.NET]

```vb
Imports Syncfusion.XlsIO
Imports Syncfusion.GridExcelConverter
Imports Syncfusion.GroupingGridExcelConverter

Imports Syncfusion.Grouping
Imports Syncfusion.Windows.Forms.Grid
Imports Syncfusion.Windows.Forms.Grid.Grouping
```

<!-- tags: [product, module, control, api, version?] keywords: [getting started, Essential Grid, Windows Forms, Grouping Grid, Excel conversion, Example, namespaces, required namespaces, C# example, VB.NET example] -->
```