```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_086.jpeg
document_name: QTP
page_number: 086
page_id: QTP#page_086
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:07:06Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Use Case Scenarios

This feature enables you to get the maximum Y-axis value of a specified region in QTP testing.

### Methods Table

| Method        | Description                                                              | Parameters                                                                  | Return Type |
|---------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------|-------------|
| GetMaxYValue | Get the                                                                 | public double GetMaxYValue(int series, int point)                       | double      |
|               | Maximum Y axis value of specified region in Essential Chart.          |                                                                              |             |

### Applying GetMaxYValue Method in QTP

The following code example illustrates how to get the displayed text.

```csharp
[For Chart Control]

MsgBox(SwfWindow("ChartDemo").SwfObject("chart1").GetMaxYValue(10,2))
```

### 7.5 Essential Schedule

#### 7.5.1 How to reschedule the appointment to another timeline

##### Supported method to reschedule the appointment to another timeline in the schedule control

The ItemDrag method is used to reschedule the appointment to another timeline in the schedule control. The appointments are rescheduled to other dates based on the given start and end time.

##### Use Case Scenarios

This feature enables you to reschedule the appointment to another timeline in the schedule control in QTP testing.

#### Methods Table
| Method  | Description | Parameters | Return Type |
|---------|-------------|------------|-------------|
|         |             |            |             |
|         |             |            |             |

---

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```