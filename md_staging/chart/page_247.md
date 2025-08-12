```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_247.jpeg
document_name: chart
page_number: 247
page_id: chart#page_247
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:29:40Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Pie Chart with HeightByAreaDepth Enabled

![](https://example.com/image.png)

**Figure 146: Pie Chart with HeightByAreaDepth Enabled**

## See Also

**Pie Chart** [Pie Chart](Pie Chart)

---

### 4.5.1.35 HeightCoefficient

When in 3D mode, the relative height of the pie chart can be specified via the property. Note that the `HeightByAreaDepth` property should be set as false for this to take effect.

#### Details

| **Attributes**            | **Description**                                                |
|---------------------------|---------------------------------------------------------------|
| **Possible Values**       | Valid Ranges From 0 to 1                                      |
| **Default Value**         | 0.2                                                           |
| **2D / 3D Limitations**  | 3D Only                                                       |
| **Applies to Chart Element** | All series                                                   |
| **Applies to Chart Types** | Pie Chart                                                    |

## API Reference

---

## Code Examples

### Sample Code Snippet

```csharp
// Example usage of HeightCoefficient in a Pie Chart
chart.PieSeries.Add(series =>
{
    series.HeightCoefficient = 0.5;
    series.HeightByAreaDepth = false;
});
```

---

## Cross References

See also: [Pie Chart](Pie Chart)

---

### Legal Notices

© 2013 Syncfusion. All rights reserved.
```