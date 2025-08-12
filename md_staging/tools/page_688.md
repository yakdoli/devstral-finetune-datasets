```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_688.jpeg
document_name: tools
page_number: 688
page_id: tools#page_688
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:28:27Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Customizing SplitContainerAdv Properties

The following properties are used to set the background for the SplitContainerAdv control:

| SplitContainerAdv Properties                | Description                                                                |
|---------------------------------------------|----------------------------------------------------------------------------|
| BackgroundImage                            | Sets the background image for the control.                                |
| BackgroundImageLayout                      | Specifies the background image layout.                                    |
| BackColor                                  | Sets the background color for the control.                                |
| BackgroundColor                            | Sets the solid, gradient or pattern style background for the control.     |

### Note:
The above properties can be overridden by SplitContainerAdv.Panel properties.

#### Code Examples

**[C#]**
```csharp
this.splitContainerAdv1.BackColor = System.Drawing.Color.LightSteelBlue;
this.splitContainerAdv1.Panel1.BackColor = new Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.BackwardDiagonal, System.Drawing.Color.AliceBlue, System.Drawing.Color.LightSteelBlue);
this.splitContainerAdv1.Panel2.BackColor = System.Drawing.Color.AliceBlue;
```

**[VB.NET]**
```vb.net
Me.splitContainerAdv1.BackColor = System.Drawing.Color.LightSteelBlue
Me.splitContainerAdv1.Panel1.BackColor = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.BackwardDiagonal, System.Drawing.Color.AliceBlue, System.Drawing.Color.LightSteelBlue)
Me.splitContainerAdv1.Panel2.BackColor = System.Drawing.Color.AliceBlue
```

## Foreground Settings

The following table describes the foreground settings for the SplitContainerAdv control.

| SplitContainerAdv Properties | Description                         |
|------------------------------|-------------------------------------|
| Font                        | Sets the font style for the display text in the control. |
| ForeColor                   | Sets the color for the display text in the control.     |

#### Code Example

**[C#]**
```csharp
this.splitContainerAdv1.ForeColor = System.Drawing.Color.Black;
this.splitContainerAdv1.Font = new System.Drawing.Font("Arial", 10);
```

### References:
- External references to the Syncfusion documentation for more detailed examples and configurations.

<!-- tags: [windowsforms, Syncfusion, SplitContainerAdv, properties, background, foreground, font, color] keywords: [splitcontaineradv, backgroundimage, backcolor, backgroundcolor, foreground, font, forecolor] -->
```
