---
title: "grouping - Syncfusion SDK Documentation"
type: "api-documentation"
framework: "syncfusion"
version: "v11"
processing_mode: "Process Isolation (프로세스 격리)"
extracted_date: "1754722943.877492"
optimized_for: ["llm-training", "rag-retrieval"]
scaling_approach: "3"
---

<!-- 페이지 1 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_001.jpeg
document_name: grouping
page_number: 001
page_id: grouping#page_001
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:57:54Z
fidelity: lossless
-->

# Syncfusion Essential Studio 2013 Volume 4 - v.11.4.0.26

## Overview
- Featured documentation for Essential Studio 2013 Volume 4.
- Focus on grouping functionalities in WinForms.
- Version details provided: v.11.4.0.26.

## Content

### Essential Grouping

#### Introduction to Grouping in WinForms
- **Grouping Functionality**: Essential Grouping provides advanced grouping and sorting capabilities for WinForms applications.
- **Use Cases**: Simplify the organization of large datasets by categorizing them into logical groups for easier navigation and analysis.

#### Key Features
- **Customizable Grouping**: Allows developers to define group levels based on specific data fields.
- **Dynamic Grouping**: Supports both static and dynamic grouping options for varying data scenarios.
- **Group Aggregations**: Generate summaries or statistics for grouped data, enhancing data insights.
- **User-Interactive Grouping**: Enable users to interactively collapse and expand groups within the application.

#### Implementation Steps
1. **Setting Up the Control**: Integrate the Essential Grouping control into your WinForms project.
2. **Defining Group Criteria**: Specify the fields or conditions for grouping.
3. **Customizing Appearance**: Adjust the visual representation of groups, including headers and summary rows.
4. **Performance Optimization**: Implement best practices to ensure smooth performance with large datasets.

#### Example Code Snippet
```csharp
// Setting up the grouping control
GridGroupingControl grid = new GridGroupingControl();
grid.FirstRecordFirstDisplayColumn = true;

// Defining group level
GridGroupDescription gd = new GridGroupDescription();
gd.GroupOptions.GroupHeaderCaption = "Total Sum";
gd.GroupOptions.ShowFooter = true;
grid.TableGroupInfo.Add(gd);

// Adding aggregate functions
GridAggregateDescription ad = new GridAggregateDescription();
ad.AggregateExpression = "[Total] = [Sales]";
ad.AggregateFormat = "[Aggregate]:{0:C}";
gd.AggregateDescriptions.Add(ad);

// Loading data
grid.DataSource = dataSet.Tables["SalesData"];
grid.DataMember = "SalesData";
```

#### Customization Options
- **Group Header Layout**: Modify the design and placement of group headers.
- **Sorting within Groups**: Allow users to sort data within individual groups.
- **Group Footers**: Display summary or aggregate data in group footers.
- **Interactive Features**: Enable drag-and-drop functionality for reordering groups.

#### Troubleshooting and Best Practices
- **Handling Large Datasets**: Optimize memory usage and loading times by paging data.
- **Runtime Customization**: Adjust grouping dynamically based on user preferences.
- **Error Handling**: Implement robust error handling for invalid group criteria or data mismatch issues.

### API Reference
#### `GridGroupingControl`
- **Method**: `AddGroupDescription`
- **Parameter**: `GridGroupDescription`
- **Usage**: Add group descriptions to define grouping criteria.

#### `GridGroupDescription`
- **Property**: `GroupOptions`
- **Example**: `gd.GroupOptions.GroupHeaderCaption = "Total Sum";`

### Code Examples
#### Creating and Configuring Groups
```csharp
// Initialize the grouping control
GridGroupingControl gridGroupingControl = new GridGroupingControl();

// Configure group description
GridGroupDescription groupDescription = new GridGroupDescription();
groupDescription.GroupOptions.GroupHeaderCaption = "Products";
groupDescription.GroupOptions.CaptionFormat = "{0}: {1}";
gridGroupingControl.TableGroupInfo.Add(groupDescription);

// Load data source
gridGroupingControl.DataSource = productsDataSource;
```

#### Handling Group Aggregations
```csharp
// Adding an aggregation description
GridAggregateDescription aggregateDescription = new GridAggregateDescription();
aggregateDescription.AggregateExpression = "[Total] = [Quantity]*[Price]";
aggregateDescription.AggregateFormat = "Total: {0:C}";
groupDescription.AggregateDescriptions.Add(aggregateDescription);
```

### Appendices
- **Support Documentation**: Refer to the official Syncfusion documentation for additional information.
- **Online Resources**: Explore tutorials and sample projects available on Syncfusion’s website.

### Cross References
- See also: Other WinForms controls and features in Syncfusion Essential Studio 2013.

<!-- tags: [WinForms, Grouping, Data Management, Syncfusion Winforms, Essential Studio, Version 11.4.0.26] keywords: [grouping, grid grouping, data aggregation, dynamic grouping, group headers, summary rows, customization, performance optimization] -->
```

---

<!-- 페이지 2 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_005.jpeg
document_name: grouping
page_number: 005
page_id: grouping#page_005
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:20Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- The document focuses on the **Essential Grouping** feature in Syncfusion Winforms, detailing its key functionalities and technical aspects.

## Content

### Grouping in Data Grid

#### Key Features
Some of the key features of Essential Grouping are listed below:

- **Grouping supports data presentation techniques** like sorting, grouping, adding caption, and summary information for the groups.
- **Grouping also supports nested tables and hierarchies** in the form of related tables.
- **The grouping technology uses balanced binary trees** as the core data structure instead of arrays. Binary trees have the advantage where parent branches can cache information about their children. This allows position information and summary information to be cached in parent branches, facilitating quick inserts of new records honoring any sort of criteria that is applied. Inserting, removing, and moving of records takes \(\text{Log}_2(n)\) operations. With linear lookup structures such as an ArrayList, each of these operations would take \(O(n)\) operations.
- **Expressions can be any well-formed algebraic combination** of property (column) names enclosed with brackets (\[\]), numerical constants and literals, and the algebraic and logical operators.

Figures and tables, as shown in the image, provide a visual representation of these key features, including a data grid with summary statistics for columns A and B.

### Visual Representation

#### Figure 1: Grouping in Data Grid
The figure showcases a data grid with rows of numerical data under columns A and B. Summary statistics for columns A and B, such as Maximum, Minimum, Total, and Count, are displayed. Additionally, there is functionality to generate new data, indicating the dynamic nature of grouping.

## Cross References
- For further information, refer to the related sections on nested tables, binary tree caching, and grouping expressions.

<!-- tags: [grouping, data grid, balanced binary trees, data presentation, sorting, nested tables, hierarchical data, algebraic expressions, arrays, ArrayList] keywords: [syncfusion, grouping, data presentation, binary trees, summary statistics, grouping expressions] -->
```

---

<!-- 페이지 3 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_009.jpeg
document_name: grouping
page_number: 009
page_id: grouping#page_009
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:34Z
fidelity: lossless
-->

# Essential Grouping

## 2 Installation and Deployment

This section covers information on the install location, samples, licensing, patches update and updation of the recent version of Essential Studio. It comprises the following subsections:

### 2.1 Installation

For step-by-step installation procedure for the installation of Essential Studio, refer to the Installation topic under Installation and Deployment in the Common UG.

#### See Also

For licensing, patches and information on adding or removing selective components refer the following topics in Common UG under Installation and Deployment.

- Licensing
- Patches
- Add / Remove Components

### 2.2 Where to Find Samples?

This section provides the location of the installed samples and describes the procedure to run the samples in the sample browser and online. It also lists the location of utilities, assemblies, and source code.

#### Sample Installation Location

Sample install locations for different platforms are listed below:

#### Windows Forms Samples

The Grouping Windows Forms samples are installed in the following location:

- `[Install Location]\...\Syncfusion\Essential Studio\[Version Number]\Windows\Grouping.Windows\Samples\2.0`

#### ASP.NET Samples

The Grouping Web samples are installed in the following location:

- `[Install Location]\...\Syncfusion\Essential Studio\[Version Number]\Web\Grouping.Web\Samples\3.5`

#### Viewing Samples

To view the samples:

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

## RAG Annotations
<!-- tags: [installation, deployment, Essential Grouping, Essential Studio, samples, licensing, patches, components] keywords: [installation procedure, sample browser, utilities, assemblies, source code, Grouping Windows Forms, Grouping Web] -->
```

---

<!-- 페이지 4 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_013.jpeg
document_name: grouping
page_number: 013
page_id: grouping#page_013
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:47Z
fidelity: lossless
-->

## Essential Grouping

### Overview
- Demonstration of the ASP.NET Sample Browser.
- Explanation of how to access different features like Grouping from the sample browser.
- Detailed description of the functionalities offered by Essential DocIO.

### Content

#### Example: ASP.NET Sample Browser

##### Figure: ASP.NET Sample Browser

```plaintext
Essential Studio 2012 Vol 3 | ASP.NET
```

**DocIO description**  
Essential DocIO is a 100% native .NET library that generates fully functional Microsoft Word documents in native Word format. Essential DocIO library can be used in any .NET environment including C#, VB.NET, and managed C++. Essential DocIO is a Non-UI component that is used on Windows Forms, WPF, and Web applications. Essential DocIO can create and preserve documents. It has unique features like find and replace, mail merge, and conversions.

![Sample Browser Interface](https://via.placeholder.com/300x200?text=Sample+Browser+Interface)

**Navigation from the Sample Browser Interface**  
To access the Grouping samples:
1. Open the ASP.NET Sample Browser.
2. On the left pane, ensure you are in the desired section (in this case, "DocIO").
3. Click "Grouping" from the bottom-left pane. The Grouping samples are displayed.

**Copyright Notice**
- Copyright © 2001-2012 Syncfusion Inc.
- Copyright © 2013 Syncfusion. All rights reserved.

#### Accessing Grouping Samples

**Step-by-Step Instructions**
1. Launch the ASP.NET Sample Browser.
2. Navigate to the applicable section (e.g., DocIO).
3. From the bottom-left pane, select "Grouping."

**Conclusion**
This section provides a clear guide on how to access and utilize the Grouping feature within the ASP.NET Sample Browser, showcasing the capabilities and functionalities of Essential DocIO.

## API Reference (Not Applicable)

## Code Examples (Not Applicable)

## RAG Annotations
<!-- tags: [essential-grouping, asp-net, sample-browser, docio, grouping, features, explore] keywords: [essential studio, 2012 vol 3, asp.net, essential docio, non-ui component, mail merge, find and replace, document creation, document preservation, sample browser, ui navigation, group samples] -->
```

---

<!-- 페이지 5 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_017.jpeg
document_name: grouping
page_number: 017
page_id: grouping#page_017
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:01Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- A guide to deploying Essential Grouping in both Windows applications (WPF) and ASP.NET applications.
- Instructions for creating a new ASP.NET Web Site project in Visual Studio.

## Content

### Deploying Essential Grouping in a Windows Application
#### Step 6: Deploy Essential Grouping
- A Windows application is already created.
- You need to deploy Essential Grouping into this Windows application.
- Refer to the Windows / WPF topic for detailed information.

### Creating an ASP.NET Application

#### Overview
- To know how to deploy a web application, refer to the **ASP.NET Behind the scenes** section in the Getting Started guide of the Essential Studio documentation.

#### Steps to Create a New ASP.NET Web Site
1. Open **Microsoft Visual Studio**.
2. Go to the **File** menu and click **New Website**.
3. In the **New Website** dialog, select the **ASP.NET Web Site** template.
4. Name the website and click **OK**.

---

#### Figure 9: New Web Site dialog box

![](attachment:Figure_9_New_Web_Site_dialog_box.png)

**Figure 9: New Web Site dialog box**

---

A web application is created.

## API Reference

## Code Examples

## Page-level Navigation/TOC

## Cross References

### See also:
- Windows / WPF topic for detailed deployment info.
- ASP.NET Behind the scenes section in the Getting Started guide.

<!-- tags: [Essential Grouping, ASP.NET, WPF, Windows Application, Microsoft Visual Studio] keywords: [deploy, ASP.NET Web Site, template, Visual Studio, Essential Studio] -->
```

---

<!-- 페이지 6 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_021.jpeg
document_name: grouping
page_number: 021
page_id: grouping#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:13Z
fidelity: lossless
-->

# Essential Grouping

Refer to the document in the following path, for step by step process of Syncfusion assemblies' deployment in ASP.NET.

[http://www.syncfusion.com/support/user/uploads/webdeployment\_c883f681.pdf](http://www.syncfusion.com/support/user/uploads/webdeployment_c883f681.pdf)

**Note:** Application with Essential Grouping needs the following dependent assemblies for deployment.

- Syncfusion.Shared.Base.dll
- Syncfusion.Shared.Web.dll
- Syncfusion.Grid.Base.dll
- Syncfusion.Grid.Windows.dll
- Syncfusion.Grouping.Base.dll
- Syncfusion.Grouping.Web.dll
- Syncfusion.Grid.Grouping.Base.dll

Essential Grouping is now deployed in your ASP.NET application.

<!-- tags: [product, module, control, api, version?] keywords: [Essential Grouping, deployment, ASP.NET, application, Syncfusion.Shared.Base.dll, Syncfusion.Shared.Web.dll, Syncfusion.Grid.Base.dll, Syncfusion.Grid.Windows.dll, Syncfusion.Grouping.Base.dll, Syncfusion.Grouping.Web.dll, syncfusion.winforms, 11.4.0.26] -->
```

---

<!-- 페이지 7 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_025.jpeg
document_name: grouping
page_number: 025
page_id: grouping#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:22Z
fidelity: lossless
-->

## Overview

- Essential Grouping functionality demonstrated using a custom `MyObject` class.
- Example code demonstrates initializing the `MyObject` class with specific properties and how they are set.

## Content

### Example Code

```vb
Sub Main()
End Sub

Public Class MyObject
    Private aValue As String
    Private bValue As String
    Private cValue As String
    Private dValue As String

    Public Sub New(ByVal i As Integer)
        aValue = String.Format("a{0}", i)

        ' Use digit only.
        bValue = String.Format("{0}", i)
        cValue = String.Format("c{0}", i Mod 3)
        dValue = String.Format("d{0}", i Mod 2)
    End Sub

    Public Property A() As String
        Get
            Return aValue
        End Get
        Set(ByVal Value As String)
            aValue = Value
        End Set
    End Property

    Public Property B() As String
        Get
            Return bValue
        End Get
        Set(ByVal Value As String)
            bValue = Value
        End Set
    End Property

    Public Property C() As String
        Get
            Return cValue
        End Get
        Set(ByVal Value As String)
            cValue = Value
        End Set
    End Property

    Public Property D() As String
        Get
            Return dValue
        End Get
    End Property
End Class
```

<!-- tags: [syncfusion, winforms, essential grouping, myobject] keywords: [essential grouping, myobject class, property initialization, modulo operation, string formatting] -->
```

---

<!-- 페이지 8 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_029.jpeg
document_name: grouping
page_number: 029
page_id: grouping#page_029
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:34Z
fidelity: lossless
-->

# Essential Grouping

## Overview

- Demonstrates how to iterate through a `Records` collection and display output in the Console.
- Explains the concept of interacting with the operating system using the Console interface.
- Provides C# and VB.NET examples for accessing data directly from the Engine.

## Content

### Iterating through the Records Collection

Add the following code to the main function. This code will iterate through the `Records` collection and will display the output in the Console.

#### Console Interface Note

> **Note:**  
> Console is a text-only user interface that allows the user to interact with the operating system or text-based application by entering the text through the keyboard and reading the text output from the computer screen.

#### C# Example

```csharp
// Access the data directly from the Engine.
foreach (Record rec in groupingEngine.Table.Records)
{
    MyObject obj = rec.GetData() as MyObject;
    if (obj != null)
    {
        Console.WriteLine(obj);
    }
}

// Pause
Console.ReadLine();
```

#### VB.NET Example

```vb.net
' Access the data directly from the Engine.
Dim rec As Record
For Each rec In groupingEngine.Table.Records
    Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
        Console.WriteLine(obj)
    End If
Next rec

' Pause
Console.ReadLine()
```

### Explanation

- **Accessing Data:**  
  The code demonstrates how to access data directly from the `groupingEngine.Table.Records` collection. Each record is processed using a loop, and its data is retrieved using the `GetData()` method.
  
- **Type Casting:**  
  The data retrieved from each record is cast to the `MyObject` type using `as` in C# and `CType` in VB.NET. The code checks if the cast was successful (`obj != null` in C# and `Not obj Is Nothing` in VB.NET) before displaying the object.

- **Pause Option:**  
  The `Console.ReadLine()` method is used to pause the program, allowing the user to see the output in the Console before the program terminates.

### Key Steps

1. **Iterate through Records:**  
   Use a `foreach` loop in C# or a `For Each` loop in VB.NET to iterate through the `Records` collection.

2. **Retrieve Data:**  
   Call the `GetData()` method on each record to retrieve its data and cast it to the appropriate type.

3. **Check for Null:**  
   Ensure that the retrieved object is not `null` before attempting to display it in the Console.

4. **Display Output:**  
   Use `Console.WriteLine()` to display the retrieved data in the Console.

5. **Pause Program:**  
   Use `Console.ReadLine()` to pause the program, allowing the user to view the output.

## API Reference

### Methods

- `GetData()`  
  Retrieves the data associated with a record.
- `Console.WriteLine()`  
  Displays the specified data in the Console.
- `Console.ReadLine()`  
  Waits for the user to press a key before continuing.

## Code Examples

### C# Example

```csharp
// Access the data directly from the Engine.
foreach (Record rec in groupingEngine.Table.Records)
{
    MyObject obj = rec.GetData() as MyObject;
    if (obj != null)
    {
        Console.WriteLine(obj);
    }
}

