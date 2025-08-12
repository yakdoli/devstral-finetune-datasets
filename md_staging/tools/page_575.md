```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_575.jpeg
document_name: tools
page_number: 575
page_id: tools#page_575
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:22:02Z
fidelity: lossless
-->

### C# Example

```csharp
// Create a Data Set.
DataSet ds = new DataSet();
ds.Tables.Add(dt);
dt.Rows.Add(new string[] { "John", "Tina", "Doctor", "Italy" });
dt.Rows.Add(new string[] { "Mary", "anu", "Teacher", "America" });
dt.Rows.Add(new string[] { "asha", "roy", "Staff", "London" });
dt.Rows.Add(new string[] { "George", "Gaskin", "Nurse", "germany" });
dt.Rows.Add(new string[] { "sam", "jens", "Engineer", "Russia" });
dt.Rows.Add(new string[] { "Ben", "Geo", "Developer", "India" });

// Create a DataView.
DataView view = new DataView(dt);

// Set DataSource.
this.comboBoxAdv1.DataSource = view;

// Set DisplayMember.
this.comboBoxAdv1.DisplayMember = "place";
```

### VB.NET Example

```vb
' Create a DataTable.
Dim dt As DataTable = New DataTable("Table1")

' Adding Columns.
dt.Columns.Add("FirstName")
dt.Columns.Add("LastName")
dt.Columns.Add("occupation")
dt.Columns.Add("place")

' Create a Data Set.
Dim ds As DataSet = New DataSet
ds.Tables.Add(dt)
dt.Rows.Add(New String() { "John", "Tina", "Doctor", "Italy" })
dt.Rows.Add(New String() { "Mary", "anu", "Teacher", "America" })
dt.Rows.Add(New String() { "asha", "roy", "Staff", "London" })
dt.Rows.Add(New String() { "George", "Gaskin", "Nurse", "germany" })
dt.Rows.Add(New String() { "sam", "jens", "Engineer", "Russia" })
dt.Rows.Add(New String() { "Ben", "Geo", "Developer", "India" })

' Create a DataView.
Dim view As DataView = New DataView(dt)

' Set DataSource.
Me.comboBoxAdv1.DataSource = view

' Set DisplayMember.
Me.comboBoxAdv1.DisplayMember = "place"
```

<!-- tags: [WinForms, DataBinding, ComboBox, DataSource, DisplayMember] keywords: [DataSet, DataTable, DataView, ComboBoxAdv, DataBinding, DataSource, DisplayMember, C#, VB.NET] -->
```