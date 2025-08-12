```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_216.jpeg
document_name: chart
page_number: 216
page_id: chart#page_216
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:29:33Z
fidelity: lossless
-->

## 4.5.1.19 EnablePhongStyle

Specifies if the PhongStyle is enabled.

### Details

| **Possible Values** | **True or False** |
| -------------------- | ----------------- |
| **Default Value**    | **True**         |
| **2D / 3D Limitations** | **No**           |
| **Applies to Chart Element** | **All Series** |
| **Applies to Chart Types** | **Bubble Chart** |

### Sample Code

Here is some sample code.

```csharp
[this.chartControl1.Series[0].ConfigItems.BubbleItem.EnablePhongStyle = false;]
```

```vb.net
[Me.chartControl1.Series(0).ConfigItems.BubbleItem.EnablePhongStyle = False]
```
<!-- tags: [syncfusion, windows forms, chart, enablephongstyle, control, api, 11.4.0.26] keywords: [phongstyle, enabling,bubble chart, syndfusion windows forms chart, enablephongstyleproperty-msdn] -->
```