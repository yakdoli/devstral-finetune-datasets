```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_705.jpeg
document_name: grid
page_number: 705
page_id: grid#page_705
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:34:00Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Grid Grouping control provides inbuilt support to group the data by more than one column. It is as simple as adding the column names to the GroupedColumns collection. With multicolumn grouping, the grouping grid organizes the data in a hierarchical structure showing groups in different levels. In the below image, you see the Employees data grouped by Title and Country columns.

## Multi Column Grouping

![Figure 279: Multi Column Grouping](<image>)

### Note: For more details, refer the following browser sample:

- `<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Grouping\Multi Column Grouping Demo`

## Grouping Through Designer

### Overview

- Grouping can also be done at design time. After binding the dataset to the grouping grid, open the TableDescriptor node in the property grid of the Grid Grouping control. In that, accessing the GroupedColumns property will open the SortColumnDescriptorCollection Editor. Clicking the Add button will add an existing column from the dataset. By using the drop down Name, you can change the column by which you want to group the table data. You can also specify the sort order for that column using the SortDirection property.

The below image depicts this process.

### Content

## Grid Grouping Design-Time Configuration

### Steps to Group Columns

1. **Bind the Dataset**:
   - Connect your dataset to the Grid Grouping control.

2. **Access TableDescriptor**:
   - Open the property grid of the Grid Grouping control and locate the TableDescriptor node.

3. **Access GroupedColumns**:
   - Click on the GroupedColumns property to open the SortColumnDescriptorCollection Editor.

4. **Add Columns for Grouping**:
   - Click the Add button to add an existing column from the dataset.
   - Use the drop-down Name to select the column by which you wish to group the data.

5. **Set Sort Order**:
   - Use the SortDirection property to specify the sort order for the selected column.

### Visualization

The below image depicts the process:
![Figure: Grouping Through Designer](<image comes here>)

### Conclusion

This section provides a detailed walkthrough for setting up multi-column grouping in the Grid Grouping control of Syncfusion Winforms, both programmatically and through the designer.

### Additional References
- For a deeper understanding, refer to the provided browser sample path.
- Consult the Grid control documentation for further customization options and advanced features.

<!-- tags: grid, grouping, windows forms, designer, multicolumn grouping, dataset binding -->
```