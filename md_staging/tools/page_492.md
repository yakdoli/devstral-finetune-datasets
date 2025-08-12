```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en 
source_filename: page_492.jpeg
document_name: tools
page_number: 492
page_id: tools#page_492
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:16:21Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Discusses the configuration and customization of the DateTimePickerAdv control in Syncfusion WinForms.
- Covers settings such as `UseCurrentCulture` and `Culture` properties.
- Explains how to create a custom popup window for DateTimePickerAdv.

## Content

### Setting UseCurrentCulture and Culture Properties

| Property            | Description                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------------|
| UseCurrentCulture   | Specifies whether the current culture of the machine will be used. By default, it is false.    |

#### Example Code

```csharp
[C#]
this.dateTimePickerAdv1.UseCurrentCulture = false;
this.dateTimePickerAdv1.Culture = new System.Globalization.CultureInfo("hi-IN");
```

```vbnet
[VB.NET]
Me.dateTimePickerAdv1.UseCurrentCulture = False
Me.dateTimePickerAdv1.Culture = New System.Globalization.CultureInfo("hi-IN")
```

#### Visual Representation

![Figure 287 Culture="Hindi(India)"](image.png)

### Custom PopupWindow

#### Section: 3.5.3.2.3.7.3 Custom PopupWindow

This section deals with creating a custom popup window for the DateTimePickerAdv control. We can implement the IDatetimePickerAdvCalendar interface to drop down a custom window.

### IDatetimePickerAdvCalendar Interface Members

| IDatetimePickerAdvCalendar Member | Description                                       |
|------------------------------------|---------------------------------------------------|
| Active                             | Boolean value indicating if the DateTimePickerAdv should consider the |

## Footer

© 2013 Syncfusion. All rights reserved. 492 | Page

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Class**: IDatetimePickerAdvCalendar
- **Members**:
  - Active: Boolean value indicating if the DateTimePickerAdv should consider the

## Code Examples

- C# Example:
```csharp
this.dateTimePickerAdv1.UseCurrentCulture = false;
this.dateTimePickerAdv1.Culture = new System.Globalization.CultureInfo("hi-IN");
```
- VB.NET Example:
```vbnet
Me.dateTimePickerAdv1.UseCurrentCulture = False
Me.dateTimePickerAdv1.Culture = New System.Globalization.CultureInfo("hi-IN")
```

### Cross References

See also:
- DateTimePickerAdv control
- CultureInfo class
- Globalization in Windows Forms

### Tags and Keywords

<!-- tags: [Windows Forms, DateTimePickerAdv, Culture, Custom Popup, Globalization, Syncfusion, WinForms] keywords: [UseCurrentCulture, Culture, hijri, DateTimePicker, CustomPopup, IDatetimePickerAdvCalendar, Hindi, India] -->
```