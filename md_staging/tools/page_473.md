```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_473.jpeg
document_name: tools
page_number: 473
page_id: tools#page_473
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:14:43Z
fidelity: lossless
-->


# Essential Tools for Windows Forms

## Overview
- Configures the calendar font, foreground colors, and trailing text for a date picker in Windows Forms.
- Demonstrates how to adjust the size and fit of the popup calendar dynamically.

## Content

### Date Picker Customization

```csharp
Me.dateTimePickerAdv1.CalendarFont = New System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Italic)
Me.dateTimePickerAdv1.CalendarForeColor = 
System.Drawing.Color.SaddleBrown
Me.dateTimePickerAdv1.CalendarTitleForeColor = 
System.Drawing.Color.SaddleBrown
Me.dateTimePickerAdv1.CalendarTrailingForeColor = 
System.Drawing.Color.Blue
```

**Figure 272**: *TitleForeColor = "SaddleBrown"; CalendarForeColor = "SaddleBrown";<br>CalendarFont = "Italic"; TrailingForeColor = "Blue"*

#### Calendar Size

The default size of the popup calendar can be changed using the below properties.

| DateTimePickerAdv Properties  | Description                       |
|-------------------------------|------------------------------------|
| CalendarSize                  | Indicates size of the popup calendar. |
| CalendarSizeToFit             | Indicates whether the calendar will size to fit according to the size of the days. |

```csharp
this.dateTimePickerAdv1.CalendarSize = new System.Drawing.Size(250, 200);
this.dateTimePickerAdv1.CalendarSizeToFit = false;
```

```vb
Me.dateTimePickerAdv1.CalendarSize = New System.Drawing.Size(250, 200)
```

## Page-level Navigation/TOC (if applicable)
- Not applicable in this section.

## Cross References
- None provided in this section.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Font properties, Date Picker, Calendar customization, Size, Visual Basic examples] keywords: [DateTimePicker, SaddleBrown, Italic, popup calendar, size adjustment, fit, code examples] -->
```