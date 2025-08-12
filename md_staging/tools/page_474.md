```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_474.jpeg
document_name: tools
page_number: 474
page_id: tools#page_474
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:15:41Z
fidelity: lossless
-->

## DateTimePickerAdv Properties and Calendar Size Adjustment

### Overview
- Demonstrates how to adjust the size of the PopUp Calendar and configure its Value and range limits.
- Focuses on setting properties such as `CalendarSizeToFit`, `Value`, `MaxValue`, and `MinValue`.

## Adjusting Calendar Size

```csharp
Me.dateTimePickerAdv1.CalendarSizeToFit = False
```

### Description
- Setting `Me.dateTimePickerAdv1.CalendarSizeToFit = False` changes the display size of the PopUp Calendar as shown in **Figure 273**.

![Figure 273: Size set for the PopUp Calendar](image_url_for_figure_273)

### See Also
- [Calendar Value](#calendar-value)

### Calendar Value Configuration

#### 3.5.3.2.3.2.2 Calendar Value

In the PopUp calendar, today's date will be selected by default at run time. This default date can be changed using the `Value` property. Additionally, you can specify the range of values/dates that can be selected at run time.

---

### DateTimePickerAdv Properties

| **DateTimePickerAdv Properties** | **Description** |
| --- | --- |
| MaxValue | Specifies the maximum value that can be picked from the DateTimePickerAdv. |
| MinValue | Specifies the minimum value that can be picked from the DateTimePickerAdv. |

---

### Code Example

```csharp
[C#]

this.dateTimePickerAdv1.Value = new System.DateTime(2008, 2, 23, 16, 46, 0);
this.dateTimePickerAdv1.MaxValue = new System.DateTime(2008, 12, 31, 23, 59, 0, 0);
this.dateTimePickerAdv1.MinValue = new System.DateTime(2007, 1, 1, 0, 0, 0);
```

---

### API Reference

- **Properties**
  - `Value`: Sets the default date to be selected in the PopUp Calendar.
  - `MaxValue`: Specifies the maximum date that can be selected.
  - `MinValue`: Specifies the minimum date that can be selected.

### Code Examples

The example demonstrates how to set the `Value`, `MaxValue`, and `MinValue` properties programmatically in C#.

---

### RAG Annotations
- **Tags**: [DateTimePickerAdv, CalendarSizeToFit, Value, MaxValue, MinValue]
- **Keywords**: [WinForms, DateTime, Calendar, PopUp, Date Selection, Range, Configuration]

```html
