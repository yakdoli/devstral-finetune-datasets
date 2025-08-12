```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_377.jpeg
document_name: tools
page_number: 377
page_id: tools#page_377
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:08:28Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes how to display a CalendarPopup in a ButtonEdit Control using its Click Event.
- Provides step-by-step instructions for creating and configuring a CalendarPopup control.

## Displaying a Calendar Popup in a ButtonEdit Control

### Overview
Using the ButtonEdit Child button click event, we can display a CalendarPopup at a specified location. It can be done using the following steps.

### Using CalendarPopup

1. **Create an instance of CalendarPopup control.**

   **[C#]**

   ```csharp
   private Syncfusion.Windows.Forms.Tools.CalendarPopup calendarPop1;
   calendarPop1 = new Syncfusion.Windows.Forms.Tools.CalendarPopup();
   ```

   **[VB.NET]**

   ```vb
   Private calendarPop1 As Syncfusion.Windows.Forms.Tools.CalendarPopup
   Private calendarPop1 = New Syncfusion.Windows.Forms.Tools.CalendarPopup()
   ```

2. **Declare an instance of MonthCalendarAdv control and add it to the CalendarPopup.**

   **[C#]**

   ```csharp
   private Syncfusion.Windows.Forms.Tools.MonthCalendarAdv MonthCal;
   MonthCal = new Syncfusion.Windows.Forms.Tools.MonthCalendarAdv();
   this.MonthCal.AutoSize = false;
   calendarPop1.AutoSize = false;
   calendarPop1.Size = new Size(200, 200);
   this.MonthCal.Size = new Size(200, 200);

   this.calendarPop1.Controls.Add(MonthCal);
   ```

   **[VB.NET]**

   ```vb
   Private MonthCal As Syncfusion.Windows.Forms.Tools.MonthCalendarAdv
   Private MonthCal = New Syncfusion.Windows.Forms.Tools.MonthCalendarAdv()
   Me.MonthCal.AutoSize = False
   calendarPop1.AutoSize = False
   calendarPop1.Size = New Size(200, 200)
   Me.MonthCal.Size = New Size(200, 200)
   ```

<!-- tags: [Syncfusion Winforms, ButtonEdit, CalendarPopup, MonthCalendarAdv, Click Event] keywords: [ButtonEdit, CalendarPopup, MonthCalendarAdv, Click Event, Syncfusion, Windows Forms] -->
```