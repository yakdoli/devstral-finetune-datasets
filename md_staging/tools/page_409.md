<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_409.jpeg
document_name: tools
page_number: 409
page_id: tools#page_409
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:10:42Z
fidelity: lossless
-->

## Overview
- Overview of syncfusion's essential tools for Windows Forms.
- Discussion on using Syncfusion's CalendarDateTime controls, specifically focusing on the `MonthCalendarAdv` control.

## Content

### WinForms-specific conventions
- **Essential Tools for Windows Forms**

```
}
```

```vb
[VB.NET]

Private Sub buttonAdv1_Click(ByVal sender As Object, ByVal e As System.EventArgs)

    'Performing the "=" button action
    Me.calculatorControl1.ButtonAction(Syncfusion.Windows.Forms.Tools.CalcActions.CalcOperatorEquals)
End Sub
```

### 3.5.3 CalendarDateTime Controls

Syncfusion CalendarDateTime controls are discussed below.

#### 3.5.3.1 MonthCalendarAdv

The Essential Tools **MonthCalendarAdv** control is an advanced calendar control that can display all the month of the year with the appropriate culture information for the months and days of the week. A wide variety of visual styles can be applied to the MonthCalendarAdv, to enhance the appearance of the control. This also includes the new Microsoft Office 2007 Style for all the child controls of the MonthCalendarAdv, such as the UpDown Spin Button, DropDown button of DateTimePickerAdv, ScrollButton, TodayButton and None button.

![Figure 209: MonthCalendarAdv Control](https://via.placeholder.com/600)

## API Reference (if applicable)

### WinForms-specific conventions
- **Namespace**: Syncfusion.Windows.Forms
- **Class**: MonthCalendarAdv
- **Properties/Methods**: Various properties and methods specific to MonthCalendarAdv, such as OnCultureChanged, OnMonthChanged, etc.

## Code Examples (multi-language supported)

```vb
' Example code to use MonthCalendarAdv
Private WithEvents monthCalendarAdv1 As New MonthCalendarAdv()
```

### Cross References
- Reference to the Microsoft Office 2007 style specifics can be found in the documentation related to control styling.
- Additional details about CultureInfo and its application can be found in the global settings documentation for Syncfusion controls.

<!-- tags: [tools, windows-forms, calendardatetimecontrols, monthcalendaradv, vb.net, millenium wheel, control element, updown spin button, dropdown dropdown, dropdown, datetimepickeradv, scrollbutton, todaybutton, none button, microsoft office 2007 style, visual styles] keywords: [syncfusion, essential tools, windows forms, calendardatetime controls, monthcalendaradv, localization, styling, visual appearance] -->
