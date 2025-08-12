```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_255.jpeg
document_name: chart
page_number: 255
page_id: chart#page_255
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:30:05Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Symbol Styling Example

```csharp
series1.Styles(0).Symbol.Shape = ChartSymbolShape.Image

// Symbol set for specific data points (Second point here)
series1.Styles(1).Images = New ChartImageCollection(Me.imageList1.Images)
series1.Styles(1).Symbol.ImageIndex = 1
series1.Styles(1).Symbol.Size = New Size(20, 20)
series1.Styles(1).Symbol.Shape = ChartSymbolShape.Image
```

### See Also

- [Area Charts](Area%20Charts)
- [Bar Charts](Bar%20Charts)
- [Bubble Chart](Bubble%20Chart)
- [Column Charts](Column%20Charts)
- [Line Charts](Line%20Charts)
- [Candle Chart](Candle%20Chart)
- [Renko chart](Renko%20chart)
- [Three Line Break Chart](Three%20Line%20Break%20Chart)
- [Box and Whisker Chart](Box%20and%20Whisker%20Chart)
- [Gantt Chart](Gantt%20Chart)
- [Tornado Chart](Tornado%20Chart)
- [Polar and Radar Chart](Polar%20and%20Radar%20Chart)

### 4.5.1.39 Images

Gets / sets the imagelist that is to be associated with this ChartPoint. This property is used in conjunction with the **ImageIndex** property to display images associated with this point.

| **Possible Values** | Value that represents the custom ImageList. |
| --- | --- |
| **Default Value** | None |
| **2D / 3D Limitations** | No |
| **Applies to Chart Element** | All series and points |
| **Applies to Chart Types** | Area Charts, Bar Charts, Bubble Chart, Column Charts, Line Charts, Candle Chart, Renko chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Tornado Chart, Polar and Radar Chart |

Here is some sample code.

```csharp
[C#]

// Setting Images For the Series1
```
<!-- tags: [product, essential chart, windows forms, series styling, images] -->
```