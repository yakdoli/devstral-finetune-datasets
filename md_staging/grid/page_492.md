```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_492.jpeg
document_name: grid
page_number: 492
page_id: grid#page_492
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:20:00Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Custom Colors

We can apply custom colors to the `TabBarSplitterControl` by setting the `Office2007ColorScheme` property to "Managed" and by giving the color through the `ApplyManagedColor` method as follows.

```csharp
this.tabBarSplitterControl.Office2007ColorScheme =
    Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(this, Color.PowderBlue);
```

```vb
Me.tabBarSplitterControl.Office2007ColorScheme =
    Syncfusion.Windows.Forms.Office2007Theme.Managed
Office2007Colors.ApplyManagedColors(Me, Color.PowderBlue)
```

![Custom Color of Tab Bar Splitter Control set to "PowderBlue"](image.png)

**Figure 190: Custom Color of Tab Bar Splitter Control set to "PowderBlue"**

### 4.1.4.19 PrepareViewStyleInfo Event

The `PrepareViewStyleInfo` event is raised to allow custom formatting of a cell by changing its style object just before it is drawn. This allows formatting based on the current view state, e.g., current cell context, focused control, and so on.

For example, if you want to draw the current row with a bold text, you can use the `PrepareViewStyleInfo` event to accomplish this task. The idea is to change the style to bold font for any cell in the current row. Given below are the steps that you can follow in order to implement this functionality.

## API Reference

### Members

- **PrepareViewStyleInfo Event**

### Parameters

- Name | Type | Description | Default | Required
- ---- | ---- | ----------- | ------- | --------
- `args` | `GridDrawArgs` | The arguments related to drawing the cell. | `null` | Yes

### Returns

Type: None

### Exceptions

- None.

## Code Examples

### C#

```csharp
this.gridControl1.PrepareViewStyleInfo += (sender, args) =>
{
    if (args.RowIndex == gridControl1.CurrentRow)
    {
        args.Style.TextFont = new Font(args.Style.TextFont, FontStyle.Bold);
    }
};
```

### VB

```vb
AddHandler gridControl1.PrepareViewStyleInfo, Sub(sender, args)
                                                  If args.RowIndex = gridControl1.CurrentRow Then
                                                      args.Style.TextFont = New Font(args.Style.TextFont, FontStyle.Bold)
                                                  End If
                                              End Sub
```

## Page-level Navigation/TOC (if applicable)

- Custom Colors
- PrepareViewStyleInfo Event

## Cross References

See also:
- [Syncfusion.Windows.Forms.Grid](#)

## RAG Annotations

<!-- tags: [WinForms, Grid, Custom Colors, PrepareViewStyleInfo, Office2007Theme] keywords: [syncfusion, winforms, custom colors, prepareviewstyleinfo, tabbarsplittercontrol, powderblue] -->
```