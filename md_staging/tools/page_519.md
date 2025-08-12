```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_519.jpeg
document_name: tools
page_number: 519
page_id: tools#page_519
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:18:25Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Displaying ColorUIControl as a PopupMenu

#### Code Examples

**[C#]**
```csharp
private void panel1_MouseUp(object sender, MouseEventArgs e)
{
    this.popupMenu1.Show(this.panel1, new Point(e.X, e.Y));
}
```

**[VB.NET]**
```vb
Private Sub panel1_MouseUp(ByVal sender As Object, ByVal e As System.Windows.Forms.MouseEventArgs)
    Me.popupMenu1.Show(Me.panel1, New Point(e.X, e.Y))
End Sub
```

#### Figure: ColorUIControl as PopupMenu

![Figure 305: ColorUIControl as PopupMenu](attachment://305_coloruicontrol_popupmenu.jpg)

**Figure 305:** ColorUIControl as PopupMenu

**Note:** You can close the popup whenever a color is selected at run time. This is done using `ColorUIControl.ColorSelectedEvent`.

#### How to customize the color cells of the UserColors group

**Section:** 3.5.4.3.2 How to customize the color cells of the UserColors group

Color cells of the UserGroup panel in a ColorUIControl can be customized using the below code. We can use `UserColors` and `UserCustomColor` for this purpose.

**[C#]**
```csharp
// For example assume you have a ColorUIControl colorUIControl1.
for (int i = 0; i < this.colorUIControl1.UserColors.Count; i++)
    // Customization code here
```

## API Reference

### Events

- `ColorUIControl.ColorSelectedEvent`

### Properties

- `UserColors`
- `UserCustomColor`

### Methods

- `Show(Point location)`

## Page-level Navigation/TOC

- Displaying ColorUIControl as a PopupMenu
  - Code Examples
  - Figure: ColorUIControl as PopupMenu
  - Note: Closing the popup
- How to customize the color cells of the UserColors group

## Cross References

- See also: ColorUIControl, UserColors, ColorSelectedEvent

<!-- tags: [syncfusion, winforms, coloruicontrol, usercolors, colorselectedevent, popupmenu] keywords: [coloruicontrol, usercolors, customization, popup, color selection] -->
```