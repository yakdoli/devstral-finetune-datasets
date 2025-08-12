```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_428.jpeg
document_name: tools
page_number: 428
page_id: tools#page_428
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:12:21Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

| DaysFont | Specifies the font style of the days / dates. |
| --- | --- |
| DaysColor | Specifies the fore color of the day names. |

## Code Samples

### C#

```csharp
this.monthCalendarAdv1.DayNamesFont = new System.Drawing.Font("Courier New", 9F, System.Drawing.FontStyle.Bold);
this.monthCalendarAdv1.DayNamesColor = Color.Black;
this.monthCalendarAdv1.DaysColor = System.Drawing.SystemColors.HotTrack;
this.monthCalendarAdv1.DaysFont = new System.Drawing.Font("Courier New", 8.25F, System.Drawing.FontStyle.Regular);
```

### VB.NET

```vb
Me.monthCalendarAdv1.DayNamesFont = New System.Drawing.Font("Courier New", 9F, System.Drawing.FontStyle.Bold)
Me.monthCalendarAdv1.DayNamesColor = Color.Black
Me.monthCalendarAdv1.DaysColor = System.Drawing.SystemColors.HotTrack
Me.monthCalendarAdv1.DaysFont = New System.Drawing.Font("Courier New", 8.25F, System.Drawing.FontStyle.Regular)
```

## Customized Month Calendar Display

![MonthCalendarAdv with Customized Days and Day Names](<image-link>)  
**Figure 227: MonthCalendarAdv with Customized Days and Day Names**

## Height and Day Names Format

The height of the day header and the day name formats are specified using the below properties.

### MonthCalendarAdv Properties

| Property Name | Description |
| --- | --- |
| DayNamesHeight | Sets the height of the days header. Default value is 17. |

## API Reference

### Properties

- **DayNamesHeight**: Sets the height of the days header. Default value is 17.

## Code Examples

The code examples above demonstrate how to customize the font styles and colors of the days and day names for the `MonthCalendarAdv` control in both C# and VB.NET.

<!-- tags: [Syncfusion, WinForms, MonthCalendarAdv] keywords: [DaysFont, DaysColor, DayNamesHeight, MonthCalendarAdv, Customization, C#, VB.NET] -->
```