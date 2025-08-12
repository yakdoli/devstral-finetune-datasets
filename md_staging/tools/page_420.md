```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_420.jpeg
document_name: tools
page_number: 420
page_id: tools#page_420
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:11:48Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Applying Office Color Schemes to MonthCalendarAdv Control

The `Office2007Theme` property of the `MonthCalendarAdv` control allows you to set different color schemes for the calendar. Below are examples of how to apply various themes using C# and VB.NET.

#### Setting the Silver Theme (C#)
```csharp
this.monthCalendarAdv1.Office2007Theme = 
Syncfusion.Windows.Forms.Office2007Theme.Silver;
```

#### Setting the Silver Theme (VB.NET)
```vb
'Sets the Color scheme as Silver when the style is Office2007
Me.monthCalendarAdv1.Office2007Theme = 
Syncfusion.Windows.Forms.Office2007Theme.Silver
```

#### Office Color Schemes for MonthCalendarAdv Control
![Figure: Office Color Schemes for MonthCalendarAdv Control](image.png)
*Figure 218: Office Color Schemes for MonthCalendarAdv Control*

#### Custom Colors

We can also apply custom colors to the `MonthCalendarAdv` control by setting `Office2007Theme` to "Managed" and specifying the custom color through the `ApplyManagedColors` method as follows.

##### Applying a Custom Color (C#)
```csharp
this.monthCalendarAdv1.Office2007Theme = 
Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(this, Color.Orange);
```

##### Applying a Custom Color (VB.NET)
```vb
Me.monthCalendarAdv1.Office2007Theme = 
Syncfusion.Windows.Forms.Office2007Theme.Managed
Office2007Colors.ApplyManagedColors(Me, Color.Orange)
```

## API Reference

### `Office2007Theme` Property
- **Type**: `Syncfusion.Windows.Forms.Office2007Theme`
- **Description**: Specifies the Office 2007 theme for the control.
- **Possible Values**:
  - `Syncfusion.Windows.Forms.Office2007Theme.Silver`
  - `Syncfusion.Windows.Forms.Office2007Theme.Managed`
  - (Other themes as applicable)

### `ApplyManagedColors` Method
- **Signature**: `public static void ApplyManagedColors(Control control, Color customColor)`
- **Parameters**:
  - `control`: The control to which the custom colors will be applied.
  - `customColor`: The custom color to apply.
- **Description**: Applies a custom color to the control when the theme is set to "Managed".

## Code Examples

### Customizing the Color Scheme

#### C#
```csharp
// Set the Office2007Theme to Managed
this.monthCalendarAdv1.Office2007Theme = 
    Syncfusion.Windows.Forms.Office2007Theme.Managed;

// Apply a custom color (Orange)
Office2007Colors.ApplyManagedColors(this, Color.Orange);
```

#### VB.NET
```vb
' Set the Office2007Theme to Managed
Me.monthCalendarAdv1.Office2007Theme = 
    Syncfusion.Windows.Forms.Office2007Theme.Managed

' Apply a custom color (Orange)
Office2007Colors.ApplyManagedColors(Me, Color.Orange)
```

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Office2007Theme, MonthCalendarAdv, custom colors, managed theme] keywords: [MonthCalendarAdv, custom colors, Office2007Theme, Silver, Managed, ApplyManagedColors, control customization] -->
```