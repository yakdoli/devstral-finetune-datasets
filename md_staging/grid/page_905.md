```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_905.jpeg
document_name: grid
page_number: 905
page_id: grid#page_905
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:47:46Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- The page focuses on using the Field Chooser feature to customize the view of a grid by enabling column visibility based on user selection.
- It provides details on associating the Field Chooser with the Grid Grouping control to add or remove columns.
- Example code snippets are provided for initializing the Field Chooser in both C# and VB.NET.

### Content

#### 4.3.4.6.3 Grid Field Chooser

The view of a grid can be customized based on column visibility by using a plug-in utility called Field Chooser. A Field Chooser can be associated with Grid Grouping control to add or remove columns from a grid. It can be done by initializing the FieldChooser class where the constructor takes a parameter as a Grid Grouping control object.

Enabling the Field Chooser allows the user to right-click on a column header and select Field Chooser menu item to view the Field Chooser dialog. This dialog would list all the column names with check boxes beside them. The required columns can be made visible in the grid by selecting the check box adjacent to the required column.

The following code example illustrates the usage of Field Chooser.

- **C#**
    ```csharp
    FieldChooser fchooser = new FieldChooser(this.gridGroupingControl1);
    ```

- **VB.NET**
    ```vb
    Dim fchooser As FieldChooser = New FieldChooser(Me.gridGroupingControl1)
    ```

---

### Summary
- The Field Chooser utility is a powerful tool for customizing the grid view dynamically by allowing users to show or hide columns based on their needs.
- The integration is straightforward, requiring the initialization of the FieldChooser class with the Grid Grouping control as an argument.
- Code examples are provided for both C# and VB.NET to facilitate quick implementation.

---

### Notes
- For more details, refer to the following browser sample:
  ```
  <Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Grouping Grid Layout\Employee View Demo
  ```

---

<!-- tags: [Grid, FieldChooser, GridGrouping, Customization, ColumnVisibility, C#, VB.NET] keywords: [Grid, Field Chooser, Dynamic Column Visibility, Customization, GridGrouping, Windows Forms, Syncfusion] -->
```