// Pause
Console.ReadLine();
```

### VB.NET Example

```vb.net
' Access the data directly from the Engine.
Dim rec As Record
For Each rec In groupingEngine.Table.Records
    Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
        Console.WriteLine(obj)
    End If
Next rec

' Pause
Console.ReadLine()
```

## RAG Annotations

<!-- tags: [product: Syncfusion Winforms, version: 11.4.0.26] keywords: [Essential Grouping, Records collection, Console interface, C# example, VB.NET example, GetData(), Console.WriteLine(), Console.ReadLine()] -->
```

---

<!-- 페이지 9 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_033.jpeg
document_name: grouping
page_number: 033
page_id: grouping#page_033
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:58Z
fidelity: lossless
-->

# Essential Grouping

| SortedColumns | Holds sorted properties. |
| --- | --- |

## 4.2.2 Accessing a Particular Group

Grouping is a recursive process whereby a data source may be grouped several times. This leads to the recursive situation of groups having sub-groups and so on. In recursion, there is usually some primary node or initial starting point that you use, to work with the recursive objects. In Grouping, the initial starting point is `Engine.Table.TopLevelGroup`. This is the 'primary' Group object.

The `Grouping.Group` class has two properties that are used to recursively access nested groups and the `Record` objects contained in the terminal group. The properties are:

- `Group.Groups` and `Group.Records`.

1. `Group.Groups` is a collection of `Group` objects that are contained in the parent `Group`, and `Group.Records` is a collection of `Records` that are contained in the parent `Group`.

2. At most one of these collections will actually hold objects. If the `Groups` collection is populated, this implies that the Group has sub-groups and there are no records.

3. If the `Records` collection is populated, then it implies that this Group is a terminal group with records, but there are no sub-groups.

Your first task is to add a recursive method to either display records if the Group has records, or to recursively call itself to display any records of its child groups.

1. Add the following code below the `Main` method to implement a recursive method to display records in a Group.

```csharp
private static void ShowRecordsUnderGroup(Group g)
{
    if (g.Records != null && g.Records.Count > 0)
    {
        // Displaying the data for all the records in each group.
        foreach (Record rec in g.Records)
        {
            MyObject obj = rec.GetData() as MyObject;
            if (obj != null)
        }
    }
}
```

## Cross References
- See also: `Group`, `Record`, `Engine.Table.TopLevelGroup`.

<!-- tags: [Syncfusion Winforms, grouping, recursion, GroupRecord, TerminalGroup] keywords: [Grouping, Recursive Group, Nested Groups, Display Records, Group Object, Terminal Group, Records] -->

---

<!-- 페이지 10 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_037.jpeg
document_name: grouping
page_number: 037
page_id: grouping#page_037
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:12Z
fidelity: lossless
-->

## Essential Grouping

### VB.NET Code Example

```vb
' Show all records under the TopLevelGroup.
ShowRecordsUnderGroup(groupingEngine.Table.TopLevelGroup)

' Pause
Console.ReadLine()
```

## 4.2.3 Adding a Summary

**Overview**
- Essential Grouping allows summarizing data by adding `SummaryDescriptor` objects to the schema information stored in the `Engine.TableDescriptor.Summaries` collection.
- Multiple summaries can be added by including several `SummaryDescriptors`.

### Content

Essential Grouping lets you summarize your data by adding `SummaryDescriptor` objects to the schema information that is stored in the `Engine.TableDescriptor.Summaries` collection. You can have multiple summaries by adding several `SummaryDescriptors`.

At the bottom of the Main method, add this code to create a summary item for the Engine.

#### C# Example

```csharp
// Create a summary that computes the Int32Aggregate calculations on property B.
SummaryDescriptor sdBInt32Agg = new SummaryDescriptor("BInt32Agg", "B", SummaryType.Int32Aggregate);

// Add this summary to the Summaries collection.
groupingEngine.TableDescriptor.Summaries.Add(sdBInt32Agg);
```

#### VB.NET Example

```vb
' Create a summary that computes the Int32Aggregate calculations on property B.
Dim sdBInt32Agg As New SummaryDescriptor("BInt32Agg", "B", SummaryType.Int32Aggregate)

' Add this summary to the Summaries collection.
groupingEngine.TableDescriptor.Summaries.Add(sdBInt32Agg)
```

### Additional Notes

- There are several overloads of the constructor for `SummaryDescriptor`. Here, we are using the overload that accepts a `SummaryType` enum as the third argument.
- The `SummaryType` enum allows you to pick out some predefined calculations such as the `Int32Aggregate` functions like `Max`, `Min`, `Sum`, and `Average`.
- There are enums that specify double, boolean, and other aggregate types.
- Here, we choose `Int32` as that is the type of value you will see in the `B` property in the data.

---

<!-- tags: [product, module, control, api, version?] keywords: [grouping, summarydescriptor, sum, max, min, average, int32aggregate, Engine.TableDescriptor.Summaries, EssentialGrouping] -->
```

---

<!-- 페이지 11 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_041.jpeg
document_name: grouping
page_number: 041
page_id: grouping#page_041
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:27Z
fidelity: lossless
-->

# Essential Grouping

```vb
Sub Main()
    ' Create an ArrayList of random MyObjects.
    Dim list As New ArrayList()
    Dim r As New Random()

    Dim i As Integer
    For i = 0 To 10
        list.Add(New MyObject(r.Next(5)))
    Next

    ' Create a Grouping.Engine object.
    Dim groupingEngine As New Engine()

    ' Set its data source.
    groupingEngine.SetSourceList(list)
End Sub
```

10. You are now ready to apply a filter to the data. Say for example you want to see only those items whose property D has the value d1. You must observe that D is a string that has non-numeric values. So, in this case you will need to use one of the string comparison operators (LIKE or MATCH) in your filter condition.

11. To add a filter condition, you will need to add a `RecordFilterDescriptor` to the `Engine.TableDescriptor.RecordFilters` collection.

### Do the following steps:

1. List the data before the filter.
2. Apply the filter by creating a `RecordFilterDescriptor`.
3. Add it to the `RecordFilters` collection.
4. List the filtered data.

**Note:** To list the data, instead of accessing the `Table.Records` collections, you were using the `Table.FilteredRecords` collections. The `FilteredRecords` collection only includes the records that satisfy all filters in the `RecordFilters` collection. Add this code at the end of the Main method.

12. Note that the constructor on the `RecordFilterDescription` takes an expression, `[D] LIKE 'd1'`. This expression will be `True` only for those items in the list where property D has the value d1.

```csharp
// Display the data before filtering.
```

## API Reference

- **Namespace:** `Syncfusion.Windows.Forms.Grouping`
- **Class:** `RecordFilterDescriptor`

### Methods and Properties
- `SetSourceList`: Method to set the data source for the grouping engine.

## Code Examples

Extracting all code exactly:

```csharp
// Display the data before filtering.
```

### Using the RecordFilterDescriptor

```csharp
// Example of using RecordFilterDescriptor to filter records.
```

## Page-level Navigation/TOC

- Creating and setting up a grouping engine.
- Applying filters using `RecordFilterDescriptor`.

<!-- tags: [grouping, filter, recordfilterdescriptor, data filtering, syncfusion winforms, version 11.4.0.26] keywords: [essentials, grouping engine, recordfilterdescriptor, filtering data, syncfusion, winforms] -->
```

---

<!-- 페이지 12 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_045.jpeg
document_name: grouping
page_number: 045
page_id: grouping#page_045
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:45Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Demonstrates filtering data on the console based on specific conditions.
- Explains how to add algebraic expressions to data objects using ExpressionFieldDescriptor.

## Content

### Filtering on the Console

![](attachment:Figure_18_data_filtered.png)

**Figure 18:** Screen Showing Data Filtered on [D] LIKE 'd1' OR [B] = 2

Filtering is applied to the data displayed in the console.

#### 4.3.2 Expressions

You can add new properties to your data object that are algebraic expressions involving other properties of the object.

To add an expression, you need to create an `ExpressionFieldDescriptor` and add it to the `Engine.TableDescriptor.Expression.Fields` collection. Here we illustrate this process by adding an expression that computes 2.1 times the value of property B plus 3.2.

#### Steps to Add an Expression

1. In the Console Application, comment out all the code that is in the `Main` method and add this code to create a data object and set it into the `GroupingEngine`.

```csharp
// Create an arraylist of random MyObjects.
ArrayList list = new ArrayList();
```

## API Reference

### ExpressionFieldDescriptor

- **Name**: ExpressionFieldDescriptor
- **Usage**: Used to define algebraic expressions for data objects.

### Engine.TableDescriptor.Expression.Fields

- **Name**: Expression.Fields
- **Usage**: Collection to store ExpressionFieldDescriptor objects.

## Code Examples

### Adding an Expression to a Data Object

```csharp
// Sample code to create an ExpressionFieldDescriptor.
ExpressionFieldDescriptor expressionField = new ExpressionFieldDescriptor();
expressionField.Expression = "2.1 * B + 3.2";
expressionField.FieldName = "ExpressionField";
tableDescriptor.Expression.Fields.Add(expressionField);
```

## Cross References

