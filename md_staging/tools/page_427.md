```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_427.jpeg
document_name: tools
page_number: 427
page_id: tools#page_427
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:12:39Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

By default, the week numbers column has a gradient background. To customize the background manually, use the `WeekInterior` property.

## Content

### Customizing the WeekInterior Property

[C#]

```csharp
this.monthCalendarAdv1.WeekInterior = new
Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Vertical,
System.Drawing.Color.AliceBlue, System.Drawing.Color.LightSteelBlue);
```

[VB.NET]

```vb
Me.monthCalendarAdv1.WeekInterior = New
Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Vertical,
System.Drawing.Color.AliceBlue, System.Drawing.Color.LightSteelBlue)
```

### Custom Gradient Background for Week Numbers

![Figure 226: Custom Gradient Background for Week Numbers](https://example.com/image)

#### Day Settings

MonthCalendarAdv has properties to customize the days displayed in the calendar. This section discusses those properties.

### Foreground Settings

The below properties deal with the foreground appearance of the dates.

| MonthCalendarAdv Properties | Description |
|-----------------------------|-------------|
| `DayNamesColor`            | Specifies the fore color of the day names. |
| `DayNamesFont`             | Specifies the font style of the day names. |
```