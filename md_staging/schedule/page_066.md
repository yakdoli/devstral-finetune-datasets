<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_066.jpeg
document_name: schedule
page_number: 066
page_id: schedule#page_066
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:12:21Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## 4.5 Time Interval

This topic illustrates the time interval format options for scheduling appointments.

### 4.5.1 Setting the Time Interval in Seconds Format

The Schedule control, by default, allows you to set the time interval for scheduling appointments only in hours and minutes format. Now, you can also include seconds in the time interval by enabling the `AllowSecondsInAppointment` property.

```csharp
this.scheduleControl1.AllowSecondsInAppointment = true;
```

```vb
Me.scheduleControl1.AllowSecondsInAppointment = True
```

𫘤