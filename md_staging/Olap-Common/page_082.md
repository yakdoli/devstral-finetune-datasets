```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_082.jpeg
document_name: Olap Common
page_number: 082
page_id: Olap Common#page_082
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:44Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Add WCF Service (from the installed templates) in to the Web project.
- Inherit the newly added WCF service with `IOLapDataProvider` and explicitly implement the `IOLapDataProvider`.
- The connection to the database is done with the help of WCF service.
- The service has to be created and instantiated as described below:
- The WCF Service has to implement the `IOLapDataProvider` interface that requires the `OlapDataProvider` which can be instantiated by passing the connection string.

## Content

### Creating OLAP WCF Service in Web Project

The code snippet below explains how to create OLAP WCF service in Web project:

```csharp
[AspNetCompatibilityRequirements(RequirementsMode = AspNetCompatibilityRequirementsMode.Allowed)]
[ServiceBehavior(IncludeExceptionDetailInFaults = true)]
public class OlapManager : IOLapDataProvider
{
#region Private variables
    private readonly OlapDataProvider _dataManager;
#endregion

#region Constructor
    /// <summary>
    /// Initializes a new instance of the <see cref="OlapManager"/>
    /// class.
    /// </summary>
    public OlapManager()
    {
        _dataManager = new OlapDataProvider("DataSource=localhost;Initial CatalogAdventure Works DW");
    }
#endregion

#region IOLapDataProvider Members

### IOLapDataProvider Members

#### ExecuteOlapReportWithLevelTypeAll Method

```csharp
    public CellSet ExecuteOlapReportWithLevelTypeAll(OlapReport report, bool showLevelTypeAll)
    {
        CellSet cellSet =
            _dataManager.ExecuteOlapReportWithLevelTypeAll(report, showLevelTypeAll);
        _dataManager.DataProvider.CloseConnection();
        return cellSet;
    }
```

#### Summary

```csharp
/// <summary>
/// Gets the MDX query.
/// </summary>
/// <param name="report">The report.</param>
/// <returns></returns>
```
```  
<!-- tags: [Essential OlapCommon, WCF Service, IOLapDataProvider, OlapDataProvider, OLAP WCF Service, Web project, C#] keywords: [OlapReport, CellSet, showLevelTypeAll, CloseConnection, MDX query, Adventure Works DW] -->
```