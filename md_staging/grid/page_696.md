```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_696.jpeg
document_name: grid
page_number: 696
page_id: grid#page_696
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:34:39Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

bl.Add(New CustomClass(105, "Mayumi", "Ohno", "Calle del Rosal 4", "Oviedo"))

3. Assign this list to the grouping grid's DataSource.

```csharp
this.gridGroupingControl1.DataSource = bl;
```

```vb.net
Me.GridGroupingControl1.DataSource = bl
```

4. Finally, run the sample. Your grid will look like this.

| LastName | Address              | FirstName | ID   | City          |
|----------|----------------------|-----------|------|---------------|
| Cooper   | 49 Gilbert St.      | Charlotte | 101 | London        |
| Burke    | P.O. Box 78934      | Shelley   | 102 | New Orleans   |
| Murphy   | 707 Oxford Rd.      | Regina    | 103 | Ann Arbor     |
| Nagase   | 9-8 Sekimai Musashino-shi | Yoshi   | 104 | Tokyo         |
| Ohno     | Calle del Rosal 4   | Mayumi    | 105 | Oviedo        |

**Figure 275: Implementing and binding a Generic Collection to the Grid Grouping Control**

**Note:** For more details, refer the following browser sample:

<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Custom Collections\Generic Collection Demo

## 4.3.4.2.4 Unbound Mode

The Grid Grouping control can be operated in **Unbound Mode**. In unbound mode, you can add your own columns to the grouping grid along with the other bound columns.

### Implementation
```markdown
© 2013 Syncfusion. All rights reserved.
```
<!-- tags: [Grid, Grouping Grid, Windows Forms, Data Binding, Unbound Mode, Generic Collection] keywords: [Essential Grid, Syncfusion, Grouping, UnboundMode, DataSource, CustomCollection] -->
```