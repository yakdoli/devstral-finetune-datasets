```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_544.jpeg
document_name: tools
page_number: 544
page_id: tools#page_544
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:19:40Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Color

| Member   | Description                            |
|----------|------------------------------------------|
| Color    | Specifies System.Drawing.Color structure. |

#### Item Selection

When the mouse is hovered over a particular color item, the ItemSelection event will be raised. The event handler receives an argument of type ColorPickedEventArgs. The event property provided by ColorPickedEventArgs argument is as follows:

| Member   | Description                            |
|----------|------------------------------------------|
| Color    | Specifies System.Drawing.Color structure. |

#### C#

```csharp
private void colorPickerUIAdv1_Picked(object sender, ColorPickerUIAdv.ColorPickedEventArgs e)
{
    BackColor = colorPickerUIAdv1.SelectedItem.Color;
}
```

#### VB.NET

```vb.net
Private Sub colorPickerUIAdv1_Picked(ByVal sender As Object, ByVal args As ColorPickerUIAdv.ColorPickedEventArgs)
    BackColor = colorPickerUIAdv1.SelectedItem.Color
End Sub
```

### Item Selection

When mouse is hovered over a particular color item, ItemSelection event will be raised. The event handler receives an argument of type ColorPickedEventArgs. The event property provided by ColorPickedEventArgs argument is as follows.

| Member   | Description                            |
|----------|------------------------------------------|
| Color    | Specifies System.Drawing.Color structure. |

#### C#

```csharp
private void colorPickerUIAdv1_ItemSelection(object sender, ColorPickerUIAdv.ColorPickedEventArgs e)
{
    // Gets the name of the color item that is selected.
    Console.WriteLine("Color Name is " + e.Color.Name.ToString());
}
```

#### VB.NET

```vb.net
Private Sub colorPickerUIAdv1_ItemSelection(ByVal sender As Object, ByVal args As ColorPickerUIAdv.ColorPickedEventArgs)
    ' Gets the name of the color item that is selected.
    Console.WriteLine("Color Name is " + e.Color.Name.ToString())
End Sub
```

### 3.5.4.5.5 Frequently Asked Questions

This section illustrates the solutions for various task-based queries about the control.

---

<!-- tags: [Syncfusion Winforms, Color Picker, Event Handling, Item Selection, C#, VB.NET, System.Drawing.Color] keywords: [color selection, event handler, mouse hover, color picker, color structure, item selection, frequently asked questions] -->
```
```