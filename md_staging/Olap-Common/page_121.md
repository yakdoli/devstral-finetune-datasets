```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_121.jpeg
document_name: Olap Common
page_number: 121
page_id: Olap Common#page_121
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:23:05Z
fidelity: lossless
-->

# Essential Olap Common

## Content

### Initializing the Service Connection

#### C#

```csharp
Binding new BinaryMessageEncodingBindingElement(), new HttpTransportBindingElement { MaxReceivedMessageSize = 2147483647 };
EndpointAddress address = new EndpointAddress(new Uri(App.Current.Host.Source + "../../OlapManager.svc/binary"));
ChannelFactory<IOLapDataProvider> clientChannel = new ChannelFactory<IOLapDataProvider>(customBinding, address);
DataProvider = clientChannel.CreateChannel();
```

#### VB

```vb
Private Sub InitializeConnection()
    Dim customBinding As System.ServiceModel.Channels.Binding = New CustomBinding(New BinaryMessageEncodingBindingElement(), New HttpTransportBindingElement With {.MaxReceivedMessageSize = 2147483647})
    Dim address As EndpointAddress = New EndpointAddress(New Uri(App.Current.Host.Source & "../../OlapManager.svc/binary"))
    Dim clientChannel As ChannelFactory(Of IOLapDataProvider) = New ChannelFactory(Of IOLapDataProvider)(customBinding, address)
    DataProvider = clientChannel.CreateChannel()
End Sub
```

### Creating the Report

17. **Create the Report.**

For creating reports, there is a report object called `OlapReport`. The `OlapReport` object contains CategoricalItems, SeriesItems, SlicerItems, and FilterItems.

The `OlapReport` is associated with the `OlapDataManager` as the current report property. When a report is set to the current report, an event triggers, and the control renders based on the current report that is set.

### Binding the Data to OlapGridData

18. **Bind the data to OlapGridData.**

```csharp
private void MainPage_Loaded(object sender, RoutedEventArgs e)
{
    // Initialize the service connection.
    this.InitializeConnection();
    // Instantiating the OlapDataManager.
    OlapDataManager m_OlapDataManager = new OlapDataManager();
}
```

## Cross References

See also:
- [OlapReport](#OlapReport)
- [OlapDataManager](#OlapDataManager)

<!-- tags: [olap, report, datamanagement, wcf, syncfusion] keywords: [OlapReport, OlapDataManager, InitConnection, BinaryMessageEncodingBindingElement, HttpTransportBindingElement, DataProvider, Report, SeriesItems, FilterItems] -->
```