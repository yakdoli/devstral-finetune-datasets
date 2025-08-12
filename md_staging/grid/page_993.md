```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_993.jpeg
document_name: grid
page_number: 993
page_id: grid#page_993
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:53:28Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## 4.3.4.13.1 Custom Grouping

### Overview
- By default, data rows with matching values in a grouping column are combined into a single group. Customization allows you to categorize records as needed.
- Custom Grouping involves adding a custom `Categorizer` object to `SortColumnDescriptor` for grouping logic.
- A custom `Comparer` object can also be added for sorting control.
- Adjacent records in sorted columns are grouped using the custom `Categorizer`.
- Custom `Comparer` and `Categorizer` objects are created by implementing `IComparer` or `ICategorizer` interfaces.

### Content
By default, the data rows having a matching value in a grouping column will be combined into a single group. If this does not suit your requirements, you can customize the grouping logic so that you can categorize the records as you need.

Custom Grouping can be achieved by adding a custom **Categorizer** object to **SortColumnDescriptor** that defines the group. You can also add a custom **Comparer** object to the **SortColumnDescriptor**. When a column is grouped, it is first sorted. The **Comparer** object allows you to control how the sorting is done on your column. Once the column is sorted, the custom **Categorizer** is used to determine which adjacent records in the sorted column belong to the same group. To create custom **Comparer** and **Categorizer** objects, you define classes that implement either **IComparer** (one method) or **ICategorizer** (two methods).

#### Example

Say you have a column with values for 0 to 50, and you want to have them grouped so that values less than 10 are in one group, values 10-20 are in another, values 20-30 in another, and so on. The following code example illustrates how to achieve this by using a **Custom Categorizer**.

1.  **Create a datasource and bind it to a grid grouping control.**

    ```csharp
    // Create the data source.
    private DataTable GetDataTable()
    {
        DataTable dt = new DataTable("MyTable");

        int nCols = 4;
        int nRows = 50;

        for (int i = 0; i < nCols; i++)
            dt.Columns.Add(new DataColumn(string.Format("Col{0}", i)));

        Random r = new Random();
        for (int i = 0; i < nRows; ++i)
        {
            DataRow dr = dt.NewRow();
    ```

<!-- tags: [syncfusion-sdk, windowsforms, grid, custom-grouping, categorizer, comparer, sortcolumndescriptor, icategorizer, icomparer, grouping, data-grouping] keywords: [custom grouping, data grouping, grouping column, categorizer, comparer, sortcolumn] -->
```