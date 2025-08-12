```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_594.jpeg
document_name: tools
page_number: 594
page_id: tools#page_594
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:22:47Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

2. **Create an instance of the ComboBoxBase control and ListBox.**

### [C#]

```csharp
private Syncfusion.Windows.Forms.Tools.ComboBoxBase comboBoxBase1;
private System.Windows.Forms.ListBox listBox1;

this.comboBoxBase1 = new Syncfusion.Windows.Forms.Tools.ComboBoxBase();
this.listBox1 = new ListBox();
```

### [VB.NET]

```vb
Private comboBoxBase1 As Syncfusion.Windows.Forms.Tools.ComboBoxBase
Private listBox1 As System.Windows.Forms.ListBox

Me.comboBoxBase1 = New Syncfusion.Windows.Forms.Tools.ComboBoxBase()
Me.listBox1 = New ListBox()
```

3. **Set the ListControl that will be used in the dropdown portion of ComboBoxBase and specify the size of ComboBoxBase.**

### [C#]

```csharp
this.comboBoxBase1.ListControl = this.listBox1;
this.comboBoxBase1.Size = new Size(120, 20);
```

### [VB.NET]

```vb
Me.comboBoxBase1.ListControl = Me.listBox1
Me.comboBoxBase1.Size = New Size(120, 20)
```

4. **Specify the datasource.**

### [C#]

```csharp
// Sets the datasource.
ArrayList USStates = new ArrayList();

USStates.Add(new USState("Washington", "WA"));
USStates.Add(new USState("West Virginia", "WV"));
USStates.Add(new USState("Wisconsin", "WI"));
USStates.Add(new USState("Wyoming", "WY"));

listBox1.DataSource = USStates;
```

## API Reference

### Essential Tools for Windows Forms

1. **ComboBoxBase**

   - **Properties**
     - `ListControl`: Specifies the ListControl that will be used in the dropdown portion of ComboBoxBase.
     - `Size`: Specifies the size of the ComboBoxBase control.

   - **Methods**
     - `SetDataSource`: Sets the data source for the ComboBoxBase control.

### Example

```csharp
private void InitializeComboBoxBase()
{
    // Step 1: Create instances
    private Syncfusion.Windows.Forms.Tools.ComboBoxBase comboBoxBase1;
    private System.Windows.Forms.ListBox listBox1;

    // Step 2: Initialize controls
    this.comboBoxBase1 = new Syncfusion.Windows.Forms.Tools.ComboBoxBase();
    this.listBox1 = new ListBox();

    // Step 3: Configure ComboBoxBase
    this.comboBoxBase1.ListControl = this.listBox1;
    this.comboBoxBase1.Size = new Size(120, 20);

    // Step 4: Set the data source
    ArrayList USStates = new ArrayList();
    USStates.Add(new USState("Washington", "WA"));
    USStates.Add(new USState("West Virginia", "WV"));
    USStates.Add(new USState("Wisconsin", "WI"));
    USStates.Add(new USState("Wyoming", "WY"));

    listBox1.DataSource = USStates;
}
```

<!-- tags: [ComboBoxBase, ListBox, Windows Forms, dataSource, dropdown, Essential Tools] keywords: [ComboBoxBase, ListBox, data source, dropdown list, Windows Forms, Syncfusion] -->
```