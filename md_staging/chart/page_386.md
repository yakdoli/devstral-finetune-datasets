```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_386.jpeg
document_name: chart
page_number: 386
page_id: chart#page_386
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:40:03Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

By default, this additional axis will be rendered right next to the corresponding primary axis as seen above. This might be undesirable and you would instead want it to be rendered at the opposite side of the primary axis. This is done by setting the `OpposedPosition` property to `true`. Read more on Opposed Axis [here](#).

![Multiple Axes in Opposed Position](ChartControl with a 2nd X-Axis in Opposed Position)

**Figure 251: ChartControl with a 2nd X-Axis in Opposed Position**

## Stacked or SideBySide Position

By default, the secondary axes are rendered stacked over, or parallel, to the corresponding primary axis. And also sometimes rendered in a position opposite to the primary axis as shown in the above screenshots. This is because the `XAxisLayoutMode` and `YAxisLayoutMode` properties are set to `Stacking` by default.

However, you might want the secondary axis to be rendered in-line, side-by-side to the primary axis. You can do by setting the `XAxisLayoutMode` and `YAxisLayoutMode` properties to `SideBySide`.

Here is a code sample.

### Code Example

```csharp
this.ChartControl1.ChartArea.XAxesLayoutMode =
ChartAxesLayoutMode.SideBySide;
```

<!-- tags: [chart, windows forms, axes configuration, Syncfusion, Stacked or SideBySide Position, XAxisLayoutMode, YAxisLayoutMode] keywords: [primary axis, secondary axis, opposed axis, multiple axes, opposed position, stacking mode, side-by-side layout] -->
```