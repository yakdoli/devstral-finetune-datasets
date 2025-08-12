```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_154.jpeg
document_name: diagram
page_number: 154
page_id: diagram#page_154
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:18:12Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

**OrgChart Alignment**

As the OrgChartLayout follows a Waterfall model, whenever there is only one child node, the layout will be widened. To overcome this, Essential diagram enables you to align the single child node parallel to the parent node, which will reduce the layout structure.

### Code Examples

- **[C#]**
  ```csharp
  OrgChartLayoutManager manager = new OrgChartLayoutManager(this.diagram.Model, RotateDirection.TopToBottom, 20, 50, LayoutType.Waterfall, 1, true);
  ```

- **[VB]**
  ```vb
  Dim manager As New OrgChartLayoutManager(Me.diagram.Model, RotateDirection.TopToBottom, 20, 50, LayoutType.Waterfall, 1, True)
  ```

### 4.5.1.9 Layout Manager Settings

**Margin Properties for Layout Managers**

---

挦ease all rights reserved. |  154 |
```

<!-- tags: [product, module, control, api, version?] keywords: [orgchartlayout, waterfall model, alignment, layout properties, layoutmanager, orgchart, margin properties] -->
```