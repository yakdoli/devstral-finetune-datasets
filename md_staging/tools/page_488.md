```html
<!-- source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_488.jpeg
document_name: tools
page_number: 488
page_id: tools#page_488
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:16:05Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to apply color schemes to the DateTimePickerAdv control using the Office2007Theme property.
- Highlights options for custom color customization within the DateTimePickerAdv control.

## Content

### Figure 283: Visual Styles for DateTimePickerAdv

```csharp
//[C#]

//Sets the Color scheme as Blue when the style is Office2007
this.dateTimePickerAdv1.Office2007Theme = 
Syncfusion.Windows.Forms.Office2007Theme.Blue;
```

```vb.net
'[VB.NET]

'Sets the Color scheme as Blue when the style is Office2007
Me.dateTimePickerAdv1.Office2007Theme = 
Syncfusion.Windows.Forms.Office2007Theme.Blue
```

### Figure 284: Office Color Scheme for DateTimePickerAdv Control

![Figure 284: Office Color Scheme for DateTimePickerAdv Control](https://user-images.githubusercontent.com/87749041/170763656-aae4e5bd-62a5-4972-a4a9-8f9eb8a8200c.png)

#### Figure Descriptions:
- **Blue:** DateTimePickerAdv with the Blue color scheme.
- **Silver:** DateTimePickerAdv with the Silver color scheme.
- **Black:** DateTimePickerAdv with the Black color scheme.

### Custom Colors

We can also apply custom colors to the DateTimePickerAdv control by setting Office2007Theme to "Managed" and specifying the custom color through the `ApplyManagedColors` method as follows.

```csharp
//[C#]

this.dateTimePickerAdv1.Office2007Theme = 
Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(this, Color.Orange);
```

```vb.net
'[VB.NET]

Me.dateTimePickerAdv1.Office2007Theme = 
Syncfusion.Windows.Forms.Office2007Theme.Managed;
```

### Section Summary
This section covers the application of both predefined Office2007 color schemes and user-defined custom colors to the DateTimePickerAdv control, enhancing its visual appearance within WinForms applications.

### Tags and Keywords
<!-- tags: [syncfusion, windows forms, datetimepickeradv, office2007theme, custom colors, managed themes] keywords: [DateTimePickerAdv, Office2007Theme, Syncfusion.Windows.Forms, ApplyManagedColors, Blue, Silver, Black, Custom Colors, Visual Styles] -->
```