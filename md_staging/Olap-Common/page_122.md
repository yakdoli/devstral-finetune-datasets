```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_122.jpeg
document_name: Olap Common
page_number: 122
page_id: Olap Common#page_122
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:14Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
// Specifying the DataProvider for OlapDataManager.
m_OlapDataManager.DataProvider = this.DataProvider;
// Set current report for OlapDataManager.
m_OlapDataManager.SetCurrentReport(CreateOlapReport());
// Specifying the OlapDataManager for OlapGrid.
this.olapGrid1.OlapDataManager = m_OlapDataManager;
// Data Binding.
this.olapGrid1.DataBind();
}
```

### [VB]
```vb
Private Sub MainPage_Loaded(ByVal sender As Object, ByVal e As RoutedEvent Args)

    ' Initialize the service connection.
    Me.InitializeConnection()
    
    ' Instantiating the OlapDataManager.
    Dim m_OlapDataManager As OlapDataManager = New OlapDataManager()
    
    ' Specifying the DataProvider for OlapDataManager.
    m_OlapDataManager.DataProvider = Me.DataProvider
    
    ' Set current report for OlapDataManager.
    m_OlapDataManager.SetCurrentReport(CreateOlapReport())
    
    ' Specifying the OlapDataManager for OlapGrid.
    Me.olapGrid1.OlapDataManager = m_OlapDataManager
    
    ' Data Binding.
    Me.olapGrid1.DataBind()
End Sub
```

### Example Output - Internet Sales Amount

|  | Internet Sales Amount |  |
| --- | --- | --- |
|  | Australia | Canada | France | Germany | United Kingdom | United States | Total |
| FY 2002 | $2,568,701.39 | $573,100.97 | $414,245.32 | $513,353.17 | $550,507.33 | $2,452,176.07 | $7,072,084.24 |
| FY 2003 | $2,099,585.43 | $305,010.69 | $633,399.70 | $593,247.24 | $696,594.97 | $1,434,296.26 | $5,762,134.30 |
| FY 2004 | $4,383,479.54 | $1,088,879.50 | $1,592,880.75 | $1,784,107.09 | $2,140,388.50 | $5,483,882.67 | $16,473,618.05 |
| FY 2005 | $9,234.23 | $10,853.70 | $3,491.95 | $3,604.83 | $4,221.41 | $19,434.51 | $50,840.63 |
| Total | $9,061,000.58 | $1,977,844.86 | $2,644,017.71 | $2,894,312.34 | $3,391,712.21 | $9,389,789.51 | $29,358,677.22 |

> **Note:** Click [here for Sample Report](#) to view a sample report.

## References
- Sample Report: [here for Sample Report](#)

<!-- tags: [syncfusion, windowsforms, olapcommon, data provider, data manager, grid, sample report, version 11.4.0.26] keywords: [internet sales amount, australia, canada, france, germany, united kingdom, united states, fiscal years, total sales, data binding, data provider, olap report, olapgrid, winforms, syncfusion, programming examples, vb.net, c#] -->
```