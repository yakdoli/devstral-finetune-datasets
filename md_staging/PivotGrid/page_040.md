```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_040.jpeg
document_name: PivotGrid
page_number: 040
page_id: PivotGrid#page_040
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:55:46Z
fidelity: lossless
-->

## Essential PivotGrid WindowsForms

```csharp
pd.DrawGridPrintFooter += new GridPrintDocumentAdv.DrawGridHeaderFooterEventHandler(pd_DrawGridPrintFooter);
```

### [VB]

```vb
AddHandler pd.DrawGridPrintHeader, AddressOf pd_DrawGridPrintHeader
AddHandler pd.DrawGridPrintFooter, AddressOf pd_DrawGridPrintFooter
```

The following image shows the printed output of the pivot grid:

![Pivot Grid in Print Preview](https://i.imgur.com/unclear.jpg)

**Figure 15: Pivot Grid in Print Preview**

### Sample Link

A sample is available in the following location:

```
<Installed Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\PivotGrid.Windows\Samples\1.0\Pivot\Print\Print Grid Demo
```

## API Reference

### Namespace: Syncfusion.Windows.Forms.PivotGrid

#### Methods
- `DrawGridPrintHeader()`
- `DrawGridPrintFooter()`

### Properties
- `DrawGridPrintHeader`
- `DrawGridPrintFooter`

## Code Examples

### C#

```csharp
pd.DrawGridPrintFooter += new GridPrintDocumentAdv.DrawGridHeaderFooterEventHandler(pd_DrawGridPrintFooter);
```

### VB.NET

```vb
AddHandler pd.DrawGridPrintHeader, AddressOf pd_DrawGridPrintHeader
AddHandler pd.DrawGridPrintFooter, AddressOf pd_DrawGridPrintFooter
```

## Cross References

See also:

- [PivotGrid Documentation](https://www.syncfusion.com/documentation/windowsforms/pivotgrid)
- [EssentialStudio Samples](https://www.syncfusion.com/downloads/community-edition/latest)

<!-- tags: PivotGrid, WindowsForms, Print, Grid, Syncfusion, 11.4.0.26 keywords: PivotGrid, Print, DrawGridPrintFooter, DrawGridPrintHeader -->
```