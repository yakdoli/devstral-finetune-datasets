```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_666.jpeg
document_name: tools
page_number: 666
page_id: tools#page_666
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:27:30Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to integrate custom host primitives and progress bars with Syncfusion Windows Forms tools.
- Includes detailed configuration of UI controls such as buttons and advanced progress bar styles.
- Explains adding primitives to a Syncfusion tool component.

## Content

### Code Example

```csharp
'button1
Private button1 As Button = New Button()
Private button1.FlatStyle = System.Windows.Forms.FlatStyle.Popup
Private button1.Text = "Button"

'hostPrimitive1
Private hostPrimitive1 As HostPrimitive = New HostPrimitive()
Private hostPrimitive1.BackColor = System.Drawing.Color.Transparent
Private hostPrimitive1.HostControl = button1
Private hostPrimitive1.Size = New System.Drawing.Size(60, 20)

'progressBarAdv1
Private progressBarAdv1 As ProgressBarAdv = New ProgressBarAdv()
Private progressBarAdv1.BackColor = System.Drawing.Color.Transparent
Private progressBarAdv1.ProgressStyle = Syncfusion.Windows.Forms.Tools.ProgressBarStyles.Tube
Private progressBarAdv1.TubeStartColor = System.Drawing.Color.FromArgb((CInt((CByte(255)))), (CInt((CByte(192)))), (CInt((CByte(192)))))
  
'hostPrimitive2
Private hostPrimitive2 As HostPrimitive = New HostPrimitive()
Private hostPrimitive2.Alignment = Syncfusion.Windows.Forms.Tools.Alignment.Bottom
Private hostPrimitive2.BackColor = System.Drawing.Color.Transparent
Private hostPrimitive2.HostControl = progressBarAdv1
Private hostPrimitive2.Position = 200
Private hostPrimitive2.Size = New System.Drawing.Size(100, 20)

'Adding Primitives
gpe.Primitives.AddRange(New Syncfusion.Windows.Forms.Tools.Primitive() {hostPrimitive1, hostPrimitive2})
```

## API Reference (if applicable)

### Members
- **HostPrimitive**
  - **Properties**
    - `HostControl`: Specifies the control hosted by the primitive.
    - `BackColor`: Gets or sets the background color of the control.
    - `Size`: Gets or sets the size of the control.
    - `Alignment`: Gets or sets the alignment of the control.
    - `Position`: Gets or sets the position of the control.
- **ProgressBarAdv**
  - **Properties**
    - `ProgressStyle`: Specifies the style of the progress bar.
    - `BackColor`: Gets or sets the background color of the progress bar.
    - `TubeStartColor`: Gets or sets the start gradient color for the tube style.

## Code Examples (multi-language supported)

The above code demonstrates the creation and configuration of custom UI elements using Syncfusion's Windows Forms tools. It integrates standard Windows Forms buttons and Syncfusion's advanced progress bar controls, showcasing customization options for alignment and style.

## Cross References

- Refer to the Syncfusion documentation for more details on HostPrimitives and ProgressBarAdv controls.
- Additional information on UI customization and component integration can be found in the Syncfusion WinForms user guide.

<!-- tags: [winforms, syncfusion, hostprimitive, progressbaradv, tools] keywords: [custom ui elements, alignment, styles, controls, integration, progress bar, host, primitive, alignment, assembly, configuration] -->
```
