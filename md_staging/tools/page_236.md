```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_236.jpeg
document_name: tools
page_number: 236
page_id: tools#page_236
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:52:00Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Event Data

The event handler receives an argument of type `ProvideGraphicsItemsEventArgs` containing data related to this event. The following `ProvideGraphicsItemsEventArgs` properties provide information specific to this event.

| Member                 | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| CaptionBackground      | Gets or sets the brush to be used for drawing the caption background.      |
| CaptionBounds          | Gets the bounds of the caption.                                            |
| CaptionFont            | Gets or sets the font to be used for the caption text.                     |
| CaptionForeground      | Gets or sets the color to be used for drawing the caption text and buttons.|
| Control                | Gets the dockable control for which the caption is being drawn.            |
| IsActiveCaption        | Gets the active / inactive state of the docking window.                    |

---

**Note:** If the control is in floating state, `DockingManager.ProvideGraphicsItems` event will not get triggered.

## Code Example

### [C#]

```csharp
private void dockingManager1_ProvideGraphicsItems(object sender,
    Syncfusion.Windows.Forms.Tools.ProvideGraphicsItemsEventArgs arg
)
{
    Console.WriteLine("ProvideGraphicsItems Event Raised" + i++);
    // Caption Background uses the Brush for Drawing on the caption bar
    arg.CaptionBackground = new LinearGradientBrush(arg.CaptionBounds,
        Color.Transparent, Color.White, (float)0);
    // Caption Foreground color property will be used to specify the Font color of the caption
    arg.CaptionForeground = Color.Black;
    // Caption Bounds property gives the values of Caption Height, width, Top, Bottom and
    // More like rectangle control.
    Console.WriteLine("Caption Bounds, Height=" +
        arg.CaptionBounds.Height +
```

## Page-level Navigation/TOC (if applicable)
- Event Data
- Code Example

<!-- tags: [winforms, event handling, ProvideGraphicsItemsEventArgs, DockingManager, Tools] keywords: [event arguments, caption background, caption bounds, caption font, caption foreground, dockable control, active/inactive state, floating state] -->
```