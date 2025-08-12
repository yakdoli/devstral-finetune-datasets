```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_543.jpeg
document_name: tools
page_number: 543
page_id: tools#page_543
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:20:03Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Color Selection at run time

Automatic color that has to be selected, when Automatic button is clicked at run time, is set through `AutomaticColor` property. Default color is black.

### Code Examples

#### C#

```csharp
this.colorPickerUIAdv1.AutomaticColor = System.Drawing.Color.OrangeRed;
```

#### VB.NET

```vb
Me.colorPickerUIAdv1.AutomaticColor = System.Drawing.Color.OrangeRed
```

![](image-of-color-picker.png)

Figure 332: `AutomaticColor = "OrangeRed"`

### Note

Height of this Automatic button can be specified in `ColorPickerUIAdv.ButtonHeight` property. Default value is 23.

## Events

### Picked Event

This event is raised every time a color is picked in the `ColorPickerUIAdv` control. The event handler receives an argument of type `ColorPickedEventArgs`. The event property provided by `ColorPickedEventArgs` argument is as follows.

| Member     | Description                    |
|------------|----------------------------------|
| Member     | Description for the member     |

## API Reference

- The event handler for the `Picked` event should handle `ColorPickedEventArgs`.

## Code Examples

- **Example Usage:**

```csharp
colorPickerUIAdv1.Picked += (sender, args) =>
{
    Console.WriteLine($"Selected Color: {args.Color}");
};
```

## Additional Information

- **Default Color:** Default automatic color is black.
- **Customizable Height:** The height of the Automatic button can be customized using the `ButtonHeight` property.

## See also

- [Color Picker UI](#)
- [Syncfusion Controls](#)
- [Event Handling in WinForms](#)

<!-- tags: [Syncfusion, WinForms, Color Picker, Events] keywords: [AutomaticColor, ButtonHeight, PickedEvent, ColorPickedEventArgs, ColorPickerUIAdv] -->
```