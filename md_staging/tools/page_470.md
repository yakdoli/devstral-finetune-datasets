```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_470.jpeg
document_name: tools
page_number: 470
page_id: tools#page_470
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:15:28Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes the functionality and customization options of the `DateTimePickerAdv` control in Syncfusion Winforms.
- Focuses on the embedded calendar control and its properties.

## Content

### Custom NullString for Text Field
**Figure 269: Custom NullString for Text Field**

#### 3.5.3.2.3.2 Calendar

The `DateTimePickerAdv` control contains an embedded calendar control which pops up on clicking the dropdown button at the end of the control. The popup calendar is a `MonthCalendarAdv` control and hence supports all the properties of the `MonthCalendarAdv` control. These properties of the calendar can be accessed using the `DateTimePickerAdv.Calendar.TodayButton` (for example) property.

![Figure 270: Calendar Popup in a DateTimePickerAdv](https://via.placeholder.com/300x200?text=Figure%20270)

#### Customizing the Calendar
Additionally, the calendar popup can be customized using the `DateTimePickerAdv` properties. Refer to the Customizing the Calendar topic.

### Day Names

In the calendar, we can specify whether shortest day names can be used or not using the `UseShortestDayNames` property. By default, it is set to `true`.

```csharp
this.dateTimePickerAdv1.UseShortestDayNames = false;
```

```vb.net
Me.dateTimePickerAdv1.UseShortestDayNames = False
```

### Buttons in Calendar

## API Reference (if applicable)

Not applicable for this section.

## Code Examples

Not applicable for this section.

## Page-level Navigation/TOC (if applicable)

Not applicable for this section.

## Cross References

Not applicable for this section.

## RAG Annotations
<!-- tags: [tools, datetimpickeradv, monthcalendaradv, winforms, customization, calendar] keywords: [calendar control, popup calendar, shortest day names, useShortestDayNames, tabs, user guide, winforms] -->
```