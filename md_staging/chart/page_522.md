```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_522.jpeg
document_name: chart
page_number: 522
page_id: chart#page_522
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:49:14Z
fidelity: lossless
-->

## Chart with Skins

### Overview
- The charts demonstrate how different skins alter the visual appearance of the same data series.
- The charts show varying aesthetics when the "Skins" value is set to either "Olive" or "Sandune."

### Content

#### Figure 341: Olive

The first chart, displayed below, showcases a data series labeled "Series" with points plotted on a two-dimensional axis. The chart has a greenish "Olive" skin that provides a vibrant and fresh visual aesthetic.

```markdown
Figure: Chart with Skins
```

##### Chart Details:
- **Skins Value**: Olive
- **Series**: Data points are plotted along an x-axis ranging from 0 to 10 and a y-axis ranging from 10 to 60.
- **Data Points**: Various data points distributed unevenly across the axes, indicating a scattered dataset.

---

#### Figure 342: Sandune

The second chart illustrates the same data series, but with a skin named "Sandune." This skin provides a warmer, earthy tone, contrasting with the "Olive" skin.

```markdown
Figure: Chart with Skins
```

##### Chart Details:
- **Skins Value**: Sandune
- **Series**: The same data points as in the previous chart are plotted, maintaining consistency in the dataset.
- **Visual Style**: The warm, beige color scheme of the "Sandune" skin gives the chart a more neutral and natural appearance.

### Conclusion

The charts demonstrate how Syncfusion's chart skins can be utilized to customize the visual style of Windows Forms charts, catering to different design preferences while preserving the integrity of the underlying data.

#### API Reference
- **Namespaces**: `Syncfusion.Windows.Forms.Chart`
- **Properties**:
  - `Skins`: This property allows setting the skin theme of the chart to enhance its visual appeal.

```csharp
chart.Skins = Skins.Olive; // Example: Setting the skin to Olive
```

### Cross References
- Refer to the Syncfusion Windows Forms documentation for more detailed examples and properties related to chart skins.

<!-- tags: chart, skins, windows forms, syncfusion, visual aesthetics, data series, chart customization, skins value, olive, sandune keywords: skins, windows forms, syncfusion, chart aesthetic, data series, chart customization, olive, sandune -->
``` 
```