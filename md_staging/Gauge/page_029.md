```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_029.jpeg
document_name: Gauge
page_number: 029
page_id: Gauge#page_029
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:15:09Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

![Metro](https://<image_url>/Metro)

## 3.4 Data Binding

You can bind any data source to the RadialGauge and map an index of a record to represent the actual value in RadialGauge. The DisplayMember and DisplayRecordIndex properties will map the DataColumn and DataRow of the binding source respectively to the Gauge control, which will then support high frequency data updates.

### Example

```csharp
this.radialGauge1.DataSource = dataTable;
this.radialGauge1.DisplayRecordIndex = [Row Index];
this.radialGauge1.DisplayMember = [column name];
```

### [ASPx]

```html
<input type="text" value="" id="SetDropDownText" />
<input type="button" value="Set Text" id="setText" />

<script type="text/javascript">
    $("#setText").bind('click', function () {
        var multiDD = $find("MultiColumnDropdown");
        multiDD.setText($('#SetDropDownText').val());
    });
</script>
```

## Page-level Navigation/TOC (if applicable)
- 3.4 Data Binding

## Cross References
See also: [Additional References]

## RAG Annotations
<!-- tags: [Metro, Windows Forms, RadialGauge, Data Binding, DisplayMember, DisplayRecordIndex, DataColumn, DataRow, Gauge control] keywords: [Metro, RadialGauge, Data Binding, DisplayMember, DisplayRecordIndex, DataColumn, DataRow, Gauge control] -->
```