- See also: [Creating a GroupingEngine](#groupingengine), [Defining Table Descriptors](#tabledescriptors)

### RAG Annotations

<!-- tags: WinForms, Grouping, ExpressionFieldDescriptor, TableDescriptor keywords: filtering, expressions, algebraic, GroupingEngine, TableDescriptor -->
```

---

<!-- 페이지 13 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_049.jpeg
document_name: grouping
page_number: 049
page_id: grouping#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:58Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Demonstrates setting up a data source for grouping.
- Displays data before and after sorting.
- Sorts a specific column and displays the sorted result.
- Includes both C# and VB.NET examples for creating and using the GroupingEngine.

## Content

### Setting Up the Data Source and Displaying Records

#### C#
```csharp
// Set its datasource.
groupingEngine.SetSourceList(list);

// Display the data before sorting.
foreach (Record rec in groupingEngine.Table.Records)
{
    MyObject obj = rec.GetData() as MyObject;
    if (obj != null)
    {
        Console.WriteLine(obj);
    }
}

// Pause
Console.ReadLine();

// Sort column A.
groupingEngine.TableDescriptor.SortedColumns.Add("A");

// Display the data after sorting.
foreach (Record rec in groupingEngine.Table.FilteredRecords)
{
    MyObject obj = rec.GetData() as MyObject;
    if (obj != null)
    {
        Console.WriteLine(obj);
    }
}

// Pause
Console.ReadLine();
```

#### VB.NET
```vb
' Create an arraylist of random MyObjects.
Dim list As New ArrayList()
Dim r As New Random()

Dim i As Integer
For i = 0 To 9
    list.Add(New MyObject(r.Next(5)))
Next i

' Create a Grouping.Engine object.
Dim groupingEngine As New Engine()
```

### Key Features
- **Data Source**: Defines the source list for grouping.
- **Sorting**: Sorts the table by a specific column.
- **Display**: Shows the data before and after sorting.
- **Paused Execution**: Allows the user to view the output at different stages.

### Summary
This example showcases how to use the Syncfusion GroupingEngine to sort a table and display the records before and after the sorting operation. Both C# and VB.NET implementations are provided, demonstrating the integration of the GroupingEngine in WinForms applications.

### Cross References
- Refer to [Grouping Overview] for more details on grouping functionality.

### API Reference
- **GroupingEngine**: The main class for managing and manipulating grouped data.
  - **SetSourceList(list)**: Sets the source list for the grouping.
  - **Table.Records**: Gets the unfiltered records.
  - **Table.FilteredRecords**: Gets the records after applying filters and sorting.
  - **TableDescriptor.SortedColumns.Add(columnName)**: Adds a column to the sorted columns list.

### Code Examples
- The provided C# and VB.NET code snippets demonstrate how to:
  1. Set the data source for grouping.
  2. Display the records before sorting.
  3. Sort a specific column.
  4. Display the sorted records.

<!-- tags: [grouping, data_source, sorting, GroupingEngine, WinForms] keywords: [syncfusion, grouping engine, data display, table sorting, csharp, vb.net] -->
```


---

<!-- 페이지 14 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: grouping
page_number: 053
page_id: grouping#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:15Z
fidelity: lossless
-->

# Essential Grouping

```cpp
sy = int.Parse(y.ToString().Substring(1));
return sy - sx;
}
catch 
{ 
    throw new ArgumentException("A must be in the form 'an***'");
}
}
```

### [VB.NET]

```vb
Public Class AComparer
    Implements IComparer
    
    ' Implementing IComparer to define the object comparisons.
    Public Function Compare(ByVal x As Object, ByVal y As Object) As Integer _
        Implements IComparer.Compare
        
        If x Is Nothing And y Is Nothing Then
            Return 0
        Else
            If x Is Nothing Then
                Return -1
            Else
                If y Is Nothing Then
                    Return 1
                Else
                    Dim sx As Integer = 0
                    Dim sy As Integer = 0
                    Try
                        ' Ignoring the leading character to have numerical sorting.
                        sx = Integer.Parse(x.ToString().Substring(1))
                        sy = Integer.Parse(y.ToString().Substring(1))
                        Return sy - sx
                    Catch
                    End Try
                End If
            End If
        End If
    End Function
End Class
```

16. Add this code to the Main method to use this custom comparer to sort column A.

---

Copyright © 2013 Syncfusion. All rights reserved.

<!-- tags: [Syncfusion Winforms, Essential Grouping, Comparer, Custom Sorting] keywords: [Syncfusion Winforms, Custom Comparer, Compare Method, Object Comparison, Numerical Sorting] -->
```

---

<!-- 페이지 15 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_057.jpeg
document_name: grouping
page_number: 057
page_id: grouping#page_057
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:26Z
fidelity: lossless
-->

## Essential Grouping

- `<`, `>`, `=`, `<=`, `>=`, `<>`: less than, greater than, equal, less than or equal, greater than or equal, not equal
- match, like, in, between
- or, and, or

### Note

1. **Alpha constants used with `match` and `like` should be enclosed in apostrophes (`'`).**
2. **Logical operators return "1", if the logical expression is True and return "0", if the logical expression is False.**

Given below is some more information on special logical operators:

- **Match**  
  - Returns `1` if there is any occurrence of the right-hand argument in the left-hand argument.  
  **Example**  
  `[Company_Name]` match `'RTR'` returns `0` for any record whose CompanyName field does not contain `RTR` anywhere in the string.

- **Like**  
  - Checks if the field starts exactly as specified in the right-hand argument.  
  **Example**  
  `[Company_Name]` like `'RTR'` returns `1` for any record whose CompanyName field is exactly `'RTR'`.  
  You can use an asterisk as a wildcard.  
  `[Company_Name]` like `'RTR*'` returns `1` for any record whose CompanyName field starts with `'RTR'`.  
  `[Company_Name]` like `'*RTR'` returns `1` for any record whose CompanyName field ends with `'RTR'`.

- **In**  
  - Checks if the field value is any of the values listed in the right-hand operand. The collection of items used as the right-hand should be separated by commas and enclosed within braces `{ }`.  
  **Example**  
  `[code]` in `{1,10,21}` returns `1` for any record whose code field contains `1` or `10` or `21`.  
  `[Company_Name]` in `{RTR,MAS}` returns `1` for any record whose CompanyName field is `RTR` or `MAS`.

### Note
Spaces that are significant in the list, i.e., `{RTR,MAS}` is not the same as `{RTR, MAS}`.

```html
```

---

<!-- 페이지 16 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: grouping
page_number: 061
page_id: grouping#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:41Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Implements custom grouping calculations using custom functions.
- Demonstrates how to add and use custom functions in Expression columns.
- Provides examples in both C# and VB.NET.

### Custom Function Implementation

#### C# Example

```csharp
string[] ss = s.Split(comma);
if (ss.GetLength(0) != 2)
    throw new ArgumentException("Requires 2 arguments.");

double arg1, arg2;
if (double.TryParse(ss[0], System.Globalization.NumberStyles.Any, null, out arg1)
    && double.TryParse(ss[1], System.Globalization.NumberStyles.Any, null, out arg2))
{
    return Math.Abs(arg1 - 2 * arg2).ToString();
}
return "";
```

#### VB.NET Example

```vb
' Step 1
' Add function named Func that uses a delegate named ComputeFunc to define a custom calculation.
Dim evaluator As ExpressionFieldEvaluator =
    Me.groupingEngine.TableDescriptor.ExpressionFieldEvaluator
evaluator.AddFunction("Func", New
    ExpressionFieldEvaluator.LibraryFunction(ComputeFunc))

' Sample usage in an Expression column.
Me.groupingEngine.TableDescriptor.ExpressionFields.Add("test")
Me.groupingEngine.TableDescriptor.ExpressionFields("test").Expression = "Func([Col1], [Col2])"

' Step 2
' Define ComputeFunc that returns the absolute value of the 1st arg minus 2 * the 2nd arg.
Public Function ComputeFunc(ByVal s As String) As String

    ' Get the list delimiter (for en-us, it is a comma).
    Dim comma As Char =
        Convert.ToChar(Me.gridGroupingControl1.Culture.TextInfo.ListSeparator)
    Dim ss As String() = s.Split(comma)
    If ss.GetLength(0) <> 2 Then
        Throw New ArgumentException("Requires 2 arguments.")
    End If

    Dim arg1, arg2 As Double
    If Double.TryParse(ss(0), System.Globalization.NumberStyles.Any, Nothing, arg1) _
       AndAlso _
       Double.TryParse(ss(1), System.Globalization.NumberStyles.Any, Nothing, arg2) Then
        Return Math.Abs((arg1 - 2 * arg2)).ToString()
    End If
    Return ""
End Function
```

## Code Examples

### C# Implementation of Custom Function
The provided C# code defines a custom function that parses two arguments from a string, checks if they are valid doubles, and calculates the absolute difference between the first argument and twice the second argument.

### VB.NET Implementation of Custom Function
The VB.NET example demonstrates the addition of a custom function named `Func` to the `ExpressionFieldEvaluator`. It also includes the implementation of the `ComputeFunc` delegate, which performs a similar calculation as the C# example.

## See also
- [Expression Calculator](#expression-calculator)
- [TableDescriptor](#tabledescriptor)

<!-- tags: [Syncfusion, Winforms, Grouping, ExpressionCalculator, ExpressionFieldEvaluator] keywords: [custom functions, C#, VB.NET, grouping, expressions, calculations, delegates, tryParse, Math.Abs] -->
```

---

<!-- 페이지 17 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_065.jpeg
document_name: grouping
page_number: 065
page_id: grouping#page_065
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:58Z
fidelity: lossless
-->

## Essential Grouping

```csharp
RecordFilterDescriptor.name
Me.gridGroupingControl1.TableDescriptor.RecordFilters.Remove() ' Removes the RecordFilter associated by mentioning as index.
Me.gridGroupingControl1.TableDescriptor.RecordFilters.RemoveAt()
```

**Note:** To remove a particular filter, use the `groupingEngine.TableDescriptor.RecordFilters.Remove` or `groupingEngine.TableDescriptor.RecordFilters.RemoveAt`. To use `Remove`, you will need a reference to the `RecordFilterDescriptor` object that you want to delete or your `RecordFilterDescriptor` object would have to be named (setting the `RecordFilterDescriptor.Name` property or by passing a name string into its overloaded constructor).

### 5.7 How to Clear a Grouping?

To clear all grouping, call the `groupingEngine.TableDescriptor.GroupedColumns.Clear` method.

**[C#]**
```csharp
// Removes the grouping of all the grouped columns.
this.gridGroupingControl1.TableDescriptor.GroupedColumns.Clear();

// Removes grouping of the column mentioned as an argument.
this.gridGroupingControl1.TableDescriptor.GroupedColumns.Remove(Name);

// Removes grouping of the column mentioned as column index.
this.gridGroupingControl1.TableDescriptor.GroupedColumns.RemoveAt(index);
```

**[VB.NET]**
```vb
' Removes the grouping of all the grouped columns.
Me.gridGroupingControl1.TableDescriptor.GroupedColumns.Clear()

' Removes grouping of the column mentioned as an argument.
Me.gridGroupingControl1.TableDescriptor.GroupedColumns.Remove()

' Removes grouping of the column mentioned as column index.
Me.gridGroupingControl1.TableDescriptor.GroupedColumns.RemoveAt()
```

```html
<!-- tags: [Syncfusion, Winforms, Grouping, RecordFilter, GroupedColumns, Remove, RemoveAt, Clear] keywords: [grouping, recordfilter, groupedcolumns, remove, removeat, clear, Winforms, Syncfusion] -->
```

---

<!-- 페이지 18 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_069.jpeg
document_name: grouping
page_number: 069
page_id: grouping#page_069
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:02:10Z
fidelity: lossless
-->

# Essential Grouping

```csharp
Console.WriteLine("c1-group {0}, {1}, {2}", int32Summary.Sum, int32Summary.Average, int32Summary.Maximum)
```

## 5.12 How to Sort a Collection?

To sort your data, add the name of the property that you want to sort to the Engine.TableDescriptor.SortedColumns collection.

### Sorting in C#

```csharp
// Sort column A.
groupingEngine.TableDescriptor.SortedColumns.Add("A");
```

### Sorting in VB.NET

```vb
' Sort column A.
groupingEngine.TableDescriptor.SortedColumns.Add("A")
```

## API Reference

- **Namespace:** Engine.TableDescriptor
- **Property:** SortedColumns

### Parameters

- **Column Name:** The name of the property you want to sort by.

### Returns

- **Type:** void

## Code Examples

### C#

```csharp
using Syncfusion.Windows.Forms.Grid;

// Example of sorting a column in C#
GridEngine groupingEngine = new GridEngine();
groupingEngine.TableDescriptor.SortedColumns.Add("A");
```

### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Grid

' Example of sorting a column in VB.NET
Dim groupingEngine As GridEngine = New GridEngine()
groupingEngine.TableDescriptor.SortedColumns.Add("A")
```

### Explanation

- The `SortedColumns.Add` method is used to add the name of the column you want to sort to the SortedColumns collection.
- This method ensures that the data is sorted based on the specified column's property.

## See also

- [Grouping and Sorting Data](#)
- [Engine.TableDescriptor Reference](#)

<!-- tags: [grouping, sorting, columns, engine.tabledescriptor, csharp, vb.net, version: 11.4.0.26] keywords: [sort, collection, property, add, column, engine, tabledescriptor, sortedcolumns] -->
```

---

<!-- 페이지 19 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_002.jpeg
document_name: grouping
page_number: 002
page_id: grouping#page_002
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:57:54Z
fidelity: lossless
-->

# Contents

## Overview

1. **Introduction to Essential Grouping**  
   - **Prerequisites and Compatibility**  
   - **Documentation**

2. **Installation and Deployment**  
   - **Installation**  
   - **Where to Find Samples?**  
   - **Deployment Requirements**

3. **Getting Started**  
   - **Creating Platform Application**  
   - **Deploying Essential Grouping**  
     - **Windows / WPF**  
     - **ASP.NET**  

4. **Concepts and Features**  
   - **Data Binding**  
     - **Creating an ArrayList of Objects**  
     - **Setting a Datasource In the Grouping Engine**  
     - **Iterating Through the Data**  
   - **Using Grouping**  
     - **Grouping a Table**  
       - **The Grouping.TableDescriptor Class**  
       - **Accessing a Particular Group**  
       - **Adding a Summary**  
       - **Retrieving Summary Values for a Particular Group**  
   - **Data Manipulation**  
     - **Filters**  
     - **Expressions**  
     - **Sorting**  
     - **Custom Sorting**  
   - **Algebra Supported In Expressions / Filters**

## Page-level Navigation/TOC
- **Overview**  
  - Introduction to Essential Grouping (Page 4)
  - Prerequisites and Compatibility (Page 6)
  - Documentation (Page 7)

- **Installation and Deployment**  
  - Installation (Page 9)
  - Where to Find Samples? (Page 9)
  - Deployment Requirements (Page 15)

- **Getting Started**  
  - Creating Platform Application (Page 16)
  - Deploying Essential Grouping
    - Windows / WPF (Page 19)
    - ASP.NET (Page 20)

- **Concepts and Features**  
  - Data Binding
    - Creating an ArrayList of Objects (Page 22)
    - Setting a Datasource In the Grouping Engine (Page 27)
    - Iterating Through the Data (Page 28)
  - Using Grouping
    - Grouping a Table
      - The Grouping.TableDescriptor Class (Page 32)
      - Accessing a Particular Group (Page 33)
      - Adding a Summary (Page 37)
      - Retrieving Summary Values for a Particular Group (Page 38)
  - Data Manipulation
    - Filters (Page 40)
    - Expressions (Page 45)
    - Sorting (Page 48)
    - Custom Sorting (Page 51)
    - Algebra Supported In Expressions / Filters (Page 56)

<!-- tags: [Syncfusion Winforms, Essential Grouping, installation, deployment, getting started, concepts, data binding, grouping, data manipulation, filters, expressions, sorting, version 11.4.0.26] keywords: [introduction, prerequisites, compatibility, documentation, platform application, ASP.NET, WPF, data binding, table grouping, summary, sorting] -->
```

---

<!-- 페이지 20 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_006.jpeg
document_name: grouping
page_number: 006
page_id: grouping#page_006
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:12Z
fidelity: lossless
-->

# Essential Grouping

- Grouping is a recursive process whereby a data source may be grouped several times. This leads to the recursive situation of groups having sub-groups and so on.

## User Guide Organization

The product comes with numerous samples as well as an extensive documentation to guide you. This User Guide provides detailed information on the features and functionalities of Essential Grouping. It is organized into the following sections:

- **Overview** - This section gives a brief introduction to our product and its key features.
- **Installation and Deployment** - This section elaborates on the install location of the samples, license, etc.
- **Getting Started** - This section guides you on getting started with various platform applications, controls, etc.
- **Concepts and Features** - The features of Essential Grouping are illustrated with use case scenarios, code examples, and screen shots under this section.
- **Frequently Asked Questions** - This section illustrates the solutions for various task-based queries about Grouping.

## Document Conventions

The conventions listed below will help you to quickly identify the important sections of information while using the content:

### Table 1: Document Conventions

| Convention           | Icon                            | Description                                                                           |
|----------------------|----------------------------------|---------------------------------------------------------------------------------------|
| Note                 | ![Image]({Note})                | Represents important information                                                      |
| Example              | Example                         | Represents an example                                                                |
| Tip                  | ![Image]({Lightbulb})           | Represents useful hints that will help you in using the controls/features           |
| Additional Information | ![Image]({Info})               | Represents additional information on the topic                                        |

## 1.2 Prerequisites and Compatibility

This section covers the requirements mandatory for using Essential Grouping. It also lists operating systems and browsers compatible with the product.

<!-- tags: [grouping, user guide, syncfusion, winforms] keywords: [recursive process, data grouping, documentation, prerequisites, compatibility, syncfusion, version 11.4.0.26] -->
```

---

<!-- 페이지 21 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_010.jpeg
document_name: grouping
page_number: 010
page_id: grouping#page_010
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:25Z
fidelity: lossless
-->

# Essential Grouping

## Content

### Dashboard Access

1. **Click** `Start → All Programs → Syncfusion → Essential Studio <version number> → Dashboard`.

   The UI Edition samples are displayed by default.

#### Figure 2: Syncfusion Essential Studio Dashboard

![Syncfusion Essential Studio Dashboard](https://example.com/syncfusion-dashboard.png)
*Figure 2: Syncfusion Essential Studio Dashboard*

### Select Reporting Edition

2. **Select** the "Reporting" Edition.

#### Figure 3: Syncfusion Reporting Edition Dashboard

![Syncfusion Reporting Edition Dashboard](https://example.com/reporting-dashboard.png)
*Figure 3: Syncfusion Reporting Edition Dashboard*

## Overview

- **User Interface Edition for ASP.NET MVC**: Ideal for creating high-performance AJAX Web applications with ease, now supporting the MVC 3 Razor engine.

- **Reporting Edition for ASP.NET**: Integrates Reporting solutions into ASP.NET applications with ease, including high-performance libraries for manipulating Word, PDF, and Excel.

## API Reference

- **Business Intelligence**: Enhance the Business Intelligence features in your applications.

- **Add-ons**: Access additional tools and libraries to enhance functionality.

- **Utilities**: Utilize utility modules for various tasks.

- **License Management**: Manage licenses for Syncfusion components.

## Code Examples

### C# Example for UI Edition

```csharp
using Syncfusion.UI.Xaml.Grid;
// Example usage of UI Edition features
GridControl grid = new GridControl();
grid.DataSource = new List<Employee>();
```

### C# Example for Reporting Edition

```csharp
using Syncfusion.Pdf;
// Example usage of Reporting Edition features
PdfDocument document = new PdfDocument();
PdfPage page = document.Pages.Add();
```

## See also

- [Syncfusion Documentation Homepage](https://www.syncfusion.com/documentation)
- [Syncfusion Support](https://www.syncfusion.com/support)

## Notes

- **Sales**: Contact support for any sales inquiries.

- **Copyright Information**: Copyright 2001-2022 Syncfusion Inc.

## Page-level Navigation/TOC

- **Dashboard Access**
- **Select Reporting Edition**
- **Overview**
- **API Reference**
- **Code Examples**
- **See also**
- **Notes**

<!-- tags: [syncfusion, winforms, essential studio, dashboard, reporting, user interface, business intelligence, license management] keywords: [syncfusion dashboard, essential studio dashboard, reporting edition, user interface edition, ajax, razor engine, pdf, excel, utilities, license management] -->
```

---

<!-- 페이지 22 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_014.jpeg
document_name: grouping
page_number: 014
page_id: grouping#page_014
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:39Z
fidelity: lossless
--> 

# Essential Grouping

## Overview
- Essential Grouping is a high-performance grouping engine that can group any list of data.
- It handles large amounts of dynamic data and is highly optimized.
- All aspects of the grouping engine are extensible and can support user-defined functionality.

## Content

### Grouping Details

- **Grouping**: Essential Grouping allows users to group data, access filtered results, and summarize information without the overhead of graphical display code.
- **Data Extraction and Manipulation**: The Grouping Engine extracts all necessary data, manipulates it as needed, and provides users with various ways to access the processed results.

### Navigation and Features

#### Sidebar Menu
- **Grouping**
  - Getting Started

#### Featured Samples
- **Examples**: Provided for various functionalities such as filtering, reporting, and user interface management.

#### Additional Links
- **User Interface Edition**, **Reporting Edition**, and **Business Intelligence Edition** are available for users to explore.

#### Sample Browser
- **ASP.NET Sample Browser**: Displays grouping examples for users to explore features.

### Source Code Location

#### Windows Forms Source Code
- **Default Location**: 
  ```
  [System Drive]:\Program Files\Syncfusion\Essential Studio\[Version Number]\Windows\Grouping.Windows\Src
  ```

#### ASP.NET Source Code
- **Default Location**: 
  ```
  [System Drive]:\Program Files\Syncfusion\Essential Studio\[Version Number]\Web\Grouping.Web\Src
  ```

### Instructions for Exploration
1. **Access Samples**: Navigate to the ASP.NET Sample Browser.
2. **Select a Sample**: Choose a sample to view detailed features.
3. **Explore Features**: Browse through the features available in the selected sample.

## Footer Information
- **Copyright**: © 2001-2012 Syncfusion Inc.
- **Links**: Forums, Documentation, Support, Sales

### Page Metadata
- **Copyright Notice**: © 2013 Syncfusion. All rights reserved.
- **Page Number**: 14

<!-- tags: [essential grouping, windows forms, asp.net, sample browser, source code location] keywords: [grouping engine, data manipulation, user interface edition, reporting edition, business intelligence edition, sample samples, source code, windows forms, asp.net, navigation, documentation, support, sales] -->
```

---

<!-- 페이지 23 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_018.jpeg
document_name: grouping
page_number: 018
page_id: grouping#page_018
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:54Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Deploying Essential Grouping into ASP.NET application.
- Creating a WPF Application.

## Content

### Creating a WPF Application
1. Open Microsoft Visual Studio.
2. Go to the File menu and click **New Project**.
3. In the **New Project** dialog, select the **WPF Application** template, name the project, and click **OK**.

#### Figure 10: WPF Application
![](attachment:New_Project_Window.png)

A WPF application is created.

#### Now you need to deploy Essential Grouping into this WPF application. Refer Windows / WPF topic for detailed info.

### For More Information Refer:
- [Deploying Essential Grouping](Deploying_Essential_Grouping)

### 3.2 Deploying Essential Grouping

## API Reference
### [unclear]  
- Not applicable for this page.

## Code Examples
Not applicable for this page.

## Cross References
See also:
- Deploying Essential Grouping

### Optional Page-level Navigation/TOC
Not applicable for this page.

<!-- tags: [Essential Grouping, WPF Application, ASP.NET, Deployment, WinForms] keywords: [deploy, grouping, WPF, ASP.NET, Windows, Visual Studio, application, template, project, Essential Grouping] -->
```

---

<!-- 페이지 24 -->

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

---

<!-- 페이지 25 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_026.jpeg
document_name: grouping
page_number: 026
page_id: grouping#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:17Z
fidelity: lossless
-->

# Essential Grouping

```vb
End Get
Set(ByVal Value As String)
    dValue = Value
End Set
End Property
Public Overrides Function ToString() As String
    Return A + ControlChars.Tab + B + ControlChars.Tab + C + ControlChars.Tab + D
End Function

' MyClass
End Class
```

```vb
End Module
```

## Content

3. Add the code to the Main function as follows. This creates a random list of 'MyObject' and echoes this list to the console.

### C#

```csharp
[STAThread]
static void Main(string[] args)
{
    // Create an arraylist of random MyObjects.
    ArrayList list = new ArrayList();
    Random r = new Random();

    for(int i = 0; i < 10; i++)
    {
        list.Add(new MyObject(r.Next(5)));
        Console.WriteLine(list[i]);
    }

    // Pause
    Console.ReadLine();
}
```

### VB.NET

```vb
Sub Main()

    ' Create an arraylist of random MyObjects.
    Dim list As New ArrayList()
    Dim r As New Random()
End Sub
```

---


<!-- tags: [syncfusion, winforms, grouping] keywords: [Essential Grouping, MyClass, ToString, ArrayList, Random, Main function, C#, VB.NET] -->
``` 


---

<!-- 페이지 26 -->

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

---

<!-- 페이지 27 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_034.jpeg
document_name: grouping
page_number: 034
page_id: grouping#page_034
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:38Z
fidelity: lossless
-->

### Essential Grouping

```csharp
{
    Console.WriteLine(obj);
}
Console.WriteLine("--");
else if (g.Groups != null && g.Groups.Count > 0)
{
    // Iterating through the groups.
    foreach (Group g1 in g.Groups)
    {
        // Recursive call
        ShowRecordsUnderGroup(g1);
    }
}
```

```
Public Sub ShowRecordsUnderGroup(ByVal g As Group)
    If Not (g.Records Is Nothing) And g.Records.Count > 0 Then
        Dim rec As Record
        
        ' Displaying the data for all the records in each group.
        For Each rec In g.Records
            Dim obj As MyObject = CType(rec.GetData(), MyObject)
            If Not (obj Is Nothing) Then
                Console.WriteLine(obj)
            End If
        Next rec
        Console.WriteLine("--")
    Else
        If Not (g.Groups Is Nothing) And g.Groups.Count > 0 Then
            Dim g1 As Group
            
            ' Iterating through the groups.
            For Each g1 In g.Groups
            
                ' Recursive call
                ShowRecordsUnderGroup(g1)
            Next g1
        End If
    End If
    ' ShowRecordsUnderGroup
End Sub
```

## API Reference

### Methods
- **ShowRecordsUnderGroup**  
  - **Parameters:**
    - `g` (`Group`): The group to display records for.
  - **Description:**
    - Recursively displays all records under a group and iterates through subgroups if present.

## Code Examples

### C#
```csharp
void ShowRecordsUnderGroup(Group g)
{
    if (g.Records != null && g.Records.Count > 0)
    {
        foreach (Record rec in g.Records)
        {
            MyObject obj = (MyObject)rec.GetData();
            if (obj != null)
            {
                Console.WriteLine(obj);
            }
        }
        Console.WriteLine("--");
    }
    else if (g.Groups != null && g.Groups.Count > 0)
    {
        foreach (Group g1 in g.Groups)
        {
            ShowRecordsUnderGroup(g1);
        }
    }
}
```

### VB.NET
```vb
Private Sub ShowRecordsUnderGroup(ByVal g As Group)
    If Not (g.Records Is Nothing) And g.Records.Count > 0 Then
        Dim rec As Record
        
        For Each rec In g.Records
            Dim obj As MyObject = CType(rec.GetData(), MyObject)
            If Not (obj Is Nothing) Then
                Console.WriteLine(obj)
            End If
        Next rec
        Console.WriteLine("--")
    Else
        If Not (g.Groups Is Nothing) And g.Groups.Count > 0 Then
            Dim g1 As Group
            
            For Each g1 In g.Groups
                ShowRecordsUnderGroup(g1)
            Next g1
        End If
    End If
End Sub
```

## Cross References
- [See also: Hierarchical Data Display]
- [See also: Grouping Techniques]

<!-- tags: [essential grouping, records, recursive, iteration, grouping techniques] keywords: [group, records, iteration, recursion, hierarchical data display, grouping methods] -->
```

---

<!-- 페이지 28 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_038.jpeg
document_name: grouping
page_number: 038
page_id: grouping#page_038
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:56Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Retrieves Summary Values for a particular group.
- Maintains summary items by group basis in the GroupingEngine.
- Demonstrates obtaining summary values for specified groups using the GetSummary method.

## Content

### Getting Summary Values for a Particular Group

**4.2.4 Retrieving Summary Values for a Particular Group**

After adding the `SummaryDescriptor`, the `GroupingEngine` will maintain these summary items in a group by group basis. You can access these summary values for any group. Here we will get the values for the `TopLevelGroup` and for our `c1` group to illustrate how this is done.

To obtain a particular group's summary values, you need to get the group and access the summary through its `GetSummary` method. Once you have the summary, you can cast it to its `Int32AggregateSummary` type.

The following code snippet illustrates this.

#### Code Example in C#

```csharp
[C#]

// To simplify notation, add this statement at the top of the file.
using ISummary = Syncfusion.Collections.BinaryTree.ITreeTableSummary;

// At the bottom of the Main method, add these lines.

// Now go through the group to get the Summary value for the group.
ISummary groupSummary =
groupingEngine.Table.TopLevelGroup.GetSummary("BInt32Agg");
Int32AggregateSummary int32Summary = (Int32AggregateSummary) groupSummary;

Console.WriteLine("whole table {0}, {1}, {2}", int32Summary.Sum, int32Summary.Average, int32Summary.Maximum);

// Value for "cl" group.
groupSummary =
groupingEngine.Table.TopLevelGroup.Groups["c1"].GetSummary("BInt32Agg");
int32Summary = (Int32AggregateSummary) groupSummary;

Console.WriteLine("c1-group {0}, {1}, {2}", int32Summary.Sum, int32Summary.Average,int32Summary. Maximum);

// Pause
Console.ReadLine();
```

#### Code Example in VB.NET

```vb.net
[VB.NET]

' At the bottom of the Main method, add these lines.

' Now go through the group to get the Summary value for the group.
```

## Page-Level Navigation/TOC (if applicable)
- 4.2.4 Retrieving Summary Values for a Particular Group

## Cross References
- See also: Section 4.2 for more details on using `SummaryDescriptor`.
- For additional functionality, refer to the `GroupingEngine` documentation.

<!-- tags: [Syncfusion Winforms, Grouping, SummaryValues, Retrieval, TopLevelGroup, SummaryDescriptor, GroupingEngine, Int32AggregateSummary] keywords: [GroupingEngine, SummaryDescriptor, Int32AggregateSummary, GetSummary, TopLevelGroup, c1 group] -->
```

---

<!-- 페이지 29 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_042.jpeg
document_name: grouping
page_number: 042
page_id: grouping#page_042
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:15Z
fidelity: lossless
-->

## Essential Grouping

### Content
#### Filtering Records

```csharp
foreach (Record rec in groupingEngine.Table.FilteredRecords)
{
    MyObject obj = rec.GetData() as MyObject;
    if (obj != null)
    {
        Console.WriteLine(obj);
    }
}

// Pause
Console.ReadLine();

// Filter on [D] = d1
RecordFilterDescriptor rfd = new RecordFilterDescriptor("[D] LIKE 'd1'");
groupingEngine.TableDescriptor.RecordFilters.Add(rfd);

// Display the data after filtering.
foreach (Record rec in groupingEngine.Table.FilteredRecords)
{
    MyObject obj = rec.GetData() as MyObject;
    if (obj != null)
    {
        Console.WriteLine(obj);
    }
}

// Pause
Console.ReadLine();
```

#### [VB.NET]

```vb
' Display the data before filtering.
Dim rec As Record
    For Each rec In groupingEngine.Table.FilteredRecords
Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
        Console.WriteLine(obj)
    End If
Next rec

' Pause
Console.ReadLine()

' Filter on [D] = d1
Dim rfd As New RecordFilterDescriptor("[D] LIKE 'd1'")
```

### API Reference

- **RecordFilterDescriptor**: Represents a descriptor for filtering records based on specific criteria.
  - **Constructor**: `RecordFilterDescriptor(string filterExpression)`
    - **filterExpression**: A string that defines the filtering criteria. (e.g., "[D] LIKE 'd1'").
  
### Code Examples

The provided code demonstrates how to:
1. Loop through filtered records and display relevant data.
2. Apply a filter condition to a table.
3. Display the filtered data.

### Cross References

See also:
- [Filtering Data in WinForms Grid](#filtering-data-in-winforms-grid)

## RAG Annotations
<!-- tags: Essential Grouping, filtering, WinForms, Grid, RecordFilterDescriptor keywords: Essential Grouping, filtering, WinForms, Grid, RecordFilterDescriptor -->
```

---

<!-- 페이지 30 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_046.jpeg
document_name: grouping
page_number: 046
page_id: grouping#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:28Z
fidelity: lossless
-->

# Essential Grouping

```csharp
Random r = new Random();

for (int i = 0; i < 10; i++)
{
    list.Add(new MyObject(r.Next(5)));
}

// Create a Grouping.Engine object.
Engine groupingEngine = new Engine();

// Set its datasource.
groupingEngine.SetSourceList(list);
```

## VB.NET

```vb
' Create an arraylist of random MyObjects.
Dim list As New ArrayList()
Dim r As New Random()

Dim i As Integer
For i = 0 To 10
    list.Add(New MyObject(r.Next(5)))
Next

' Create a Grouping.Engine object.
Dim groupingEngine As New Engine()

' Set its datasource.
groupingEngine.SetSourceList(list)
```

14. Now you must add code to list the data, add an expression property, and then display the value of the expression. To retrieve the value, you must use the `Record.GetValue` method by passing it as the name of the expression that you had assigned when it was created.

## Code Examples

### Displaying the Data Before Filtering

```csharp
// Display the data before filtering.
foreach (Record rec in groupingEngine.Table.FilteredRecords)
{
    MyObject obj = rec.GetData() as MyObject;
    if (obj != null)
    {
        Console.WriteLine(obj);
    }
}
```

## API Reference

### Methods

- `GetValue(expressionName)`
  - **Parameters**:
    - `expressionName`: Type (string) - The name of the expression to retrieve the value for.
  - **Returns**: Type (Object) - The value of the specified expression.

## Cross References

See also:
- [Expression Evaluation](#expression-evaluation)
- [Grouping Engine Setup](#grouping-engine-setup)

<!-- tags: [Syncfusion Winforms, Grouping, Data Visualization] keywords: [grouping, essential grouping, data visualization, filtering, expression evaluation, Record.GetValue] -->
```

---

<!-- 페이지 31 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: grouping
page_number: 050
page_id: grouping#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:41Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Demonstrates how to configure and use the Grouping Engine to perform essential grouping operations in a dataset.

## Content

### Setting the Data Source
The following code snippet initializes a Grouping Engine and sets its data source using the `SetSourceList` method. It then iterates through the records of the Table, printing each object to the console.

```vb
' Set its datasource.
    groupingEngine.SetSourceList(list)

    ' Display the data before sorting.
    Dim rec As Record
    For Each rec In groupingEngine.Table.Records
        Dim obj As MyObject = CType(rec.GetData(), MyObject)
        If Not (obj Is Nothing) Then
            Console.WriteLine(obj)
        End If
    Next rec

    ' Pause
    Console.ReadLine()
```

### Sorting a Column
The next part of the snippet sorts the data based on Column "A" using the `SortedColumns.Add` method. After sorting, it displays the filtered records in the sorted order.

```vb
' Sort column A.
    groupingEngine.TableDescriptor.SortedColumns.Add("A")

    ' Display the data after sorting.
    For Each rec In groupingEngine.Table.FilteredRecords
        Dim obj As MyObject = CType(rec.GetData(), MyObject)
        If Not (obj Is Nothing) Then
            Console.WriteLine(obj)
        End If
    Next rec

    ' Pause
    Console.ReadLine()
```

This example illustrates the process of setting up a data source, performing sorting, and displaying the dataset at both before and after sorting stages.

## API Reference
- **GroupingEngine**: The main class that manages grouping operations.
  - **SetSourceList**: Method to set the data source for the Grouping Engine.
    - **Parameters**:
      - `list`: Collection of objects to set as the data source.
  - **TableDescriptor**: Property to access the TableDescriptor object.
    - **SortedColumns**: Collection property to add sorted columns.
      - **Add**: Method to add a column name to the sorted columns list.

## Code Examples

The provided snippet demonstrates the complete setup and usage of the Grouping Engine, including setting the data source, sorting, and displaying the data.

<!-- tags: [syncfusion, winforms, grouping, datahandling, tabledescriptor, group, sort] keywords: [groupingengine, sortedcolumns, filtering, records, display, sort, pause, console, data, source, table, descriptor, add] -->
```

---

<!-- 페이지 32 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_054.jpeg
document_name: grouping
page_number: 054
page_id: grouping#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:56Z
fidelity: lossless
-->

## Essential Grouping

### Overview
- This page demonstrates the use of `Grouping.Engine` in Syncfusion Winforms for handling data grouping and custom sorting.
- The example showcases how to create an `ArrayList` of `MyObject` instances and use the `Grouping.Engine` to display and sort the data.

### Content

The following code example illustrates how to create an `ArrayList` of random `MyObject` instances, set up the `Grouping.Engine`, display the data before sorting, and implement a custom sort for a specific column.

```csharp
// Create an arraylist of random MyObjects.
ArrayList list = new ArrayList();
Random r = new Random();

for(int i = 0; i < 10; i++)
{
    list.Add(new MyObject(r.Next(20)));
}

// Create a Grouping.Engine object.
Engine groupingEngine = new Engine();

// Set its datasource.
groupingEngine.SetSourceList(list);

// Display the data before sorting.
foreach(Record rec in groupingEngine.Table.Records)
{
    MyObject obj = rec.GetData() as MyObject;
    if(obj != null)
    {
        Console.WriteLine(obj);
    }
}

// Pause
Console.ReadLine();

// Custom sort column A.
// Get an IComparer object to handle the custom sorting.
AComparer comparer = new AComparer();
groupingEngine.TableDescriptor.SortedColumns.Add("A");
groupingEngine.TableDescriptor.SortedColumns["A"].Comparer = comparer;

// Display the data before sorting.
foreach(Record rec in groupingEngine.Table.FilteredRecords)
{
    MyObject obj = rec.GetData() as MyObject;
    if(obj != null)
    {
        Console.WriteLine(obj);
    }
}
```

#### Explanation
- **Creating Random Data**: The code starts by creating an `ArrayList` filled with instances of `MyObject`, using a `Random` object to assign values.
- **Initializing Grouping Engine**: A new instance of `Grouping.Engine` is created, and its data source is set to the `ArrayList`.
- **Displaying Data Before Sorting**: The `foreach` loop iterates through the `Records` collection, displaying the data before any sorting is applied.
- **Custom Sorting**: An `IComparer` object is created to handle custom sorting for column "A". This is applied to the `TableDescriptor.SortedColumns`.
- **Displaying Sorted Data**: After applying the custom sorting, the data is displayed again to show the sorted order.

## API Reference

### Namespaces and Types
- **System.Collections.ArrayList**
  - Represents a variable-size list that can grow and shrink dynamically.
- **System.Random**
  - Generates a sequence of random numbers.
- **Syncfusion.Grouping.Engine**
  - The class responsible for handling the grouping functionality.
- **Syncfusion.Grouping.Record**
  - Represents a single record in the grouping engine.
- **Syncfusion.Grouping.TableDescriptor**
  - Provides information about the columns and their sorting options.

### Methods and Properties
- **SetSourceList**
  - Sets the data source for the grouping engine.
- **Table.Records**
  - Accesses the collection of records in the table.
- **TableDescriptor.SortedColumns**
  - Allows specifying and configuring sorted columns in the table.

### Parameters
- **ArrayList**
  - The `ArrayList` object containing the dataset.
- **IComparer**
  - The custom comparer object used for sorting.

## Code Examples

The code example provided demonstrates:
1. Creating and populating an `ArrayList` with `MyObject` instances.
2. Setting up the `Grouping.Engine` with the populated `ArrayList`.
3. Displaying the data before and after custom sorting of column "A".

## Cross References
- Refer to the `MyObject` class documentation for more details on the object type used in this example.
- For more information on `IComparer` and custom sorting, refer to the appropriate documentation.

<!-- tags: [syncfusion winforms, grouping, group engine, sorting, custom comparer] keywords: [ArrayList, Random, Grouping.Engine, TableDescriptor, IComparer, sorting, filtering, records] -->
```

---

<!-- 페이지 33 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_058.jpeg
document_name: grouping
page_number: 058
page_id: grouping#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:19Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Between: Checks if a date field value between the two values is listed in the right-hand operand.

## Content

### Between
Checks if a date field value between the two values is listed in the right-hand operand.

#### Example
[Date] between {2/25/2004, 3/2/2004} returns 1 for any record whose date field is greater than or equal to 2/25/2004 and less than 3/2/2004. To represent the current date, use the token TODAY. To represent DateTime.MinValue, leave the first argument empty. To represent DateTime.MaxValue, leave the second argument empty.

### Custom Functions
Essential Grouping lets you add custom functions to your code that can then be used in expressions.

#### Limitations on the Use of Custom Functions
- You cannot use custom functions in algebraic expressions.
- They must be used stand-alone in a simple expression that consists of only the function name and its argument list.
- The argument list can be any number of arguments separated by a delimiter.

## Code Examples

```csharp
// Example usage of custom functions
string result = CustomFunction("Argument1", "Argument2");
```

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, Essential Grouping, Custom Functions, Between] keywords: [custom functions, algebraic expressions, date fields, DateTime.MinValue, DateTime.MaxValue, TODAY, stand-alone expressions, argument lists, operators] -->
``` 


---

<!-- 페이지 34 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_062.jpeg
document_name: grouping
page_number: 062
page_id: grouping#page_062
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:31Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- ComputeFunc:
  - Explains how to compute functions for grouping.
- Expression Fields:
  - Details the process of adding expression fields to data records.

## Content

### 5.3 How to Add Expression Fields?

To add an expression field to the data in the Grouping Engine, you must first create an instance of an `ExpressionFieldDescriptor` and add it to the `ExpressionFields` collection in the `TableDescriptor`. The `ExpressionFieldDescriptor` will allow you to specify a string that holds an algebraic expression using any of the other fields that are in the record.

The following code snippet illustrates this.

#### [C#]

```csharp
// Add an expression property that multiplies field B by 2.1 and adds 3.2
ExpressionFieldDescriptor efd = new ExpressionFieldDescriptor("MultipleOfB", "2.1 * [B] + 3.2");
this.groupingEngine.TableDescriptor.ExpressionFields.Add(efd);

// Assumes the datasource to be an IList, holding objects of type MyClass.
MyClass o = this.groupingEngine.Table.Records[2].GetData() as MyClass;

// MultipleOfB is an expression field name and B is a property in MyClass.
object someValue = this.groupingEngine.Table.Records[2].GetValue("B");
object someExpressionValue =
this.groupingEngine.Table.Records[2].GetValue("MultipleOfB");
```

#### [VB.NET]

```vb
' Add an expression property that multiplies field B by 2.1 and adds 3.2
Dim efd As New ExpressionFieldDescriptor("MultipleOfB", "2.1 * [B] + 3.2")
Me.groupingEngine.TableDescriptor.ExpressionFields.Add(efd)

' Assumes the datasource to be an IList, holding objects of type MyClass.
Dim o As MyClass = CType(Me.groupingEngine.Table.Records(2).GetData(), MyClass)

' MultipleOfB is an expression field name and B is a Property in MyClass.
Dim someValue As Object = Me.groupingEngine.Table.Records(2).GetValue("B")
Dim someExpressionValue As Object =
Me.groupingEngine.Table.Records(2).GetValue("MultipleOfB")
```

## API Reference

The `ExpressionFieldDescriptor` class is used to define a descriptor for an expression field. It allows specifying an algebraic expression that can be evaluated over the fields in the records.

- **Constructor**: 
  - `ExpressionFieldDescriptor(string name, string expression)`: Creates a new instance of the `ExpressionFieldDescriptor` with the specified name and expression.

## Code Examples

The provided code examples demonstrate how to:
- Create an `ExpressionFieldDescriptor` object.
- Add it to the `TableDescriptor`'s `ExpressionFields` collection.
- Retrieve the values of both regular fields and expression fields.

## Page-level Navigation/TOC
- [5.3 How to Add Expression Fields?]

## Cross References
See also:
- Grouping Engine
- TableDescriptor
- ExpressionFieldDescriptor

<!-- tags: [Essential Grouping, Expression Fields, Grouping Engine, TableDescriptor, ExpressionFieldDescriptor] keywords: [ExpressionFieldDescriptor, algebraic expression, ExpressionFields, TableDescriptor, Grouping Engine, MyClass, records, GetValue] -->
```


---

<!-- 페이지 35 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_066.jpeg
document_name: grouping
page_number: 066
page_id: grouping#page_066
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:49Z
fidelity: lossless
-->

# Essential Grouping

**Note:** To remove a particular grouping, use `groupingEngine.TableDescriptor.GroupedColumns.Remove` or `groupingEngine.TableDescriptor.SortedColumns.RemoveAt`.

## How to Clear a Sort?

To clear all sorts, call the `groupingEngine.TableDescriptor.SortedColumns.Clear` method.

**C#**

```csharp
// Removes all the sorting associated with the table.
this.gridGroupingControl.TableDescriptor.SortedColumns.Clear();

// Removes the sorting of the column mentioned as argument.
this.gridGroupingControl.TableDescriptor.SortedColumns.Remove(Name of the column);

// Removes the sorting of the column mentioned as column index.
this.gridGroupingControl.TableDescriptor.SortedColumns.RemoveAt(index);
```

**VB.NET**

```vb
' Removes all the sorting associated.
Me.gridGroupingControl1.TableDescriptor.SortedColumns.Clear()

' Removes the sorting of the column mentioned as argument.
Me.gridGroupingControl1.TableDescriptor.SortedColumns.Remove()

' Removes the sorting of the column mentioned as column index.
Me.gridGroupingControl1.TableDescriptor.SortedColumns.RemoveAt()
```

**Note:** To remove a particular sort, use `groupingEngine.TableDescriptor.SortedColumns.Remove` or `groupingEngine.TableDescriptor.SortedColumns.RemoveAt`.

## How to Filter a Collection?

To add a filter condition, add a `RecordFilterDescriptor` to the `Engine.TableDescriptor.RecordFilters` collection. The constructor on the `RecordFilterDescription` takes an expression, `[D] LIKE 'd1'`. This expression will be `True` only for those items in the list where the string property `D` has the value `d1`. Here are some other valid expressions where `B` is an integer property:

- `[D] LIKE 'd1'`
- `[B] > 30`

<!-- tags: [Syncfusion, Winforms, grouping, filter, sort, control, api, TableDescriptor] keywords: [filter condition, RecordFilterDescriptor, RecordFilters, groupingEngine, sortedColumns, groupedColumns] -->
```

---

<!-- 페이지 36 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_070.jpeg
document_name: grouping
page_number: 070
page_id: grouping#page_070
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:02:02Z
fidelity: lossless
-->

## Index

### A
- Accessing a Particular Group 33
- Adding a Summary 37
- Algebra Supported In Expressions / Filters 56
- ASP.NET 20
- Concepts and Features 22
- Creating an ArrayList of Objects 22
- Creating Platform Application 16
- Custom Sorting 51

### D
- Data Binding 22
- Data Manipulation 39
- Deploying Essential Grouping 18
- Deployment Requirements 15
- Documentation 7

### E
- Expressions 45

### F
- Filters 40
- Frequently Asked Questions 59

### G
- Getting Started 16
- Grouping a Table 30

### H
- How to Access the Value of a Record Or Field? 59
- How to Add Custom Calculations to Expression Fields? 60
- How to Add Expression Fields? 62
- How to Add Summary Items? 63
- How to Bind a Datasource to the Grouping Engine? 63

### I
- Installation 9
- Installation and Deployment 9
- Introduction to Essential Grouping 4
- Iterating Through the Data 28

### O
- Overview 4

### P
- Prerequisites and Compatibility 6

### R
- Retrieving Summary Values for a Particular Group 38

### S
- Setting a Datasource In the Grouping Engine 27
- Sorting 48

### T
- The Grouping.TableDescriptor Class 32

### U
- Using Grouping 30

### W
- Where to Find Samples? 9
- Windows / WPF 19

### Global Content
- How to Clear a Filter? 64
- How to Clear a Grouping? 65
- How to Clear a Sort? 66
- How to Filter a Collection? 66
- How to Group a Collection? 67
- How to Retrieve Summary Item Values? 67
- How to Sort a Collection? 69
```

---

<!-- 페이지 37 -->

```markdown
<!--  
source: image  
domain: syncfusion-sdk  
task: pdf-ocr-to-markdown  
language: en (keep original; do not translate)  
source_filename: page_003.jpeg  
document_name: grouping  
page_number: 003  
page_id: grouping#page_003  
product: Syncfusion Winforms  
version: 11.4.0.26  
timestamp: 2025-08-09T06:57:54Z  
fidelity: lossless  
-->  

## Essential Grouping  

### Overview  
- Quick access to solutions for grouping-related tasks in Syncfusion Winforms.  
- Covers frequently asked questions on accessing values, adding calculations, handling filters, sorts, groupings, and more.  
- Integrates with datasources and provides a systematic guide to handling collections and summaries.  

### Frequently Asked Questions  

#### 5.1 How to Access the Value of a Record Or Field?  
**Page:** 59  

#### 5.2 How to Add Custom Calculations to Expression Fields?  
**Page:** 60  

#### 5.3 How to Add Expression Fields?  
**Page:** 62  

#### 5.4 How to Add Summary Items?  
**Page:** 63  

#### 5.5 How to Bind a Datasource to the Grouping Engine?  
**Page:** 63  

#### 5.6 How to Clear a Filter?  
**Page:** 64  

#### 5.7 How to Clear a Grouping?  
**Page:** 65  

#### 5.8 How to Clear a Sort?  
**Page:** 66  

#### 5.9 How to Filter a Collection?  
**Page:** 66  

#### 5.10 How to Group a Collection?  
**Page:** 67  

#### 5.11 How to Retrieve Summary Item Values?  
**Page:** 67  

#### 5.12 How to Sort a Collection?  
**Page:** 69  

<!-- tags: [syncfusion, winforms, grouping, datasources, calculations, filters, sorts, summaries] keywords: [record, field, expression, summarization, engine, collections, filter, sort, group] -->
```

---

<!-- 페이지 38 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_007.jpeg
document_name: grouping
page_number: 007
page_id: grouping#page_007
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:06Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Prerequisites for development environments and compatibility with various versions of Visual Studio and .NET Framework are specified.
- Compatibility details with multiple Windows operating systems are outlined.
- Documentation guidelines for using Essential Grouping in different platform applications are described.

## Content

### Prerequisites
The prerequisites details are listed below:

**Table 2: Prerequisites**

| Development Environments | .NET Framework Versions |
|---------------------------|-------------------------|
| - Visual Studio 2012 (Ultimate, Premium, Professional, and Express) <br> - Visual Studio 2010 (Ultimate, Premium, Professional, and Express) <br> - Visual Studio 2008 (Team System, Professional, Standard & Express) <br> - Visual Studio 2005 (Professional, Standard & Express) | - .NET 4.5 <br> - .NET 4.0 <br> - .NET 3.5 SP1 <br> - .NET 2.0 |

### Compatibility
The compatibility details are listed below:

**Table 3: Compatibility**

| Operating Systems |
|-------------------|
| - Windows 8 (32 bit and 64 bit) <br> - Windows Server 2012 (32 bit and 64 bit) <br> - Windows Server 2008 (32 bit and 64 bit) <br> - Windows 7 (32 bit and 64 bit) <br> - Windows Vista (32 bit and 64 bit) <br> - Windows XP <br> - Windows 2003 |

### 1.3 Documentation

Syncfusion provides the following documentation segments to provide all necessary information for using Essential Grouping in different platform applications in an efficient manner.

**Table 4: Documentation**

| Type of documentation | Location |
|-----------------------|----------|
|                       |          |

<!-- tags: [syncfusion, winforms, essential grouping, prerequisites, compatibility, documentation] keywords: [development environments, .NET Framework, Windows operating systems, documentation segments, Essential Grouping, Syncfusion Winforms] -->
```

---

<!-- 페이지 39 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_011.jpeg
document_name: grouping
page_number: 011
page_id: grouping#page_011
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:20Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Steps to view Grouping samples in various platforms are explained.
- Focus on Windows Forms for demonstration.

## Content

### Windows
1. **In the Dashboard window**, click **Run Samples for Windows Forms** under the **Reporting Edition panel**. The **Windows Forms Sample Browser window** is displayed.

#### Note:
You can view the samples in any of the following three ways:
- **Run Samples** – Click to view the locally installed samples.
- **Online Samples** – Click to view online samples.
- **Explore Samples** – Explore Windows Forms samples on disk.

#### Figure 3: Syncfusion Essential Studio Dashboard

The steps to view the Grouping samples in various platforms are discussed below.

#### Figure 4: Windows Forms Sample Browser

2. **Click Grouping** from the bottom-left pane. The Grouping samples are displayed.

### WinForms Sample Browser Display
The sample browser window shows various sections, including sections for **Product Showcase**, **Get Started**, **Insert Content**, **Formatting**, **Page Layout**, **References**, **Editing**, **Mail Merge**, **View**, **Security**, and **Import And Export**. Featured samples such as **Sales Invoice**, **Table Insertion**, **Employee Report**, **Table Of Contents**, **Forms**, **Clone and Merge**, and **Update Fields** are visible.

### Navigation Instructions
- To see the **Grouping samples**, navigate through the Windows Forms Sample Browser as described above.

## API Reference
- This section focuses on demonstrating how to access Grouping samples in the Windows Forms environment.

## Code Examples
No explicit code examples are provided in this section. The focus is on user interaction with the Sample Browser.

### Cross References
- **Related Sections**: For more details on Grouping and how it can be implemented programmatically, refer to the API Reference and Code Examples sections in the full documentation.

<!-- tags: [syncfusion, winforms, reporting, dashboard, sample browser, grouping] keywords: [grouping samples, windows forms, reporting edition, sample browser, product showcase, table of contents, sales invoice, employee report] -->
```

---

<!-- 페이지 40 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_015.jpeg
document_name: grouping
page_number: 015
page_id: grouping#page_015
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:33Z
fidelity: lossless
-->

# Essential Grouping

## 2.3 Deployment Requirements

### Dll List

While deploying an application that references Syncfusion Essential Grouping assembly, the following dependencies must be included in the distribution.

#### Windows Forms – Grouping

- Syncfusion.Core.dll
- Syncfusion.Shared.Base.dll
- Syncfusion.Shared.Windows.dll
- Syncfusion.Grouping.Base.dll
- Syncfusion.Grouping.Windows.dll

#### ASP.NET - Grouping

- Syncfusion.Core.dll
- Syncfusion.Shared.Base.dll
- Syncfusion.Shared.Web.dll
- Syncfusion.Grouping.Base.dll
- Syncfusion.Grouping.Windows.dll
- Syncfusion.Grouping.Web.dll

<!-- tags: [Syncfusion Winforms, Essential Grouping, Deployment Requirements, Dll List, Windows Forms, ASP.NET] keywords: [Syncfusion.Core.dll, Syncfusion.Shared.Base.dll, Syncfusion.Shared.Windows.dll, Syncfusion.Grouping.Base.dll, Syncfusion.Grouping.Windows.dll, Syncfusion.Grouping.Web.dll] -->
```

---

<!-- 페이지 41 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_019.jpeg
document_name: grouping
page_number: 019
page_id: grouping#page_019
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:42Z
fidelity: lossless
-->

# Essential Grouping

We have now created a platform application in the previous topic ([Creating Platform Application](Creating_Platform_Application)). This section will guide you to deploy Essential Grouping in those applications under the following topics:

- Windows / WPF-Step-by-step procedure to deploy Grouping in Windows / WPF applications
- ASP.NET-Step-by-step procedure to deploy Grouping in web applications

## 3.2.1 Windows / WPF

Now, you have created a Windows / WPF application ([refer Creating Platform Application](Creating_Platform_Application)). This section will guide you to deploy Essential Grouping in a Windows/WPF applications.

### Deploying Essential Grouping in a Windows / WPF Application

The following steps will guide you to deploy Essential Grouping:

1. In order to deploy an application that uses the Syncfusion assemblies, the referenced Syncfusion assemblies should reside in the application folder where the exe exists, in the target machine.
2. In order to do that, go to the References folder in the Solution Explorer. Select all the Syncfusion assemblies, right-click and go to Properties. Change the Copy Local property of the Syncfusion assemblies to **true** and compile the project.
3. Check whether the licenses.licx file listed in the project has its Build Action property to be **Embedded Resource**.
4. Now you may see that the Syncfusion assemblies referenced in the project are copied to the output directory along with the application executable `(bin/debug/)`.
5. Deploy the exe along with the Syncfusion assemblies in that location to the target machine. Be sure that these Syncfusion assemblies reside in the same location as the application exe in the target machine.

**Note**: For Windows Forms applications, placing these referenced Syncfusion assemblies in the GAC alone, in the target machine, will also work.

### DLLs needed for deployment

- Syncfusion.Core.dll
- Syncfusion.Grouping.Base.dll
- Syncfusion.Grouping.Windows.dll

<!-- tags: [product, module, control, api, version?] keywords: [Essential Grouping, Windows, WPF, ASP.NET, Syncfusion assemblies, Deployment, Solution Explorer, Build Action, Embedded Resource, licenses.licx, DLLs, Syncfusion.Core.dll, Syncfusion.Grouping.Base.dll, Syncfusion.Grouping.Windows.dll, GAC] -->
```

---

<!-- 페이지 42 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_023.jpeg
document_name: grouping
page_number: 023
page_id: grouping#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:56Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Creating a new console project.
- Defining a custom object class and integrating it into the generated code.
- Sample code for the custom object class with properties and constructor.

## Content

### Creating a New Console Project

Figure 11 illustrates the process of creating a new console project in Visual Studio.

```plaintext
Name:          GroupingSample
Location:      C:\A_SyncWork\incident
```

#### Step 1: Create a Custom Object Class
Create a custom object class and add it to the 'Class1' file generated in the first step. Name the class 'MyObject', and define it with the following properties:

- Four string properties named A, B, C, and D.
- A constructor that accepts an integer argument.

**Note:** The B property is designed to hold digits and will be used later for summarizing data.

#### Sample Code for the Custom Object Class

```csharp
using System;

namespace GroupingSample
{
    class Class1
    {
        [STAThread]
        static void Main(string[] args)
        {
        }
    }

    public class MyObject
    {
        // Properties and constructor to be defined here
    }
}
```

### Explanation of the Code
The provided code snippet includes the basic structure for the console application and the starting point for defining the `MyObject` class. The `MyObject` class will include the required properties and a constructor as specified.

## API Reference

### Class `MyObject`
- **Properties**:
  - `A` (string)
  - `B` (string)
  - `C` (string)
  - `D` (string)
- **Constructor**:
  - Accepts an integer argument for initialization.

## Code Examples

### Full Sample Code
```csharp
using System;

namespace GroupingSample
{
    class Class1
    {
        [STAThread]
        static void Main(string[] args)
        {
            // Example usage of MyObject
            MyObject obj = new MyObject(123);
            Console.WriteLine(obj.A);
            Console.WriteLine(obj.B);
            Console.WriteLine(obj.C);
            Console.WriteLine(obj.D);
        }
    }

    public class MyObject
    {
        public string A { get; set; }
        public string B { get; set; }
        public string C { get; set; }
        public string D { get; set; }

        public MyObject(int value)
        {
            A = "InitialA";
            B = value.ToString(); // B holds digits
            C = "InitialC";
            D = "InitialD";
        }
    }
}
```

## Cross References
- Refer to the generated 'Class1' file for further implementation details.
- Ensure the custom object class integrates seamlessly with the existing application logic.

<!-- tags: [Syncfusion, WinForms, data grouping, console application, custom object class] keywords: [GroupingSample, MyObject, Class1, properties, constructor, data summarization, digits] -->
```

---

<!-- 페이지 43 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_027.jpeg
document_name: grouping
page_number: 027
page_id: grouping#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:16Z
fidelity: lossless
-->



### Essential Grouping

```vb
Dim i As Integer

For i = 0 To 10
    list.Add(New MyObject(r.Next(5)))
    Console.WriteLine(list(i))
Next

' Pause
Console.ReadLine()
End Sub
```

The console display showing random `MyObjects` is illustrated below:

![Console Display Showing Random MyObjects](https://i.imgur.com/oOaFZ.jpg)

**Figure 12: Console Display Showing Random MyObjects**

4. An `ArrayList` of Objects is created.

#### 4.1.2 Setting a Datasource In the Grouping Engine

Add the following grouping namespace for referring the assemblies deployed in the application.

**i** Refer Deploying Essential Grouping section to know about deploying Essential Grouping.

```csharp
using Syncfusion.Grouping;
```

**Note:** The namespace `Syncfusion.Grouping` should be included to utilize the Essential Grouping engine in your application.

---
```html
<!-- tags: [syncfusion, essential grouping, datasource, datasources, list, object] keywords: [essential grouping, setting, datasource, deploy, group grouping, syncfusion grouping] -->
```

---

<!-- 페이지 44 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_031.jpeg
document_name: grouping
page_number: 031
page_id: grouping#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:25Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- This section demonstrates how to group data in a `MyObject` class using the `GroupingEngine` in Syncfusion Winforms.
- Focuses on grouping by a specific property, `C`, and sorting the grouped data accordingly.

## Content

**Note:** Here, the columns correspond to the public properties in our sample `MyObject` class, `A`, `B`, `C`, and `D`.

We will now continue using the same sample created in the **previous** section and add the corresponding code at the bottom of the `Main` method.

### Step 1: Grouping the Data

To group the `MyObject` `ArrayList` by a particular property, say property `C`, you have to add only the property name (`"C"`) to the `groupingEngine.TableDescriptor.GroupedColumns` collections. Add the following code snippet to the bottom of the `Main` method.

#### C# Implementation

```csharp
// Group on property C.
groupingEngine.TableDescriptor.GroupedColumns.Add("C");

// Display the records in the engine after grouping.
foreach (Record rec in groupingEngine.Table.Records)
{
    MyObject obj = rec.GetData() as MyObject;
    if (obj != null)
    {
        Console.WriteLine(obj);
    }
}
```

#### VB.NET Implementation

```vb
' Group on property C.
groupingEngine.TableDescriptor.GroupedColumns.Add("C")

' Display the records in the engine after grouping.
For Each rec In groupingEngine.Table.Records
    Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
        Console.WriteLine(obj)
    End If
Next rec
```

### Step 2: Observing the Grouped Data

After running the code from step 1, a screen similar to the one below will be displayed. Note that the bottom list displayed is now sorted by **column C**. This is a one side effect of grouping by column `C`.

## Result

The grouped data is now sorted by the specified column, `C`, and the output reflects this sorting. This ensures that the grouped data is organized and displayed as intended.

## Code Examples

### C# Example
```csharp
using Syncfusion.GroupingEngine;

void Main()
{
    // Setup groupingEngine and MyObject data
    GroupingEngine groupingEngine = new GroupingEngine();

    // Populate MyObject objects in ArrayList

    // Group on property C.
    groupingEngine.TableDescriptor.GroupedColumns.Add("C");

    // Display the results
    foreach (Record rec in groupingEngine.Table.Records)
    {
        MyObject obj = rec.GetData() as MyObject;
        if (obj != null)
        {
            Console.WriteLine(obj);
        }
    }
}
```

### VB.NET Example
```vb
Imports Syncfusion.GroupingEngine

Sub Main()
    ' Setup groupingEngine and MyObject data
    Dim groupingEngine As New GroupingEngine()

    ' Populate MyObject objects in ArrayList

    ' Group on property C.
    groupingEngine.TableDescriptor.GroupedColumns.Add("C")

    ' Display the results
    For Each rec In groupingEngine.Table.Records
        Dim obj As MyObject = CType(rec.GetData(), MyObject)
        If Not (obj Is Nothing) Then
            Console.WriteLine(obj)
        End If
    Next rec
End Sub
```

## API Reference

- **GroupingEngine**: The main class responsible for handling grouping operations.
- **TableDescriptor.GroupedColumns**: Property to specify the columns to group by.
- **Record.GetData()**: Method to retrieve the data object from a record.

## Page-level Navigation/TOC
- [Essential Grouping](#essential-grouping)
  - Overview
  - Content
    - Step 1: Grouping the Data
    - Step 2: Observing the Grouped Data
  - Result
  - Code Examples
    - C# Example
    - VB.NET Example
  - API Reference

## Tags and Keywords

<!-- tags: [syncfusion, winforms, grouping, groupingengine, tabledescriptor, groupedcolumns] keywords: [grouping, property grouping, column sorting, data grouping, engine, table descriptor, grouped columns] -->

---

<!-- 페이지 45 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_035.jpeg
document_name: grouping
page_number: 035
page_id: grouping#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:50Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Demonstrates viewing records associated with a specific category after grouping.
- Utilizes the `ShowRecordsUnderGroup` method to display records under a selected group.

## Content

### Accessing Records Under Specific Groups

Once you have the `ShowRecordsUnderGroup` method, you only need to retrieve a specific group from the `Groups` collection and call the method. After grouping on property `C`, you can view all records whose `Category` is "c1" using the following code, similar to what is shown below the `Main` method.

#### C#

```csharp
// Get the Group associated with the value "c1".
Group g = groupingEngine.Table.TopLevelGroup.Groups["c1"];
ShowRecordsUnderGroup(g);

// Pause
Console.ReadLine();
```

#### VB.NET

```vb
' Get the Group associated with the value "c1".
Dim g As Group = groupingEngine.Table.TopLevelGroup.Groups("c1")
ShowRecordsUnderGroup(g)

' Pause
Console.ReadLine()
```

## API Reference

### Methods

- **ShowRecordsUnderGroup(g)**
  - **Purpose**: Displays records under the specified group `g`.
  - **Parameters**:
    - `g`: The group object to access records from.

### Properties

- **Groups**: Collection of groups within the `TopLevelGroup` to access specific groups by their category value.

## Page-level Navigation/TOC (if applicable)

- **Accessing Records Under Specific Groups**

## Cross References

See also:
- Chapter on Grouping Techniques in the Syncfusion Winforms User Guide.

<!-- tags: [Syncfusion, Winforms, Grouping, Records, ShowRecordsUnderGroup] keywords: [grouping, records, c1, groups, ShowRecordsUnderGroup, TopLevelGroup, categories] -->
```

---

<!-- 페이지 46 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_039.jpeg
document_name: grouping
page_number: 039
page_id: grouping#page_039
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:03Z
fidelity: lossless
-->

# Essential Grouping

```vbnet
Dim groupSummary As Syncfusion.Collections.BinaryTree.ITreeTable = ...
```

```vbnet
Dim int32Summary as Int32AggregateSummary = CType(groupSummary, Int32AggregateSummary)
Console.WriteLine("whole table {0}, {1}, {2}", int32Summary.Sum, int32Summary.Average, int32Summary.Maximum)

' Value for "c1" group.
groupSummary = groupingEngine.Table.TopLevelGroup.Groups("c1").GetSummary("BInt32Agg")
int32Summary = CType(groupSummary, Int32AggregateSummary)

Console.WriteLine("cl-group {0}, {1}, {2}", int32Summary.Sum, int32Summary.Average, int32Summary.Maximum)

' Pause
Console.ReadLine()
```

![Screenshot of the summary statistics displayed for the whole table and Group c1](https://i.imgur.com/image.png)

Figure 16: Summary Statistics Shown for the Whole Table and for Group c1

## 4.3 Data Manipulation

<!-- tags: [essential grouping, data manipulation, summary statistics, whole table, group, syncfusion winforms, version 11.4.0.26] keywords: [essential grouping, data manipulation, summary statistics, whole table, group, syncfusion winforms, version, csharp, vb net, api, code examples, grouping engine, table, top level group, groups, getsummary, cte, int32aggregatesummary, console.writeline, pause, read line, table manipulation, group manipulation, statistics calculation, example, code, summary, aggregate summary, table, group, whole, c1, cl group, average, maximum, sum,停顿,阅读行,整张表, ] -->
```

---

<!-- 페이지 47 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_043.jpeg
document_name: grouping
page_number: 043
page_id: grouping#page_043
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:15Z
fidelity: lossless
-->

# Essential Grouping

groupingEngine.TableDescriptor.RecordFilters.Add(rfd)

```vb
' Display the data after filtering.
For Each rec In groupingEngine.Table.FilteredRecords
    Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
        Console.WriteLine(obj)
    End If
Next rec

' Pause
Console.ReadLine()
```

![Figure 17: Screen Showing the Initial Data Followed by the Same Data Filtered on [D] LIKE 'd1'](/images/grouping#page_043-figure17.png)

13. You can apply more complex filters. Here is the code that will remove any existing filters and filter the property D being d1 or property b equal 2. Note here that since you expect property B to display only numeric data, you must use the = operator in the comparison.

## C#

```csharp
groupingEngine.TableDescriptor.RecordFilters.Clear();
```

## API Reference (if applicable)
Namespace, Class, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required
- Returns: Type + description.
- Exceptions: bullet list.

## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
See also: bullet list of explicit links/texts present on the page. Do not fabricate.

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```

---

<!-- 페이지 48 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_047.jpeg
document_name: grouping
page_number: 047
page_id: grouping#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:28Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- This page describes how to add an expression property to a table descriptor using C# and VB.NET in the context of Syncfusion Winforms.
- Highlights the process of displaying records before and after adding an expression property.
- Demonstrates creating and adding an expression field descriptor to the `ExpressionFields` collection of the table descriptor.

## Content

### Adding an Expression Property

#### Adding before Filtering

In the following code snippets, the process of displaying the data before filtering, adding an expression property, and then displaying the data after adding the field is outlined.

#### C# Code

```csharp
// Pause
Console.ReadLine();

// Add an expression property.
ExpressionFieldDescriptor efd = new ExpressionFieldDescriptor("MultipleOfB", "2.1 * [B] + 3.2");
groupingEngine.TableDescriptor.ExpressionFields.Add(efd);

// Display the data after adding the field.
foreach (Record rec in groupingEngine.Table.FilteredRecords)
{
    Console.WriteLine(rec.GetValue("MultipleOfB"));
}

// Pause
Console.ReadLine();
```

#### VB.NET Code

```vb
' Display the data before filtering.
Dim rec As Record
For Each rec In groupingEngine.Table.FilteredRecords
    Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
        Console.WriteLine(obj)
    End If
Next rec

' Pause
Console.ReadLine()

' Add an expression property.
Dim efd As New ExpressionFieldDescriptor("MultipleOfB", "2.1 * [B] + 3.2")
groupingEngine.TableDescriptor.ExpressionFields.Add(efd)

' Display the data after adding the field.
For Each rec In groupingEngine.Table.FilteredRecords
    Console.WriteLine(rec.GetValue("MultipleOfB"))
Next rec
```

## API Reference

### Methods/Properties Used

- `ExpressionFieldDescriptor`
  - `ExpressionFieldDescriptor(String name, String expression)`
    - Creates a new expression field descriptor with the specified name and expression.
  - `ExpressionFields.Add(ExpressionFieldDescriptor)`
    - Adds an expression field descriptor to the table descriptor.

### Parameters

- `name`: The name of the expression field.
- `expression`: The mathematical expression to evaluate.

### Returns

- No explicit return value for the methods used in the context.

## Cross References

- See also: [Expression Fields in Syncfusion Winforms](#expression-fields-in-syncfusion-winforms)

<!-- tags: [Syncfusion, Winforms, ExpressionFieldDescriptor, TableDescriptor, Grouping, Version: 11.4.0.26] keywords: [ExpressionFieldDescriptor, TableDescriptor, Filtering, Winforms, C#, VB.NET] -->
```

---

<!-- 페이지 49 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_051.jpeg
document_name: grouping
page_number: 051
page_id: grouping#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:44Z
fidelity: lossless
-->

# Essential Grouping

## 4.3.4 Custom Sorting

We used a simplest overload in the previous section for sorting the data. The `TableDescriptor.SortedColumns.Add` method has three overloads as shown below:

- `Add(string propertyName)`
- `Add(string propertyName, ListSortDirection dir)`
- `Add(SortColumnDescriptor sdc)`

The following code snippets illustrate the syntax for these overloads:

```csharp
[C#]

public int Add(string propertyName);
public int Add(string propertyName, ListSortDirection dir);
public int Add(SortColumnDescriptor sdc);
```

## Page-Level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, include it here with links/text as shown.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.

## RAG Annotations
- Add tags and keywords derived ONLY from visible content:
  <!-- tags: [Syncfusion, WinForms, CustomSorting, TableDescriptor, SortedColumns, Add, Overloads] keywords: [Custom Sorting, TableDescriptor, SortedColumns, Add, Overloads, C# Syntax, Property Sorting, ListSortDirection, SortColumnDescriptor] -->


---

<!-- 페이지 50 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_055.jpeg
document_name: grouping
page_number: 055
page_id: grouping#page_055
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:55Z
fidelity: lossless
-->

## Essential Grouping

### Overview

- Demonstrates the process of grouping objects in a `Grouping.Engine`.
- Explains setting up data sources, defining custom sorting, and displaying the grouped data.

### Content

```vb
' Create an arraylist of random MyObjects.
Dim list As New ArrayList()
Dim r As New Random()

Dim i As Integer
For i = 0 To 9
    list.Add(New MyObject(r.Next(20)))
Next i

' Create a Grouping.Engine object.
Dim groupingEngine As New Engine()

' Set its datasource.
groupingEngine.SetSourceList(list)

' Display the data before sorting.
Dim rec As Record
For Each rec In groupingEngine.Table.Records
    Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
        Console.WriteLine(obj)
    End If
Next rec

' Pause
Console.ReadLine()

' Custom sort column A.
' Get an IComparer object to handle the custom sorting.
Dim comparer As New AComparer()
groupingEngine.TableDescriptor.SortedColumns.Add("A")
groupingEngine.TableDescriptor.SortedColumns("A").Comparer = comparer

' Display the data before sorting.
Dim rec As Record
For Each rec In groupingEngine.Table.FilteredRecords
    Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
```

### WinForms-specific conventions

- The sample demonstrates the use of `Grouping.Engine` in VB.NET for organizing and sorting data.
- It leverages the `ArrayList` to store objects, and the `Random` class to simulate data generation.
- Custom sorting is implemented by setting an `IComparer` object for the specific column.

### Copyright Notice

© 2013 Syncfusion. All rights reserved.

---

<!-- tags: [product, module, control, api, version?] keywords: [grouping, Grouping.Engine, ArrayList, Random, IComparer, sorting] -->
```

---

<!-- 페이지 51 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_059.jpeg
document_name: grouping
page_number: 059
page_id: grouping#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:08Z
fidelity: lossless
-->

# Essential Grouping

## 5 Frequently Asked Questions

The following are some common tasks that you might encounter as you use Essential Grouping in your applications:

### 5.1 How to Access the Value of a Record Or Field?

The `groupingEngine.Table.Records` property will allow you to access the records (items) in your `IList` and particular fields (properties) in the records.

#### Code Examples

##### [C#]
```csharp
// Assumes the datasource is an IList holding objects of type MyObject.
// Retrieves the third object in the list.
MyObject o = this.groupingEngine.Table.Records[2].GetData() as MyObject;

// A is a public property of MyObject, so "A" is treated as a field.
object someValue = this.groupingEngine.Table.Records[2].GetValue("A");
```

##### [VB.NET]
```vbnet
' Assumes the datasource is an IList holding objects of type MyObject.
' Retrieves the third object in the list.
Dim o As MyObject = CType(Me.groupingEngine.Table.Records(2).GetData(), MyObject)

' A is a public property of MyObject, so "A" is treated as a field.
Dim someValue As Object = Me.groupingEngine.Table.Records(2).GetValue("A")
```

### Note:
<!-- tags: [Essential Grouping, Records, Property Access, C#, VB.NET] keywords: [groupingEngine, Table.Records, GetValue, IList, MyObject, field access, property retrieval] -->
```

---

<!-- 페이지 52 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_063.jpeg
document_name: grouping
page_number: 063
page_id: grouping#page_063
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:19Z
fidelity: lossless
-->

# Essential Grouping

## 5.4 How to Add Summary Items?

Essential Grouping lets you summarize data by adding SummaryDescriptor objects to the schema information stored in the Engine.TableDescriptor.Summaries collection. You can have multiple summaries by adding several SummaryDescriptors.

### Code Examples

```csharp
[C#]

// Create a summary that computes the Int32Aggregate calculations on field B.
SummaryDescriptor sdInt32Agg = new SummaryDescriptor("BInt32Agg", "B", 
    SummaryType.Int32Aggregate);

// Add this summary to the Summaries collection.
groupingEngine.TableDescriptor.Summaries.Add(sdInt32Agg);
```

```vb
[VB.NET]

' Create a summary that computes the Int32Aggregate calculations on property B.
Dim sdInt32Agg As New SummaryDescriptor("BInt32Agg", "B", 
    SummaryType.Int32Aggregate)

' Add this summary to the Summaries collection.
groupingEngine.TableDescriptor.Summaries.Add(sdInt32Agg)
```

### Note

There are several overloads of the constructor for the SummaryDescriptor. We are using the overload that accepts a SummaryType enum as the third argument. This SummaryType will allow you to pick out some predefined calculations such as the Int32Aggregate functions like Max, Min, Sum, and Average. There are enums that specify double, boolean, and other aggregate types. Here we choose Int32 as that is the type of value we see in the B property in the data.

## 5.5 How to Bind a Datasource to the Grouping Engine?

Essential Grouping can use any IList object holding objects and a common System.Type as its datasource. The public properties of the common type can be used to group, sort and summarize the data in the IList.

### Example

The following code shows how to set an IList object to be the data source of a GroupingEngine object. Within Essential Grouping, the items in your IList datasource are referred to as records.

## Page-level Navigation/TOC (if applicable)
- 5.4 How to Add Summary Items?
- 5.5 How to Bind a Datasource to the Grouping Engine?

## Cross References
See also: Grouping Engine, SummaryDescriptor, TableDescriptor, Summaries collection, IList, System.Type.

## RAG Annotations
<!-- tags: [Syncfusion, Windows Forms, Grouping, SummaryDescriptor, TableDescriptor, IList, System.Type] keywords: [grouping engine, summaries, data source, aggregate calculations, summary types, add summary, bind data source, Essential Grouping] -->


---

<!-- 페이지 53 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_067.jpeg
document_name: grouping
page_number: 067
page_id: grouping#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:37Z
fidelity: lossless
-->

# Essential Grouping

- "[B] = 5 OR [B] < 0"
- "[D] LIKE 'd1' OR [B] = 2"

### Sample Code

```csharp
[C#]

// Filter on [D] = d1
RecordFilterDescriptor rfd = new RecordFilterDescriptor("[D] LIKE 'd1'");
this.groupingEngine.TableDescriptor.RecordFilters.Add(rfd);
```

```vbnet
[VB.NET]

' Filter on [D] = d1
Dim rfd As New RecordFilterDescriptor("[D] LIKE 'd1'")
Me.groupingEngine.TableDescriptor.RecordFilters.Add(rfd)
```

## 5.10 How to Group a Collection?

To sort your data, add the name of the property you want to sort to the **Engine.TableDescriptor.GroupedColumns** collection.

```csharp
[C#]

// Group column A.
groupingEngine.TableDescriptor.GroupedColumns.Add("A");
```

```vbnet
[VB.NET]

' Group column A.
groupingEngine.TableDescriptor.GroupedColumns.Add("A")
```

## 5.11 How to Retrieve Summary Item Values?

Summaries are calculated on groups of records. The **TopLevelGroup** is the collection of all records in the **IList** data source. If you have added additional grouping through the **groupingEngine.TableDescriptor.GroupedColumns.Add**, then in addition to the top level group, there will be additional groups available to you. Each group will have an associated summary value. So to retrieve a summary value, you need to specify the group associated with the summary.

<!-- tags: [grouping, filtering, sorting, summaries, data source, groups, records, summary values] keywords: [group, filter, sort, summary, record, data, values] -->
```

---

<!-- 페이지 54 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_071.jpeg
document_name: grouping
page_number: 071
page_id: grouping#page_071
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:49Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Provides an overview of data grouping features.
- Demonstrates grouping functionality specific to Syncfusion Winforms.
- Highlights key concepts like group customization and usage scenarios.

## Content
- **Introduction to Grouping**
  - Describes what grouping is and its importance in data management.
  - Explains how grouping can enhance user interactions in applications.
  
  ### Grouping Basics
  - Detailed explanation of how to implement grouping in WinForms.
  - Steps to configure group filters and group levels.
  
  ### Customizing Group Appearance
  - Tips on styling and customizing appearance of groups.
  - Examples of formatting groups using Syncfusion WinForms APIs.
  
  ### Grouping Operations
  - Lists operations such as collapsing, expanding, and sorting groups.
  - How to manage group interactively using mouse and keyboard inputs.
  
  <!-- tags: [syncfusion-winforms, grouping, essential-grouping, version-11.4.0.26] keywords: [grouping, Syncfusion, WinForms, data grouping, customization, operations] -->
```

---

<!-- 페이지 55 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_004.jpeg
document_name: grouping
page_number: 004
page_id: grouping#page_004
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:57:54Z
fidelity: lossless
-->

# Essential Grouping

## Overview

This section covers information on Essential Grouping, its key features, prerequisites to use the control, its compatibility with various OS and browsers, and finally the documentation details complimentary with the product. It comprises the following subsections:

### 1.1 Introduction to Essential Grouping

Essential Grouping is a 100% Native .NET library that provides you with support for managing and manipulating tabular information without dependencies on any particular UI component. Our grouping framework can be used in any .NET environment, including C#, VB.NET, and managed C++.

Syncfusion Essential Grouping is a data technology that allows you to easily access, manipulate, and display your data in a variety of configurations. Your data source can be any IList object whose items have public properties. You can easily sort the items on one or several of these public properties. You can display and retrieve items based on the grouping that is produced through these sorts, you can include caption information and / or summary information on these groups; you can impose filters on the items, retrieving only items that specify your filter conditions and you can also add expression properties to display calculated values depending upon other properties in the item.
```

---

<!-- 페이지 56 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_008.jpeg
document_name: grouping
page_number: 008
page_id: grouping#page_008
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:04Z
fidelity: lossless
-->

# Essential Grouping

## Content

### Readme

| Platform Variant | Path |
|------------------|------|
| 1. For Windows and BackOffice | [drive:]\Program Files\Syncfusion\Essential Studio\x.x.x.x\Infrastructure\Data\Release Notes\readme.htm |
| 2. For other platforms | [drive:]\Program Files\Syncfusion\Essential Studio\x.x.x.x\Infrastructure\Data\<asp/WPF> Release Notes\readme.htm |

### Release Notes

| Platform Variant | Path |
|------------------|------|
| 1. For Windows and BackOffice | [drive:]\Program Files\Syncfusion\Essential Studio\x.x.x.x\Infrastructure\Data\Release Notes\Release Notes.htm |
| 2. For other platforms | [drive:]\Program Files\Syncfusion\Essential Studio\x.x.x.x\Infrastructure\Data\<asp/WPF> Release Notes\Release Notes.htm |

### User Guide (this document)

- **Online**: [http://help.syncfusion.com/resources](http://help.syncfusion.com/resources) (Navigate to the Grouping User Guide.)
  - **Note**: Click "Download as PDF" to access a PDF version.
  
- **Installed Documentation**  
  Dashboard -> Documentation -> Installed Documentation.

### Class Reference

- **Online**: [http://help.syncfusion.com/resources](http://help.syncfusion.com/resources) (Navigate to the Reporting User Guide. Select "Grouping," and then click the Class Reference link found in the upper right section of the page.)
  
- **Installed Documentation**  
  Dashboard -> Documentation -> Installed Documentation.

## Related Information

- **Product**: Syncfusion Winforms
- **Version**: 11.4.0.26
- **Documentation Source**: Syncfusion Help Portal and Installed Documentation

<!-- tags: [syncfusion-sdk, winforms, grouping, user-guide, release-notes, class-reference, documentation] keywords: [syncfusion, essential studio, windows, backoffice, asp, wpf, user guide, release notes, class reference, online, installed documentation] -->
```

---

<!-- 페이지 57 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_012.jpeg
document_name: grouping
page_number: 012
page_id: grouping#page_012
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:18Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Demonstrates how to easily access, manipulate, and display data in various configurations using Syncfusion Essential Grouping.
- Offers capabilities to sort, display, filter, and calculate data based on grouping in Windows Forms and ASP.NET.
- Emphasizes customization and flexibility in handling data.

## Content

### Windows Forms Grouping

#### Introduction to Syncfusion Essential Grouping
Syncfusion Essential Grouping is a data technology that allows you to easily access, manipulate, and display your data in a variety of configurations. Your data source can be any Ilist object whose items have public properties. You can easily sort the items on one or several of these public properties. You can display and retrieve items based on the grouping that is produced through these sorts. You can include caption information and/or summary information on these groups. You can impose filters on the items, retrieving only items that specify your filter conditions, and you can also add expression properties to display calculated values depending upon other properties in the item.

#### Featured Samples

![](attachment.png)

**Figure 5: Grouping samples displayed in the Windows Forms Sample Browser**

- **Grouping With Data Grid Demo**: Demonstrates how grouping interacts with a data grid.
- **Grouping Tutorial**: Provides a tutorial for implementing grouping features.
- **Random Test Demo**: Displays random test scenarios involving grouping.

3. **Select any sample and browse through the features.**

### ASP.NET Grouping

1. **In the Dashboard window, click Run Samples for ASP.NET under Reporting Edition panel. The ASP.NET Sample Browser window is displayed.**

#### Note: You can view the samples in any of the three ways displayed.

## References and Support
- For additional resources and support, visit:
  - **Forum**: Link to Syncfusion's community forum for discussions and queries.
  - **Documentation**: Access detailed documentation for WinForms and ASP.NET Grouping features.
  - **Sales**: Contact for sales inquiries.
  - **Support**: Technical support for integration and usage issues.

```markdown

## Page-level Navigation/TOC (if applicable)
- `Grouping Overview`
- `Windows Forms Grouping`
  - `Introduction`
  - `Featured Samples`
  - `Navigation and Support`
- `ASP.NET Grouping`
  - `Accessing Samples`
  - `Support and Resources`

## Cross References
- **Related Sections**:
  - Grouping in Windows Forms and ASP.NET.
- **API Documentation**:
  - Refer to the Syncfusion documentation for detailed API references.

## RAG Annotations
<!-- tags: [grouping, windows forms, asp.net, sorting, filtering, reporting] keywords: [syncfusion, data manipulation, features, samples, dashboard, forum, documentation, sales, support] -->
``` 
```

---

<!-- 페이지 58 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_016.jpeg
document_name: grouping
page_number: 016
page_id: grouping#page_016
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:34Z
fidelity: lossless
-->

# Essential Grouping

## Getting Started

This section will show you how easy it is to get started using Essential Grouping. It will give you a basic introduction to the concepts you need to know before getting started with the product and some tips and ideas on how to implement Grouping into your projects to improve customization and increase efficiency. It shows how to create an IList data source and use it with Grouping. The datasource is an ArrayList of custom objects. As part of this lesson, you will see how to iterate through the data in the GroupingEngine.

### 3.1 Creating Platform Application

This section illustrates the step-by-step procedure to create the following platform applications.

#### Creating a Windows Application

1. Open Microsoft Visual Studio. Go to File menu and click New Project. In the New Project dialog, select Windows Forms Application template, name the project and click OK.

![Creating a New Project in Microsoft Visual Studio](https://example.com/new_project_image.jpg)

---

## Overview

- Introduction to Essential Grouping and its benefits.
- Step-by-step guide to setting up a Windows Forms Application.
- Demonstrates creating an IList data source and using it with Grouping.

## Content

### 3.1 Creating Platform Application

This section provides detailed instructions for setting up a Windows Forms Application using Microsoft Visual Studio. The steps include:

1. **Open Visual Studio**: Launch Microsoft Visual Studio.
2. **Access New Project**: Go to the **File** menu and select **New Project**.
3. **Choose Template**: In the **New Project** dialog, select the **Windows Forms Application** template.
4. **Name the Project**: Enter a name for your project in the **Name** field.
5. **Confirm**: Click **OK** to create the project.

The image included above shows the **New Project** dialog box, highlighting the selection of the **Windows Forms Application** template.

## Code Examples

### Example: Creating a Data Source

```csharp
using System;
using System.Collections.Generic;

public class Product
{
    public string Name { get; set; }
    public double Price { get; set; }
    public string Category { get; set; }
}

public class DataProvider
{
    public static IList<Product> GetProductList()
    {
        List<Product> productList = new List<Product>
        {
            new Product { Name = "Laptop", Price = 1200.00, Category = "Electronics" },
            new Product { Name = "Pen", Price = 1.50, Category = "Stationery" },
            new Product { Name = "Smartphone", Price = 800.00, Category = "Electronics" },
            new Product { Name = "Pencil", Price = 1.00, Category = "Stationery" }
        };

        return productList;
    }
}
```

## RAG Annotations

<!-- tags: [Essential Grouping, Windows Forms Application, Data Source, IList, GroupingEngine, Product, ArrayList] keywords: [Microsoft Visual Studio, New Project, Windows Forms, Data Source, Essential Grouping] -->

```

---

<!-- 페이지 59 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_020.jpeg
document_name: grouping
page_number: 020
page_id: grouping#page_020
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:51Z
fidelity: lossless
-->

## Essential Grouping

- Syncfusion.Shared.Base.dll
- Syncfusion.Shared.Windows.dll

Essential Grouping is now deployed in your Windows / WPF applications.

### 3.2.2 ASP.NET

Now, you have created a ASP.NET application (refer Creating Platform Application). This section will guide you to deploy Essential Grouping in an ASP.NET Application.

The following steps will guide you to deploy Essential Grouping in an ASP.NET application:

1. **Marking the Application directory**-The appropriate directory, usually where the aspx files are stored, must be marked as Application in IIS.
2. **Syncfusion Assemblies**-The Syncfusion assemblies need to be in the bin folder that is beside the aspx files.

**Note:** They can also be in the GAC, in which case, they should be referenced in Web.config file.

#### Configuration in Web.config

```xml
<configuration>
    <system.web>
        <compilation>
            <assemblies>
                <add assembly="Syncfusion.Grid.Grouping.Web, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89"/>
            </assemblies>
        </compilation>
        .
        .
        .
    </system.web>
</configuration>
```

**Note:** The version numbers in the above references will vary depending on the version you are linking to.

1. **Data Files**-If you have .xml, .mdb, or other data files, ensure that they have sufficient security permission. Authenticated Users should have full control over the files and the directories in order to give ASP.NET code, enough permissions to open the file during runtime.
```html
```

---

<!-- 페이지 60 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: grouping
page_number: 024
page_id: grouping#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:03Z
fidelity: lossless
-->

## Example: Essential Grouping in a WinForms Application

### Overview
- Demonstrates the implementation of grouping in a WinForms application.
- Shows how to create a class `MyObject` with properties for grouping and displaying data.
- Includes a constructor that initializes the object with a numerical parameter.
- Provides public string properties `A`, `B`, `C`, and `D` for accessing grouped data.
- Overrides the `ToString` method for custom string representation.

### Code Example

#### C#

```csharp
{
    private string aValue;
    private string bValue;
    private string cValue;
    private string dValue;

    public MyObject(int i)
    {
        aValue = string.Format("a{0}", i);

        // Use digit only.
        bValue = string.Format("{0}", i);
        cValue = string.Format("c{0}", i % 3);
        dValue = string.Format("d{0}", i % 2);
    }

    public string A
    {
        get { return aValue; }
        set { aValue = value; }
    }

    public string B
    {
        get { return bValue; }
        set { bValue = value; }
    }

    public string C
    {
        get { return cValue; }
        set { cValue = value; }
    }

    public string D
    {
        get { return dValue; }
        set { dValue = value; }
    }

    public override string ToString()
    {
        return A + "\t" + B + "\t" + C + "\t" + D;
    }
}
```

#### VB.NET

```vb
Module Module1
```

### Explanation
- **Constructor**: The `MyObject` constructor initializes the private fields `aValue`, `bValue`, `cValue`, and `dValue` based on the input integer `i`. The `string.Format` method is used to create formatted strings.
- **Properties**: The `A`, `B`, `C`, and `D` properties provide access to the private fields, allowing both retrieval and modification of the values.
- **ToString Method**: Overrides the default `ToString` method to return a tab-separated string representation of the object's values.

#### Notes:
- The use of the modulus operator (`%`) in the calculations for `cValue` and `dValue` suggests a cyclic behavior based on the input `i`.
- The `ToString` method formats the output in a tabular form, making it suitable for display in a grid or table.

### API Reference

#### Class
- **MyObject**
  - **Constructor**: `MyObject(int i)`
    - Initializes the object with a numerical parameter `i`.
  - **Properties**:
    - `A`: A string property representing the first group.
    - `B`: A string property representing the second group.
    - `C`: A string property representing the third group.
    - `D`: A string property representing the fourth group.
  - **Method**:
    - `ToString()`: Overrides the default implementation to provide a custom string representation of the object.

### RAG Annotations
<!-- tags: [Syncfusion Winforms, grouping, MyObject, C#, VB.NET, property, ToString] keywords: [grouping, WinForms, object initialization, property accessor, tab-separated string, override, modulus, tabular display] -->
```

---

<!-- 페이지 61 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_028.jpeg
document_name: grouping
page_number: 028
page_id: grouping#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:24Z
fidelity: lossless
-->

# Essential Grouping

```vb
Imports Syncfusion.Grouping
```

Then create a `Grouping.Engine` object and set the `ArrayList` we created to be its data source.

**Note:** For more details on creating array list, refer to the **Creating an ArrayList Of Objects** topic.

### Creating a Grouping Engine Object

#### C#

```csharp
// Put this code in the Main function after Console.ReadLine().
// Create a Grouping.Engine object.
Engine groupingEngine = new Engine();

// Set its data source.
groupingEngine.SetSourceList(list);
```

#### VB.NET

```vb
Imports Syncfusion.Grouping

' Put this code in the Main function after Console.ReadLine().
' Create a Grouping.Engine object.
Dim groupingEngine As New Engine()

' Set its data source.
groupingEngine.SetSourceList(list)
```

ArrayList of Objects is set as the datasource for the Grouping engine.

### 4.1.3 Iterating Through the Data

Now, we have set a datasource in the Grouping Engine. Let's see how to iterate through the data.

This section will show you how to access the data through the `Grouping.Engine` object by using the `Engine.Table.Records` collection.

### Summary

- Created a `Grouping.Engine` object and set its data source to an `ArrayList`.
- Demonstrated how to iterate through the data using the `Engine.Table.Records` collection.

### Next Steps

Explore how to manipulate and display the grouped data in a grid or similar UI component.

<!-- tags: [grouping, datasource, ArrayList, Grouping.Engine, iteration, records, WinForms] keywords: [grouping engine, arraylist, iterating through data, engine.table.records, syncfusion group, syncfusion data engine] -->
```

---

<!-- 페이지 62 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_032.jpeg
document_name: grouping
page_number: 032
page_id: grouping#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:36Z
fidelity: lossless
-->

## Essential Grouping

### Display After Grouping by Property C

![Figure: Display After Grouping by Property C](image.png)

#### The Grouping.TableDescriptor Class

As noted previously, the `grouping.TableDescriptor` is the property that maintains the schema information for the data source. Here is a table showing some collections in the `TableDescriptor` that you will be using as the lessons continue.

| TableDescriptor Property | Description                                           |
|---------------------------|-------------------------------------------------------|
| SortedColumns            | Holds sorted properties.                              |
| GroupedColumns           | Holds grouped properties.                             |
| Summaries                | Holds the columns that have summaries.               |
| RecordFilters            | Holds information on columns that are part of        |

---

© 2013 Syncfusion. All rights reserved. 
```

---

<!-- 페이지 63 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: grouping
page_number: 036
page_id: grouping#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:44Z
fidelity: lossless
-->

# Essential Grouping

## Overview

- Displays records grouped under the "c1" group.
- Demonstrates code for showing all records under the primary group.
- Explains how to implement the `ShowRecordsUnderGroup` method in the `Main` method.

## Content

### Displaying Grouped Records

The following figure shows the records from the "c1" group:

Figure: Last Section Shows the Records from the "c1" Group

#### Code Implementation

Similar code can be used to display all the records by passing the 'primary' group to your `ShowRecordsUnderGroup` method. To implement this, add the following code to the `Main` method.

```csharp
// Show all records under the TopLevelGroup.
ShowRecordsUnderGroup(groupingEngine.Table.TopLevelGroup);

// Pause
Console.ReadLine();
```

### Notes

- Ensure that the `groupingEngine` object is properly initialized and available in the `Main` method.
- The `ShowRecordsUnderGroup` method should be defined to handle the display logic for the grouped records.

---

This section details the display of records grouped under specific categories, focusing on the "c1" group, and provides a code example for showing all records under the main group.

## API Reference

- **Namespace**: (Not explicitly shown in the image; would require additional context or documentation)
- **Class**: `GroupingEngine`
- **Method**: `ShowRecordsUnderGroup`

### Parameters

| Name               | Type              | Description                                                                 |
|--------------------|-------------------|-----------------------------------------------------------------------------|
| `topLevelGroup`    | `GroupInfo`       | The primary group under which all records should be displayed. |

## Code Examples

Example: Showing all records under the top-level group.

```csharp
// Example code to display all records under the top-level group.
ShowRecordsUnderGroup(groupingEngine.Table.TopLevelGroup);
Console.ReadLine();
```

## Page-level Navigation/TOC (if applicable)

- [ ] Essential Grouping
  - [ ] Displaying Grouped Records
  - [ ] Code Implementation
  - [ ] Notes
  - [ ] API Reference
  - [ ] Code Examples

<!-- tags: [Syncfusion Winforms, Grouping, Records, GroupInfo, GroupingEngine, ShowRecordsUnderGroup, TopLevelGroup] keywords: [grouping, records, top level group, group, groupinfo, groupingengine, showrecordsundergroup, main method, pause, console.readline, display logic, implementation] -->
```

---

<!-- 페이지 64 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_040.jpeg
document_name: grouping
page_number: 040
page_id: grouping#page_040
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:59Z
fidelity: lossless
-->

# Essential Grouping

In addition to grouping data, you may want to filter it for some special criteria. For example, you may want to see the total monthly sales due to orders under some value. Essential Grouping gives you the flexibility to add calculated values to the data, and then use these values to produce other information like total monthly sales due for respective order etc.

The following data manipulation techniques are available in Essential Grouping:

## 4.3.1 Filters

Another collection that is part of the schema information in the `Engine.TableDescriptor` is the `RecordFilters` collection. This collection lets you filter the data to see only the items that are in your data list and that satisfy the criteria that is specified. You can express the criteria as a logical expression using the property names, algebraic, and logical operators. You can also use LIKE, MATCH, and IN operators.

### 1. In the Console Application used in lessons 1 and 2, comment out all the code that is in the `Main` method and add the following code to create a data object and set it into the Grouping Engine.

[C#]

```csharp
static void Main(string[] args)
{
    // Create an arraylist of random MyObjects.
    ArrayList list = new ArrayList();
    Random r = new Random();

    for (int i = 0; i < 10; i++)
    {
        list.Add(new MyObject(r.Next(5)));
    }

    // Create a Grouping.Engine object.
    Engine groupingEngine = new Engine();

    // Set its datasource.
    groupingEngine.SetSourceList(list);
}
```

[VB.NET]
```vb
Sub Main(ByVal args As String())
    ' Create an arraylist of random MyObjects.
    Dim list As New ArrayList()
    Dim r As New Random()

    For i As Integer = 0 To 9
        list.Add(New MyObject(r.Next(5)))
    Next

    ' Create a Grouping.Engine object.
    Dim groupingEngine As New Engine()

    ' Set its datasource.
    groupingEngine.SetSourceList(list)
End Sub
```

<!-- tags: [grouping, filtering, essential grouping, record filters, data manipulation] keywords: [grouping, filters, criteria, logical operators, data object, Grouping.Engine, SetSourceList, ArrayList, Random, MyObject] -->
```

---

<!-- 페이지 65 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_044.jpeg
document_name: grouping
page_number: 044
page_id: grouping#page_044
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:14Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Demonstrates filtering and accessing grouped data directly in the engine.
- Example code for C# and VB.NET to apply filters and iterate through filtered records.

## Content

### Code Example in C#

```csharp
rfd = new RecordFilterDescriptor("[D] LIKE 'd1' OR [B] = 2");
groupingEngine.TableDescriptor.RecordFilters.Add(rfd);

// Access the data directly from the Engine.
foreach (Record rec in groupingEngine.Table.FilteredRecords)
{
    MyObject obj = rec.GetData() as MyObject;
    if (obj != null)
    {
        Console.WriteLine(obj);
    }
}

// Pause
Console.ReadLine();
```

### Code Example in VB.NET

```vb
groupingEngine.TableDescriptor.RecordFilters.Clear()

rfd = New RecordFilterDescriptor("[D] LIKE 'd1' OR [B] = 2")
groupingEngine.TableDescriptor.RecordFilters.Add(rfd)

' Access the data directly from the Engine.
For Each rec In groupingEngine.Table.FilteredRecords
    Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
        Console.WriteLine(obj)
    End If
Next rec

' Pause
Console.ReadLine()
```

## API Reference

### Methods/Properties
- `RecordFilterDescriptor(string filterExpression)`
  - Creates a new record filter descriptor with the specified filter expression.

- `TableDescriptor.RecordFilters`
  - Collection of record filter descriptors applied to the table.

- `Record.GetData()`
  - Retrieves the data object associated with the record.

- `FilteredRecords`
  - Collection of records that satisfy the current filter criteria.

## Code Examples

The examples demonstrate how to:
- Define a filter expression using `RecordFilterDescriptor`.
- Apply the filter to a `groupingEngine`.
- Iterate through the filtered records and access their data.
- Pause the program to view the output.

## Cross References

- See also:
  - [Using Filters in Grouping Engine](#)
  - [Accessing Data in Grouping](#)

<!-- tags: [WinForms, Grouping, Filter, Engine] keywords: [grouping, filter, record, engine, data access] -->
```

---

<!-- 페이지 66 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_048.jpeg
document_name: grouping
page_number: 048
page_id: grouping#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:27Z
fidelity: lossless
-->

## Essential Grouping

![Figure 19: Screen showing the initial data followed by values computed using the expression 2.1 * [B] + 3.2](attachment://2.png)

### 4.3.3 Sorting

To sort your data, you must add the name of the property that you want to sort to the `Engine.TableDescriptor.SortedColumns` collection.

To demonstrate this, create and sort a dataset in a Console Application:

In the Console Application, comment out all the code that is in the `Main` method and add this code to create a data object, set it into the `GroupingEngine`, display the data, sort it by property A, and re-display the sorted data.

```csharp
[C#]

// Create an ArrayList of random MyObjects.
ArrayList list = new ArrayList();
Random r = new Random();

for(int i = 0; i < 10; i++)
{
    list.Add(new MyObject(r.Next(5)));
}

// Create a Grouping.Engine object.
Engine groupingEngine = new Engine();
```

## API Reference (if applicable)

### WinForms-specific conventions

- Use C# examples unless VB is explicitly shown.
- Indicate namespaces and types correctly, such as `Syncfusion.Windows.Forms.Tools.TabControlAdv` or `Syncfusion.Windows.Forms.Grid`.

### Example Usage

The snippet demonstrates creating a dataset and initializing a `GroupingEngine` for sorting purposes.

## Code Examples

```csharp
// Example showing the creation of a random dataset and its sorting.
ArrayList list = new ArrayList();
Random r = new Random();

for(int i = 0; i < 10; i++)
{
    list.Add(new MyObject(r.Next(5)));
}

Engine groupingEngine = new Engine();
```

<!-- tags: [syncfusion, windows forms, grouping, sorting, tabledescriptor] keywords: [sort, property, data, dataset, demo, c#, main method, console application, groupingengine, random data] -->
```

---

<!-- 페이지 67 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_052.jpeg
document_name: grouping
page_number: 052
page_id: grouping#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:40Z
fidelity: lossless
-->

# Essential Grouping

## Overview

- Demonstrates how to perform custom sorting using a custom comparer in VB.NET.
- Explains the use of SortColumnDescriptor.Comparer to specify a custom comparer object.
- Provides steps for creating a custom comparer class and integrating it into the sorting process.

## Content

### Sorting Functions

The following method overloads are available for adding sort columns:

```vb
Overloads Public Function Add(propertyName As String) As Integer
Overloads Public Function Add(propertyName As String, dir As ListSortDirection) As Integer
Overloads Public Function Add(sdc As SortColumnDescriptor) As Integer
```

The second overload allows specifying the sort direction. The `SortColumnDescriptor.Comparer` property is an `IComparer` property that enables the use of a custom comparer object.

#### Custom Sorting Using IComparer

**Note:** We are going to use the third function in this section to perform custom sorting.

The following steps illustrate how to do custom sorting using the `IComparer` property:

1. Create a class that implements `IComparer`, which can accept values such as `ax`, where `x` is a digit used for comparison. This leads to numerical sorting, ignoring the leading character.

15. Add the following code immediately after the end of the `Class1` code:

### Custom Comparer Implementation

```csharp
public class AComparer : IComparer
{
    // Implementing IComparer to define the object comparisons.
    public int Compare(object x, object y)
    {
        if (x == null && y == null)
            return 0;
        else if (x == null)
            return -1;
        else if (y == null)
            return 1;
        else
        {
            int sx = 0;
            int sy = 0;
            try
            {
                // Ignoring the leading character to have numerical sorting.
                sx = int.Parse(x.ToString().Substring(1));
                // Additional code for comparing numerical values would follow here.
            }
            // Further implementation details are omitted for brevity.
        }
    }
}
```

## API Reference

The following sections detail how to use the `SortColumnDescriptor.Comparer` property to implement custom sorting:

### Methods

- **Add(sdc As SortColumnDescriptor) As Integer:** Adds a column descriptor with a custom comparer for sorting.

## Code Examples

The provided code snippet demonstrates the creation of a custom comparer class that ignores the leading character for numerical sorting.

### Import and Using Statements

Ensure that the following namespaces are included for the code to work seamlessly in your project:

```csharp
using System;
using System.Collections;
```

### Additional Information

For further details on implementing custom sorting in Syncfusion WinForms, refer to the official documentation or contact Syncfusion support.

## Cross References

- See also: [Syncfusion WinForms Documentation](https://www.syncfusion.com/documentation/windows-forms/)

### Page-level Navigation/TOC

- [Section 1](#essentials): Essential Grouping
- [Section 2](#customsorting): Custom Sorting Using IComparer
- [Section 3](#apireference): API Reference
- [Section 4](#codeexamples): Code Examples

<!-- tags: [Syncfusion WinForms, Custom Sorting, IComparer, SortColumnDescriptor, Numerical Sorting] keywords: [custom sorting, comparer, numerical, leading character,ignore] -->
```

---

<!-- 페이지 68 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_056.jpeg
document_name: grouping
page_number: 056
page_id: grouping#page_056
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:01Z
fidelity: lossless
-->

# Essential Grouping

```csharp
Console.WriteLine(obj)
End If
Next rec

' Pause
Console.ReadLine()
```

### Figure 21: Screen Showing Custom Sorting on Property A

![Figure 21: Screen Showing Custom Sorting on Property A](https://i.imgur.com/TFEx2.png)

## 4.4 Algebra Supported In Expressions / Filters

Expressions can be any well-formed algebraic combination of the following:

- Property (column) names enclosed with square brackets ([ ])
- Numerical constants and literals
- Algebraic and logical operators

The computations are performed as listed below, with level one operations done first.

- \*, /: multiplication, division
- +, -: addition, subtraction

## API Reference
(Insert API reference content here as per structure schema)

## Code Examples
(Insert code examples here as per structure schema)

<!-- tags: [syncfusion-sdk, expression-filters, algebraic-combinations, property-sorting, syncfusion-winformsversion: 11.4.0.26] keywords: [expression, filters, algebraic, properties, sorting, custom] -->
```

---

<!-- 페이지 69 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_060.jpeg
document_name: grouping
page_number: 060
page_id: grouping#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:11Z
fidelity: lossless
-->

# Essential Grouping

1. The `groupingEngine.Table.Records` collection will give you access to the raw data in your datasource through the `GroupingEngine`.

2. If you have applied filters or have sorted the data and want to access the sorted or filtered data, then you must use the `GroupingEngine.Table.FilteredRecords` collection.

3. This collection reflects the visible state of the data in the `GroupingEngine`.

## 5.2 How to Add Custom Calculations to Expression Fields?

Essential Grouping lets you add your own functions to a function library which can be used in an expression field. In this manner, you can do custom calculations in expressions. This is a two-step process which is given below:

1. Register the function name and a delegate with the grouping engine.
2. Implement a method that does your calculation.

In the code given below, we add a method named 'Func' that takes two arguments and performs a certain calculation on those arguments.

```csharp
// Step 1
// Add function named Func that uses a delegate named ComputeFunc to define a custom calculation.
ExpressionFieldEvaluator evaluator = 
    this.groupingEngine.TableDescriptor.ExpressionFieldEvaluator;
evaluator.AddFunction("Func", new 
    ExpressionFieldEvaluator.LibraryFunction(ComputeFunc));

// Sample usage in an Expression column.
this.groupingEngine.TableDescriptor.ExpressionFields.Add("test");
this.groupingEngine.TableDescriptor.ExpressionFields["test"].Expression = 
    "Func([Col1], [Col2])";

//...
```

```csharp
// Step 2
// Define ComputeFunc that returns the absolute value of the 1st arg minus 2 * the 2nd arg.
public string ComputeFunc(string s)
{
    // Get the list delimiter (for en-us, it is a comma).
    char comma = 
        Convert.ToChar(this.gridGroupingControl1.Culture.TextInfo.ListSeparator);
}
```

<!-- tags: [product, module, control, api, version?] keywords: [grouping, filtering, sorting, data access, custom calculations, expression fields, grouping engine, function library, delegate, ComputeFunc, FilteredRecords, TableDescriptor] -->
```

---

<!-- 페이지 70 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: grouping
page_number: 064
page_id: grouping#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:25Z
fidelity: lossless
-->

# Essential Grouping

```csharp
using Syncfusion.Grouping;

// Create a Grouping.Engine object.
Engine groupingEngine = new Engine();

// Set its datasource.
groupingEngine.SetSourceList(list);
```

```vb
Imports Syncfusion.Grouping

' Create a Grouping.Engine object.
Dim groupingEngine As New Engine()

' Set its datasource.
groupingEngine.SetSourceList(list)
```

## 5.6 How to Clear a Filter?

To clear all filters, call the `groupingEngine.TableDescriptor.RecordFilters.Clear` method.

### Clear All Filters

```csharp
// Removes all the filters associated with the table.
this.gridGroupingControl.TableDescriptor.RecordFilters.Clear();
```

```vb
' Removes all the filters associated with the table.
Me.gridGroupingControl1.TableDescriptor.RecordFilters.Clear()
```

### Remove Specific Filter by Name

```csharp
// Removes the Filter associated by sending the argument as RecordFilterDescriptor.name
this.gridGroupingControl.TableDescriptor.RecordFilters.Remove(RecordFilterDescriptor.Name);
```

### Remove RecordFilter by Index

```csharp
// Removes the RecordFilter associated by mentioning as index.
this.gridGroupingControl1.TableDescriptor.RecordFilters.RemoveAt();
```

```vb
' Removes the Filter associated by sending the argument as
Me.gridGroupingControl1.TableDescriptor.RecordFilters.Remove(RecordFilterDescriptor.Name);
```

### Remove Specific Filter by Name (Vb.Net)

```vb
' Removes the Filter associated by sending the argument as
Me.gridGroupingControl1.TableDescriptor.RecordFilters.Remove(RecordFilterDescriptor.Name);
```
```

---

<!-- 페이지 71 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_068.jpeg
document_name: grouping
page_number: 068
page_id: grouping#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:36Z
fidelity: lossless
-->

# Essential Grouping

For example, the code below assumes that you have grouped the table on field "C" and are looking for the summary associated with the group whose records have field "C" equal to the value "c1". It also shows the same summary value for the TopLevelGroup.

## C#

```csharp
// To simplify notation, set this using the statement at the top of your code file.
using ISummary = Syncfusion.Collections.BinaryTree.ITreeTableSummary;

// Now get the Summary value for the TopLevelGroup group.
ISummary groupSummary =
groupingEngine.Table.TopLevelGroup.GetSummary("BInt32Agg");
Int32AggregateSummary int32Summary = (Int32AggregateSummary) groupSummary;

Console.WriteLine("whole table {0}, {1}, {2}", int32Summary.Sum,
int32Summary.Average, int32Summary.Maximum);

// Value for "c1" group.
groupSummary =
groupingEngine.Table.TopLevelGroup.Groups["c1"].GetSummary("BInt32Agg");
int32Summary = (Int32AggregateSummary) groupSummary;

Console.WriteLine("c1-group {0}, {1}, {2}", int32Summary.Sum,
int32Summary.Average, int32Summary.Maximum);
```

## VB.NET

```vb.net
' To simplify notation, set this using the statement at the top of your code file.
Imports ISummary = Syncfusion.Collections.BinaryTree.ITreeTableSummary

' Now get the Summary value for the TopLevelGroup group.
Private groupSummary As ISummary =
groupingEngine.Table.TopLevelGroup.GetSummary("BInt32Agg")
Private int32Summary As Int32AggregateSummary = CType(groupSummary,
Int32AggregateSummary)

Console.WriteLine("whole table {0}, {1}, {2}", int32Summary.Sum,
int32Summary.Average, int32Summary.Maximum)

' Value for "c1" group.
Private groupSummary =
groupingEngine.Table.TopLevelGroup.Groups("c1").GetSummary("BInt32Agg")
Private int32Summary = CType(groupSummary, Int32AggregateSummary)
```

<!-- tags: [product, module, control, api, version?] keywords: [grouping, C#, VB.NET, summary, Table, TopLevelGroup, Group, GetSummary, BInt32Agg, Int32AggregateSummary, Syncfusion Winforms, 11.4.0.26] -->
```