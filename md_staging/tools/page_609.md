```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_609.jpeg
document_name: tools
page_number: 609
page_id: tools#page_609
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:22:58Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```vb
Private Sub Form_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    ' Fill the dataset.
    Me.oleDbDataAdapter1.Fill(Me.dataSet1)
    Me.oleDbDataAdapter2.Fill(Me.dataSet2)

    ' Set the DataSource, DisplayMember, ValueMember properties.
    Me.multiColumnComboBox1.DataSource = Me.dataSet2.Customers
    Me.multiColumnComboBox1.DisplayMember = "ContactName"
    Me.multiColumnComboBox1.ValueMember = "CompanyName"
End Sub
```

A sample which demonstrates the OleDbDataAdapter databinding is available in the below sample installation location.

### Location
..\\My Documents\\Syncfusion\\EssentialStudio\\**Version Number**\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\MultiColumnComboBox

## 3.5.5.4.3.2.3 Populating MultiColumnComboBox

This section deals with populating MultiColumnComboBox with typed Dataset as datasource. Follow the steps below:

1. Open VS .NET IDE and click File → New → Project → Windows Application.
2. Right click the project in the Solutions Explorer and click Add → New Item and Add New Item dialog box will be displayed.
3. Select DataSet from templates pane, give the name (Say newdataset.xsd) and click Open. This will add file by name newdataset.xsd to the solution.
4. Add the XML Schema as shown below.
```xml
<!-- omitted XML content -->
```

## API Reference (if applicable)

### Namespaces and Classes
- **System.Windows.Forms.MultiColumnComboBox**
  - **Properties**
    - `DataSource`: Specifies the data source for the control.
    - `DisplayMember`: Specifies the property or column to display in the control.
    - `ValueMember`: Specifies the property or column to represent the actual value.

## Code Examples

### VB.NET Example
```vb
Me.multiColumnComboBox1.DataSource = Me.dataSet2.Customers
Me.multiColumnComboBox1.DisplayMember = "ContactName"
Me.multiColumnComboBox1.ValueMember = "CompanyName"
```

## Cross References
See also:  
- MultiColumnComboBox  
- DataSource  
- DisplayMember  
- ValueMember  

<!-- tags: [syncfusion, winforms, multicombo, databinding, typed_dataset, version:11.4.0.26] keywords: [multiColumnComboBox, oleDbDataAdapter, dataset, dataBinding, typedDataset] -->
```