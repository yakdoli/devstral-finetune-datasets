```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_363.jpeg
document_name: tools
page_number: 363
page_id: tools#page_363
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:09:02Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Figure 173: ButtonStyles for ButtonEdit Control

**Note:** ButtonEdit control also supports all the three windows color themes, i.e., Blue, Silver, and Olivier themes. We need to change the Windows theme color in desktop properties for this.

### Custom Colors

We can also apply custom colors to the ButtonEditControl by setting **Office2007ColorScheme** of individual child buttons to **"Managed"**, and specifying the custom color through the **ApplyManagedColors** method as follows.

#### C#

```csharp
this.buttonEditChildButton1.Office2007ColorScheme = Syncfusion.Windows.Forms.Office2007Theme.Managed;
this.buttonEditChildButton2.Office2007ColorScheme = Syncfusion.Windows.Forms.Office2007Theme.Managed;
this.buttonEditChildButton3.Office2007ColorScheme = Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyResources(this, Color.LightGreen);
```

#### VB.NET

```vb
Me.buttonEditChildButton1.Office2007ColorScheme = Syncfusion.Windows.Forms.Office2007Theme.Managed
Me.buttonEditChildButton2.Office2007ColorScheme = Syncfusion.Windows.Forms.Office2007Theme.Managed
Me.buttonEditChildButton3.Office2007ColorScheme = Syncfusion.Windows.Forms.Office2007Theme.Managed
Office2007Colors.ApplyResources(Me, Color.LightGreen)
```

### Figure 174: Custom Color Of Child Buttons = "LightGreen"

![Figure 174](https://raw.githubusercontent.com/Syncfusion/Documentation/assets/docs/windows-forms/174-custom-color.png)

### Border Styles

The border styles for the ButtonEdit can be controlled using the below properties.

| Properties     | Description                               |
|----------------|-------------------------------------------|
| Border3DStyle | Sets the 3D border style for the control. The options are, |

<!-- tags: [Syncfusion Winforms, ButtonEditControl, Office2007ColorScheme, ApplyManagedColors, Border3DStyle] keywords: [custom colors, managed, theme color, 3D border, ButtonEdit, child buttons, LightGreen] -->
```