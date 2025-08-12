```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_419.jpeg
document_name: tools
page_number: 419
page_id: tools#page_419
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:12:06Z
fidelity: lossless
--> 

## Overview

- Demonstrates how to set the Office 2003 style for the `MonthCalendarAdv` control using Syncfusion WinForms.
- Provides examples in both C# and VB.NET.
- Displays the visual styles applied for the `MonthCalendarAdv` control by comparing different Office themes: Office XP, Office 2003, VS 2005, and Office 2007.
- Explains how to use the `VisualStyle` property to apply different styles to the control.

## Content

### Setting Office 2003 Style for MonthCalendarAdv

#### Sample Code in C#

```csharp
// Sample code for setting Office2003 style for MonthCalendarAdv
this.monthCalendarAdv1.Style = Syncfusion.Windows.Forms.VisualStudio.Office2003;
```

#### Sample Code in VB.NET

```vb.net
' Sample code for setting Office2003 style for MonthCalendarAdv
Me.monthCalendarAdv1.Style = Syncfusion.Windows.Forms.VisualStudio.Office2003
```

#### Visual Styles Applied

The following figure shows the styles applied for the `MonthCalendarAdv` control with various Office themes:

![Figure 217: Styles Applied for MonthCalendarAdv Control](https://i.imgur.com/1L2Q0G2.png)

### Setting the Color Scheme as Silver for Office 2007

```csharp
// Sets the Color scheme as Silver when the style is Office2007
```

## API Reference

The `MonthCalendarAdv` control in Syncfusion WinForms provides the following key members:

- **Property**: `Style`
  - Type: `Syncfusion.Windows.Forms.VisualStudio`
  - Description: Specifies the visual style for the control.
  - Example:
    ```csharp
    this.monthCalendarAdv1.Style = Syncfusion.Windows.Forms.VisualStudio.Office2007;
    ```

## Code Examples

### Applying Different Styles

#### Office 2003 Style Example

```csharp
this.monthCalendarAdv1.Style = Syncfusion.Windows.Forms.VisualStudio.Office2003;
```

#### Office 2007 Style Example

```csharp
this.monthCalendarAdv1.Style = Syncfusion.Windows.Forms.VisualStudio.Office2007;
```

## Page-Level Navigation/TOC

- Setting Office 2003 Style for MonthCalendarAdv
- Visual Styles Applied
- Setting the Color Scheme as Silver for Office 2007
- API Reference
- Code Examples

## Cross References

- See also: [MonthCalendarAdv Control Overview](MONTHCALENDARADV-CONTROL-OVERVIEW)

<!-- tags: [syncfusion, winforms, monthcalendaradv, visualstyle, office2003, office2007, color scheme, control styles] keywords: [monthcalendaradv, style, office, theme, color scheme] -->
```