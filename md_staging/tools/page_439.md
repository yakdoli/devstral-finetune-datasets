```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_439.jpeg
document_name: tools
page_number: 439
page_id: tools#page_439
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:13:14Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Selecting Dates Programmatically

Dates should be specified in the DateTime Array List. Then the DateTime Array list should be declared to the `SelectedDates` Property. This would select the dates that are in the DateTime Array list.

```vb
Dim dateTimes As DateTime() = New DateTime() {New DateTime(2010, 11, 2), New DateTime(2010, 11, 3)}
Me.monthCalendarAdv1.SelectedDates = dateTimes
```

#### Figure: Select Date Range Programmatically

![](image.png)

**Figure 238:** Select Date Range Programmatically

**Note:** Date range should be specified manually in the DateTime Array list.

#### 3.5.3.1.4.3.2 Month Settings: Navigation at RunTime

At run time, you have options to move to the next month or previous month using the left or right scroll buttons and also using the context menu displayed, when you click on the month of the calendar. To specify images for individual months in the menu, use the `MonthImageList` property.

## Footer
© 2013 Syncfusion. All rights reserved.

<!-- tags: [Syncfusion Winforms, DateTime Array, SelectedDates Property, MonthImageList, Navigation, Month Settings, runtime, dates selection] keywords: [DateTime Array, SelectedDates, MonthImageList, navigation, month settings, runtime, dates selection] -->
```
