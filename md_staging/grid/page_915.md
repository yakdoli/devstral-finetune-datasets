```html
<!-- source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_915.jpeg
document_name: grid
page_number: 915
page_id: grid#page_915
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:49:31Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Model Based Selection Illustrated

![Figure 331: Model Based Selection Illustrated](https://i.imgur.com/qOxqZ3G.png)

#### Format Selection

It is possible to modify the default color used for alpha blend selection. This can be achieved by assigning a desired color to the AlphaBlendSelectionColor property. The example given below uses Red Color for alpha blending.

[C#]

```csharp
this.gridGroupingControl1.TableOptions.AllowSelection = GridSelectionFlags.AlphaBlend | GridSelectionFlags.Cell;
this.gridGroupingControl1.TableModel.Options.AlphaBlendSelectionColor = Color.Red;
```

[VB.NET]

```vb
Me.gridGroupingControl1.TableOptions.AllowSelection = GridSelectionFlags.AlphaBlend Or GridSelectionFlags.Cell
Me.gridGroupingControl1.TableModel.Options.AlphaBlendSelectionColor = Color.Red
```
```