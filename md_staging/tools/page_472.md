```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_472.jpeg
document_name: tools
page_number: 472
page_id: tools#page_472
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:14:51Z
fidelity: lossless
-->

### Essential Tools for Windows Forms

#### Overview
- Describes customization options for calendars in Windows Forms.
- Focuses on background and foreground settings using color and font properties.

## Content

```csharp
System.Drawing.Color.Wheat
```

### Figure 271: CalendarMonthBackground = "OldLace"; CalendarTitleBackColor = "Wheat"

![Figure 271: CalendarMonthBackground = "OldLace"; CalendarTitleBackColor = "Wheat"](image.png)

### Foreground Settings

The foreground appearance can be customized using the below properties.

| DateTimePickerAdv Properties               | Description                                                                               |
|--------------------------------------------|-------------------------------------------------------------------------------------------|
| CalendarFont                              | Sets font style for the text in the popup calendar.                                       |
| CalendarForeColor                          | Sets the fore color of the popup calendar.                                                |
| CalendarTitleForeColor                     | Specifies the fore color of the calendar header.                                          |
| CalendarTrailingForeColor                  | Specifies the fore color of the inactive month date.                                     |

### [C#]

```csharp
this.dateTimePickerAdv1.CalendarFont = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Italic);
this.dateTimePickerAdv1.CalendarForeColor = System.Drawing.Color.SaddleBrown;
this.dateTimePickerAdv1.CalendarTitleForeColor = System.Drawing.Color.SaddleBrown;
this.dateTimePickerAdv1.CalendarTrailingForeColor = System.Drawing.Color.Blue;
```

### [VB.NET]

## RAG Annotations

<!-- tags: [WinForms, Calendar, DateTimePickerAdv, Color, Font, Properties] keywords: [Customization, Foreground, Background, Font Style, Color Properties] -->
```