```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_889.jpeg
document_name: tools
page_number: 889
page_id: tools#page_889
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:40:30Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section provides an overview of the events associated with `NumericUpDownExt` in Windows Forms. These events notify the user when specific properties of the control are changed.
- Events listed include `Border3DStyleChanged`, `BorderColorChanged`, `BorderSidesChanged`, `BorderStyleChanged`, `ReadOnlyChanged`, `ThemeChanged`, and `ValueChanged`, each occurring when their respective properties are modified.

## Content

### NumericUpDownExt Events

The following table lists the events associated with the `NumericUpDownExt` control and their descriptions:

| NumericUpDownExt Events            | Description                                                                                       |
|------------------------------------|---------------------------------------------------------------------------------------------------|
| Border3DStyleChanged               | This event occurs when the `Border3DStyle` property is changed.                                  |
| BorderColorChanged                 | This event occurs when the `BorderColor` property is changed.                                    |
| BorderSidesChanged                 | This event occurs when the `BorderSides` property is changed.                                    |
| BorderStyleChanged                 | This event occurs when the `ClipText` property is changed.                                       |
| ReadOnlyChanged                    | This event occurs when the `ReadOnly` property is changed.                                       |
| ThemeChanged                       | This event occurs when the `ThemesEnabled` property is changed.                                  |
| ValueChanged                       | This event occurs when the `Value` property is changed.                                          |

#### 3.5.8.9.4.1 Border3DStyleChanged

This event occurs when the `Border3DStyle` property is changed. The `Border3DStyle` property indicates the style of the 3D border.

The event handler receives an argument of type `EventArgs` containing data related to this event.

##### C#

```csharp
private void numericUpDownExt1_Border3DStyleChanged(object sender, EventArgs e)
{
    Console.WriteLine("Border3DStyleChanged event is raised ");
}
```

##### VB.NET

```vb
Private Sub numericUpDownExt1_Border3DStyleChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("Border3DStyleChanged event is raised ")
End Sub
```

## API Reference
- **Events:**
  - `Border3DStyleChanged`: Triggered when the `Border3DStyle` property changes.
  - `BorderColorChanged`: Triggered when the `BorderColor` property changes.
  - `BorderSidesChanged`: Triggered when the `BorderSides` property changes.
  - `BorderStyleChanged`: Triggered when the `ClipText` property changes.
  - `ReadOnlyChanged`: Triggered when the `ReadOnly` property changes.
  - `ThemeChanged`: Triggered when the `ThemesEnabled` property changes.
  - `ValueChanged`: Triggered when the `Value` property changes.

## Code Examples
### C#
```csharp
private void numericUpDownExt1_Border3DStyleChanged(object sender, EventArgs e)
{
    Console.WriteLine("Border3DStyleChanged event is raised ");
}
```

### VB.NET
```vb
Private Sub numericUpDownExt1_Border3DStyleChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("Border3DStyleChanged event is raised ")
End Sub
```

## Page-level Navigation/TOC
- Events associated with `NumericUpDownExt`
- Detailed explanation of `Border3DStyleChanged` event
- Code examples in C# and VB.NET

## Cross References
- Refer to documentation on other properties such as `BorderColor`, `BorderSides`, `ClipText`, `ReadOnly`, `ThemesEnabled`, and `Value`.
- Consult the general documentation on `NumericUpDownExt` control for additional details and usage examples.

<!-- tags: [windows forms, numericupdownext, events, properties, themes, border styles, control] keywords: [numericupdownext, border3dstylechanged, bordercolorchanged, bordersideschanged, borderstylechanged, readonlychanged, themechanged, valuechanged] -->
```