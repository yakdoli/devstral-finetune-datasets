```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_435.jpeg
document_name: tools
page_number: 435
page_id: tools#page_435
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:13:01Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Custom Images for Scroll Buttons

### Source Code Examples

```csharp
this.monthCalendarAdv1.LeftScrollButtonImage = 
    ((System.Drawing.Image)(resources.GetObject("monthCalendarAdv1.LeftScrollButtonImage")));
this.monthCalendarAdv1.RightScrollButtonImage = 
    ((System.Drawing.Image)(resources.GetObject("monthCalendarAdv1.RightScrollButtonImage")));
this.monthCalendarAdv1.ScrollButtonSize = new System.Drawing.Size(30, 25);
this.monthCalendarAdv1.StretchScrollImage = false;
```

```VB.NET
Me.monthCalendarAdv1.LeftScrollButtonImage = 
    DirectCast((resources.GetObject("monthCalendarAdv1.LeftScrollButtonImage")), System.Drawing.Image)
Me.monthCalendarAdv1.RightScrollButtonImage = 
    DirectCast((resources.GetObject("monthCalendarAdv1.RightScrollButtonImage")), System.Drawing.Image)
Me.monthCalendarAdv1.ScrollButtonSize = New System.Drawing.Size(30, 25)
Me.monthCalendarAdv1.StretchScrollImage = False
```

#### Figure 335: Custom Images for Scroll Buttons  
![Custom Images for Scroll Buttons](https://example.com/image_path)

### Runtime Features

#### 3.5.3.1.4.3.1 Selecting a Date

##### Range of Selection

The minimum and maximum date selectable by the calendar can be specified using `MinValue` and `MaxValue` properties. (This is similar to `MinDate` and `MaxDate` of the Windows MonthCalendar control).

| MonthCalendarAdv Properties | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| Value                       | Indicates the current value of the calendar. By default, this value will be the current date. |

---

© 2013 Syncfusion. All rights reserved.  
Page 435  
<!-- tags: [syncfusion, windows forms, month calendar, scroll buttons, min max value] keywords: [custom images, runtime features, range selection, minvalue, maxvalue] -->
```