```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_433.jpeg
document_name: tools
page_number: 433
page_id: tools#page_433
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:12:03Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Control Appearance and Behavior

Today and None buttons are displayed at the bottom of the calendar and they can be customized to set background image and font styles. This section will discuss the properties which control the appearance and behavior of the MonthCalendarAdv.

| MonthCalendarAdv Properties | Description |
|-----------------------------|-------------|
| TodayButton                 | Clicking this button at run time will move the focus to today's date in the calendar. |
| NoneButton                  | Clicking this button at run time will remove the focus of the date in the calendar. |
| BottomHeight                | The height of the bottom which contains the Today and None buttons are changed using this property. Default value is 20. |

### Customizing Today and None Buttons

The "Today" and "None" buttons are like Essential Tools ButtonAdv controls and they support all the properties of ButtonAdv control. You can access those properties using MonthCalendarAdv.NoneButton.Visible which controls the visibility (for example).

#### Accessing Properties of TodayButton

![](figure_233_accessing_properties_of_todaybutton_in_monthcalendaradv_propertygrid.png)

Figure 233: Accessing Properties of TodayButton in MonthCalendarAdv PropertyGrid

<!-- tags: [product, module, control, api, version?] keywords: [MonthCalendarAdv, TodayButton, NoneButton, BottomHeight, ButtonAdv, properties, visibility, customization] -->
```