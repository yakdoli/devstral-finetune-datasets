```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_074.jpeg
document_name: grid
page_number: 074
page_id: grid#page_074
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:21:03Z
fidelity: lossless
-->

## Essentials for Windows Forms

### Setting the Anchor Property

#### Figure 39: Setting the Anchor Property

12. To allow grouping at run time, the Grid Grouping control displays a drop panel onto which the user can drag columns to be grouped. To display this drop panel, you need to set the **ShowGroupDropArea** property to `true` as shown in the following screen shot.

#### Figure 40: Adding the Group Drop Area

Figure 39 demonstrates the process of setting the **Anchor** property, which defines the edges of the container to which a specific control or component is anchored. The screen shot shows the **gridGroupingControl1** in the Properties panel where the **Anchor** property is set to **Bottom, Left, Right**.

Figure 40 highlights the configuration of the **gridGroupingControl1** where the **ShowGroupDropArea** property is set to `True`. This setting enables the display of the group drop area, allowing users to drag column headers into it for runtime grouping functionality.

## API Reference

### Properties
- **Anchor**: Defines the edges of the container to which a specific control or component is anchored.
- **ShowGroupDropArea**: Controls the display of the group drop area for runtime column grouping.

### Methods
- **RaiseSourceListChange**: Handles changes to the source list that affects the grid.

### Events
- (No specific events listed in the screenshot.)

## Code Examples

```csharp
// Example to set the Anchor property
gridGroupingControl1.Anchor = AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;

// Example to enable the group drop area
gridGroupingControl1.ShowGroupDropArea = true;
```

## Cross References

See also:
- [Grid Grouping Control Documentation](https://www.syncfusion.com/documentation/windowsforms/griddatumapping)
- [Essential Grid for Windows Forms User Guide](https://www.syncfusion.com/documentation/windowsforms/grid)

<!-- tags: [Syncfusion Winforms, Grid, Grouping Control, Group Drop Area, Anchor, Property Settings] keywords: [Runtime Grouping, Grid Display, Grouping Panel, Column Drag, Grid Configuration, Property Grid, GroupDropArea, AnchorStyles] -->
```