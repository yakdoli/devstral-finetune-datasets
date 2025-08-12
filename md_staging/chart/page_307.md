```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_307.jpeg
document_name: chart
page_number: 307
page_id: chart#page_307
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:32:54Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Chart Details

| **Possible Values**         | Any Possible Numeric Values |
| **Default Value**           | 0.5                         |
| **2D / 3D Limitations**    | No                          |
| **Applies to Chart Element**      | All Series                 |
| **Applies to Chart Types** | ScatterSplineChart          |

### Sample Code

Here is some sample code.

#### C#

```csharp
this.chartControl1.Series[i].ScatterConnectType = ScatterConnectType.Spline;
this.chartControl1.Series[i].ScatterSplineTension =3;
```

#### VB.NET

```vb
Private Me.chartControl1.Series(i).ScatterConnectType = ScatterConnectType.Spline
Private Me.chartControl1.Series(i).ScatterSplineTension =3
```

## Cross References
- See also: Related documentation sections or topics.
<!-- tags: [chart, ScatterSplineChart, chartControl1, ScatterConnectType, ScatterSplineTension] keywords: [possible values, default value, 2D/3D limitations, chart element] -->
```