```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_030.jpeg
document_name: grouping
page_number: 030
page_id: grouping#page_030
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:27Z
fidelity: lossless
 -->

### Essential Grouping

![Console Showing Two Sets of Output](https://syncfusion.com/documentation/grouping/images/figure_13.png)

*Figure 13: Console Showing Two Sets of Output (Directly from the List and from the Engine)*

#### 4.2 Using Grouping

The Grouping of data is one type of data analysis technique. It is natural to organize data into groups. For example, you may want to group your sales details by months and get the total sales on a month-by-month basis. The following sections elaborate on this:

##### 4.2.1 Grouping a Table

In this lesson, you will start working with the `GroupingEngine` object to see how to apply a grouping to the data as well as summarize the data. In the `Data Binding` section, you used the `groupingEngine.Table.Records` collection to access the data in the `GroupingEngine` object. The `groupingEngine.Table` property is the property of the `GroupingEngine` that holds the actual data needed by Essential Grouping.

You will now look at the property that holds the schema information that is associated with the data, i.e., the `groupingEngine.TableDescriptor` property. For example, the `TableDescriptor.Columns` property holds a collection of `ColumnDescriptor` objects that define the schema information on the columns in the data.
```