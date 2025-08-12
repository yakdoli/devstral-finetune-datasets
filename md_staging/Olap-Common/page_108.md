```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_108.jpeg
document_name: Olap Common
page_number: 108
page_id: Olap Common#page_108
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:03Z
fidelity: lossless
-->

## Essential OlapCommon

### Initialize Connection in VB

```vb
Private Sub InitializeConnection()
    Dim basicHttpBinding As System.ServiceModel.Channels.Binding = New BasicHttpBinding(BasicHttpSecurityMode.None With {.MaxReceivedMessageSize = 2147483647})
    'Address for Basic HTTP binding in corresponding Web configuration file
    Dim address As EndpointAddress = New EndpointAddress(New Uri(App.Current.Host.Source & "../../OlapManager.svc/basic"))
    Dim clientChannel As ChannelFactory(Of IOlapDataProvider) = New ChannelFactory(Of IOlapDataProvider)(basicHttpBinding, address)
    DataProvider = clientChannel.CreateChannel()
End Sub
```

### Retrieve the MDX Query of a CurrentReport

The MDX query of a current report is used to display data in Grid/Chart control and it can be retrieved by calling the `GetMdxQuery()` method.

The following code explains how to retrieve MDX Query from the OlapDataManager:

#### In C#

```csharp
olapDataManager.GetMDXQuery();
```

#### In VB

```vb
olapDataManager.GetMDXQuery()
```

#### In Silverlight

```csharp
[C#]
string currentMdxQuery = null;
//// Invoke the service call to retrieve the MDX query from the Server based on current report.
_olapDataManager.GetMdxQuery(_olapDataManager.CurrentReport);
_olapDataManager.MdxQueryObtained += () => {
    //// MDX Query retrieved.
    currentMdxQuery = _olapDataManager.CurrentReport.CurrentMdxQuery;
};
```

## Code Examples

### Initializing Connection in C#

```csharp
[C#]
Private Sub InitializeConnection()
    Dim basicHttpBinding As System.ServiceModel.ServiceModel.HttpBinding = New BasicHttpBinding (BasicHttpSecurityMode.None With (.MaxReceivedMessageSize = 2147483647))
    ' Address for Basic HTTP binding in corresponding Web configuration file
    Dim address As EndpointAddress = New EndpointAddress (New Uri(". /APP. Current. Source & " "" / / / / OIapManager.svc/basic"))
    Dim clientChannel As ChannelFactory(Of IOlapDataProvider) = New ChannelFactory(Of IOlapDataProvider) (basicHttpBinding, address)
    DataProvider = clientChannel.CreateChannel()
End Sub
```

### Retrieving MDX Query from OlapDataManager

#### Sample Code

```csharp
[C#]
string currentMdxQuery = null;
//// Invoke the service call to retrieve the MDX query from the Server based on current report.
_olapDataManager.GetMdxQuery(_olapDataManager.CurrentReport);
_olapDataManager.MdxQueryObtained += () => {
    //// MDX Query retrieved.
    currentMdxQuery = _olapDataManager.CurrentReport.CurrentMdxQuery;
};
```

<!-- tags: [Olap Common, WinForms, MDX Query, OlapDataManager, Silverlight, Syncfusion Winforms] keywords: [MDX Query, OlapDataManager, GetMdxQuery, InitializeConnection, ChannelFactory, DataProvider, Silverlight, WCF] -->
```