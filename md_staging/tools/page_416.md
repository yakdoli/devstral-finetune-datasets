```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_416.jpeg
document_name: tools
page_number: 416
page_id: tools#page_416
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:11:37Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Illustrates the configuration of the **2DBorderColor** property in a month calendar control.
- Demonstrates how to apply a background image to a control.

## Content

### Visual Settings Example

#### Figure 214: 2DBorderColor = "DodgerBlue"

![MonthCalendar with 2DBorderColor set to "DodgerBlue"](field3.png)

#### See Also
- [Background Settings, Visual Settings](#)

### 3.5.3.1.4.1.2 Background Settings

#### Background Image

The background image for the `MonthCalendarAdv` is specified in the `BackgroundImage` property.

**[C#]**

```csharp
this.monthCalendarAdv1.BackgroundImage =
    (System.Drawing.Image)(resources.GetObject("monthCalendarAdv1.BackgroundImage"));
this.monthCalendarAdv1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
```

**[VB.NET]**

```vb
Me.monthCalendarAdv1.BackgroundImage =
    DirectCast((resources.GetObject("monthCalendarAdv1.BackgroundImage")), System.Drawing.Image)
Me.monthCalendarAdv1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
```

## Page-level Navigation/TOC (if applicable)

- [Background Settings, Visual Settings](#)

## Cross References

- Provides links to related sections on background settings and visual properties.

<!-- tags: [syncfusion, winforms, monthcalendaradv, backgroundimage, 2dbordercolor] keywords: [monthcalendar, background, bordercolor, dodgerblue, visualsettings] -->
```