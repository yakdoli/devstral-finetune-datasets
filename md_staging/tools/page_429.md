```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_429.jpeg
document_name: tools
page_number: 429
page_id: tools#page_429
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:11:47Z
fidelity: lossless
--> 

## Essential Tools for Windows Forms

### Overview
- Explanation of key tools and features for Windows Forms development with Syncfusion.
- Highlighting the configuration and customization options for the MonthCalendarAdv component.

### Content

#### UseShortestDayNames
| **Property** | **Description** |
|--------------|------------------|
| UseShortestDayNames | Specifies whether shortest day names are used or not. by default it is true. |

##### Code Examples

###### C#
```csharp
this.monthCalendarAdv1.DayNamesHeight = 22;
this.monthCalendarAdv1.UseShortestDayNames = false;
```

###### VB.NET
```vb
Me.monthCalendarAdv1.DayNamesHeight = 22
Me.monthCalendarAdv1.UseShortestDayNames = False
```

#### Gradient Background for Day Header
By default, the day's header has a gradient background. We can change the default background style using the `DaysHeaderInterior` property.

##### Code Examples

###### C#
```csharp
this.monthCalendarAdv1.DaysHeaderInterior = new Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Vertical, System.Drawing.Color.AntiqueWhite, System.Drawing.Color.SandyBrown);
```

###### VB.NET
```vb
Me.monthCalendarAdv1.DaysHeaderInterior = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Vertical, System.Drawing.Color.AntiqueWhite, System.Drawing.Color.SandyBrown)
```

#### Today's Date
- Explanation and usage of setting today's date in the MonthCalendarAdv component.

### Figure 228: DayNamesHeight = "22" and without ShortDayNames
![](image_for_Figure_228)

### Figure 229: Custom Gradient Style for DaysHeader Background
![](image_for_Figure_229)

## 3.5.3.1.4.2.3.1 Today's Date
- [Table of content or detailed section description]

### API Reference (if applicable)
- Pertinent methods, properties, and event details related to the MonthCalendarAdv component.

### Code Examples (multi-language supported)
- Additional examples demonstrating the usage of the `UseShortestDayNames` and `DaysHeaderInterior` properties.

## Cross References
- Refer to related sections or documentation for further customization options.

### RAG Annotations
HTML comment with tags and keywords derived from visible content:
```html
<!-- tags: [syncfusion, winforms, monthcalendaradv, useshortestdaynames, daysheaderinterior, version:11.4.0.26] 
keywords: [monthcalendar, day names height, gradient background, .net, csharp, vb.net, today's date, customization] -->
``` 
``` 
