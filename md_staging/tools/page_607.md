```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_607.jpeg
document_name: tools
page_number: 607
page_id: tools#page_607
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:24:09Z
fidelity: lossless
-->

## Essential Tools For Windows Forms

### C\#

```csharp
// Create a Data Set
DataSet ds = new DataSet();
ds.Tables.Add(dt);

dt.Rows.Add(new string[] { "John", "Tina", "Doctor", "Italy" });
dt.Rows.Add(new string[] { "Mary", "anu", "Teacher", "America" });
dt.Rows.Add(new string[] { "asha", "roy", "Staff", "London" });
dt.Rows.Add(new string[] { "George", "Gaskin", "Nurse", "germany" });
dt.Rows.Add(new string[] { "sam", "jens", "Engineer", "Russia" });
dt.Rows.Add(new string[] { "Ben", "Geo", "Developer", "India" });

DataView view = new DataView(dt);
// DATASOURCE is DATAVIEW

this.MultiColumnComboBox1.DataSource = view;
this.MultiColumnComboBox1.DisplayMember = "FirstName";
this.MultiColumnComboBox1.ValueMember = "LastName";
}
```

### VB.NET

```vb
Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)

    ' Create dataTable
    Dim dt As DataTable = New DataTable("Table1")
    dt.Columns.Add("FirstName")
    dt.Columns.Add("LastName")
    dt.Columns.Add("occupation")
    dt.Columns.Add("place")

    ' Create a Data Set
    Dim ds As DataSet = New DataSet()
    ds.Tables.Add(dt)

    dt.Rows.Add(New String() { "John", "Tina", "Doctor", "Italy" })
    dt.Rows.Add(New String() { "Mary", "anu", "Teacher", "America" })
    dt.Rows.Add(New String() { "asha", "roy", "Staff", "London" })
    dt.Rows.Add(New String() { "George", "Gaskin", "Nurse", "germany" })
    dt.Rows.Add(New String() { "sam", "jens", "Engineer", "Russia" })
    dt.Rows.Add(New String() { "Ben", "Geo", "Developer", "India" })

    Dim view As DataView = New DataView(dt)
    ' DATASOURCE is DATAVIEW
End Sub
```
```html

<!-- tags: [product, module, control, api, version?] keywords: [windows forms, essential tools, dataset, dataview, multicolumndropdown, data source, displaymember, valuemember, vb.net, data set] -->
```