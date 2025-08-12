```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_426.jpeg
document_name: tools
page_number: 426
page_id: tools#page_426
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:13:07Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Foreground Settings

By default, week numbers will not be shown in the calendar. The `ShowWeekNumbers` property should be set to `true` to display the week numbers. The font and foreground color can be set using the below properties.

| MonthCalendarAdv Properties | Description |
|---|---|
| WeekFont | Gets or sets the font of the week numbers column. |
| WeekTextColor | Gets or sets the text color for week numbers column. |

#### C#

```csharp
this.monthCalendarAdv1.ShowWeekNumbers = true;
this.monthCalendarAdv1WeekFont = new System.Drawing.Font("Courier New", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
this.monthCalendarAdv1.WeekTextColor = System.Drawing.Color.Blue;
```

#### VB.NET

```vb
Me.monthCalendarAdv1.ShowWeekNumbers = True
Me.monthCalendarAdv1.WeekFont = New System.Drawing.Font("Courier New", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CByte((0)))
Me.monthCalendarAdv1.WeekTextColor = System.Drawing.Color.Blue
```

![Figure 225: WeekFont = "Courier new, 9, Bold"; WeekTextColor = "Blue"](https://i.imgur.com/placeholder.png)
*Figure 225: WeekFont = "Courier new, 9, Bold"; WeekTextColor = "Blue"*

### Gradient Background
```html

<!-- tags: [syncfusion, winforms, calendar, weeknumbers, background, gradient, colors, properties, MonthCalendarAdv, font] keywords: [syncfusion, windows forms, calendar control, week numbers, gradient background, foreground settings, properties, showweeknumbers, weekfont, weektextcolor, visual studio, C#, VB.NET] -->
```