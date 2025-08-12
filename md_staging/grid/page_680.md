```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_680.jpeg
document_name: grid
page_number: 680
page_id: grid#page_680
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:33:16Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Creating a Sample

1. **Initialize an ArrayList**  
Use an `ArrayList` to store data for the grid. The data is added as objects of a custom `Data` class. Here is an example for C# and VB.NET:

#### C#

```csharp
using System;
using System.Collections;

ArrayList al = new ArrayList();
al.Add(new Data("Condiments", "Charlotte Cooper", "Bigfoot Breweries"));
al.Add(new Data("Confections", "Regina Murphy", "Grandma Kelly's Homestead"));
al.Add(new Data("Grains/Cereals", "Jean-Guy Laizon", "Ma Maison"));
al.Add(new Data("Meat/Poultry", "Shelley Burke", "New Orleans Cajun Delights"));
al.Add(new Data("Produce", "Mayumi Ohno", "Mayumi's"));
al.Add(new Data("Seafood", "Robb Merchant", "New England Seafood Cannery"));
```

#### VB.NET

```vb
Imports System
Imports System.Collections

Dim al As ArrayList = New ArrayList()
al.Add(New Data("Condiments", "Charlotte Cooper", "Bigfoot Breweries"))
al.Add(New Data("Confections", "Regina Murphy", "Grandma Kelly's Homestead"))
al.Add(New Data("Grains/Cereals", "Jean-Guy Laizon", "Ma Maison"))
al.Add(New Data("Meat/Poultry", "Shelley Burke", "New Orleans Cajun Delights"))
al.Add(New Data("Produce", "Mayumi Ohno", "Mayumi's"))
al.Add(New Data("Seafood", "Robb Merchant", "New England Seafood Cannery"))
```

2. **Assign the ArrayList to the Grid's DataSource**  
The `ArrayList` is then set as the data source for the `GridGroupingControl`.

#### C#

```csharp
this.gridGroupingControl1.DataSource = al;
```

#### VB.NET

```vb
Me.gridGroupingControl1.DataSource = al
```

3. **Run the Sample**  
Once the data is assigned, running the sample will display the grid similar to the one shown below.

### Sample Output

The resulting grid will display the data structured and grouped according to the provided `ArrayList` and custom `Data` objects.

## Advanced Grouping Operations

Once the grid is populated, you can perform advanced grouping operations using the `GridGroupingControl`. This control supports various functionalities such as grouping, sorting, and filtering.

### Grouping Data

To perform grouping, the grid uses the `GridGroupingControl`'s built-in features to group data based on specific criteria. For example, you can group rows by the first column, such as "Condiments," "Confections," etc.

### Sorting Data

Sorting can be applied to any column to organize the data in ascending or descending order. This is achieved using the grid's sorting options.

### Filtering Data

Filters can be applied to focus on specific subsets of the data, allowing for more targeted analysis.

---

<!-- tags: [essentialgrid, windowsforms, data_source, arraylist, gridgroupingcontrol] keywords: [arraylist, data_source, grid, grouping, sorting, filtering, windowsforms, essentialgrid] -->
```