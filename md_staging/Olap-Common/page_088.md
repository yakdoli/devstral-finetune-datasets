```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_088.jpeg
document_name: Olap Common
page_number: 088
page_id: Olap Common#page_088
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:52Z
fidelity: lossless
-->

## Essential OlapCommon

```csharp
IolapDataProvider>(customBinding, address);
IOLapDataProvider _dataProvider = clientChannel.CreateChannel();
//////Sets the data provider (WCF Service connection) in OlapDataManager
_olapDataManager.DataProvider = _dataProvider;
```

```vb
Dim customBinding As Binding = New CustomBinding(New BinaryMessageEncodingBindingElement(), New HttpTransportBindingElement() With { _
    Key .MaxReceivedMessageSize = 2147483647 _
})
Dim address As New EndpointAddress(New Uri(App.Current.Host.Source.ToString() & 
    ".../.../.../Services/OlapManager.svc/binary"))
Dim clientChannel As New ChannelFactory(Of IOLapDataProvider)(customBinding, address)
Dim _dataProvider As IOLapDataProvider = clientChannel.CreateChannel()

'''Sets the data provider (WCF Service connection) in OlapDataManager
_olapDataManager.DataProvider = _dataProvider
```

## 5.8 Bind an OlapReport with OlapDataManager

Once the connection is established, you can create and bind the OlapReport to the manger by using any one of the following property and methods:

### Property:

- 1. CurrentReport

### Methods:

- 1. SetCurrentReport
- 2. LoadOlapDataManager
- 3. LoadReportDefinitionFile
- 4. LoadReportDefinitionFromStream

### Methods for Silverlight:

- 1. SetCurrentReport
- 2. LoadReportFromStream

The following code snippet will illustrate the binding of OlapReport using these methods with a sample OlapReport:

### Sample OlapReport

```csharp
[C#]
```

<!-- tags: [OlapCommon, OlapReport, OlapDataManager, Winforms] keywords: [Olap Report, Data Manager, WCF Service, Binding, Syncfusion, C#, VB] -->
```