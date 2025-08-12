```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_129.jpeg
document_name: diagram
page_number: 129
page_id: diagram#page_129
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:16:50Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Position

| Property | Description | Parameters | Type | Return Type | Reference links |
| --- | --- | --- | --- | --- | --- |
| Position | Gets or sets the<br>position of the<br>label. | NA | Position | NA | NA |

## Methods

### Table 2: Methods Table

| Method | Description | Parameters | Type | Return Type | Reference links |
| --- | --- | --- | --- | --- | --- |
| GetPosition | Gets the label position in the node coordinates. | Empty | NA | PointF | NA |
| GetStringFormat | Creates a StringFormat object that encapsulates the properties of the text object. | Empty | NA | StringFormat | NA |

## Adding a Label to an Application

You can create a label as illustrated in the following code example:

```csharp
RoundRect node = new RoundRect(0, 0, 170, 100,MeasureUnits.Pixel);

// Create a label with predefined position
Syncfusion.Windows.Forms.Diagram.Label lbl_TopCenter = new Syncfusion.Windows.Forms.Diagram.Label(node, "Label_TopCenter");
// Position the label
lbl_TopCenter.Position = Position.TopCenter;
/* Position enum has the values Center, TopLeft, TopCenter, TopRight, MiddleLeft, MiddleRight, BottomLeft, BottomCenter, BottomRight and Custom */

// Apply font style
lbl_TopCenter.FontStyle.Bold = true;
lbl_TopCenter.FontStyle.Family = "Corbel";
lbl_TopCenter.FontStyle.Size = 9;
// Add the label to node's label collection
node.Labels.Add(lbl_TopCenter);
```

## API Reference (if applicable)
- **Namespace**: Syncfusion.Windows.Forms.Diagram
- **Class**: Label
- **Methods**:
  - **GetPosition**:
    - **Parameters**: None
    - **Type**: NA
    - **Return Type**: PointF
  - **GetStringFormat**:
    - **Parameters**: None
    - **Type**: NA
    - **Return Type**: StringFormat

## Code Examples (multi-language supported)
- **C#**:
  ```csharp
  // Sample code as shown above
  ```

<!-- tags: [syncfusion, windowsforms, label, position, method, stringformat, essentialdiagram] keywords: [label, position, getposition, getstringformat, node, topcenter, fontstyle, corbel] -->
```