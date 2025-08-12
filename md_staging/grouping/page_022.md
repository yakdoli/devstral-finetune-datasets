```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_022.jpeg
document_name: grouping
page_number: 022
page_id: grouping#page_022
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:04Z
fidelity: lossless
-->

# Essential Grouping

## Concepts and Features

This section comprises the following subsections:

- **Data Binding** - This section elaborates on the procedure to setup a datasource for the Grouping engine.
- **Using Grouping** - In this section, you will see how to group the data, add summaries and locate a particular summary value for a particular group.
- **Data Manipulation** - This section will give you information about the additional concepts that are necessary for the complete customization of a spreadsheet. You will also learn about data validation, macros / VBA support, and named ranges. Also included is important information on protection, how to read contents, and implementing ASP.NET usage.
- **Algebra Supported in Expressions / Filters**

### 4.1 Data Binding

**Essential Grouping** lets you sort, group and summarize data. The data needs to be an `IList` object. For this lesson, we will use an `ArrayList` of custom objects which have four public properties: A, B, C, and D.

The below section illustrates how to access the data that is bound to the grouping engine.

#### Iterating Through the Data

This section elaborates on the procedure to setup a datasource for the Grouping engine in the below topics.

### 4.1.1 Creating an ArrayList of Objects

The first thing you need to do is to derive a class that will serve as your custom object.

1. In Visual Studio .NET, select **Files -> New -> Project**. Then using either C# or VB.NET, select the Console Application project template to create a new Console Application, and name it **GroupingSample**.

<!-- tags: [product, module, control, api, version?] keywords: [data binding, grouping, data manipulation, algebra expressions, filters, Ilist, ArrayList, custom objects, Essential Grouping, Sorting, Grouping, Summarizing, Visual Studio .NET, Console Application, GroupingSample] -->
```