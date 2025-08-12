```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_087.jpeg
document_name: Olap Common
page_number: 087
page_id: Olap Common#page_087
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:08Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
End Function
Public Function ExecuteOlapReportWithTotalCount(ByVal report As OlapReport) As Syncfusion.OlapSilverlight.Common.SerializableDictionary(Of String, Object)
    Dim dict As
Syncfusion.OlapSilverlight.Common.SerializableDictionary(Of String, Object) =
    Me._dataManager.ExecuteOlapReportWithTotalCount(report)
    Me._dataManager.DataProvider.CloseConnection()
    Return dict
End Function
#End Region
#End Class
```

3. Include the custom binding and the service endpoint address in the Web.Config file.

## Web.Config

```xml
<!-- Binding -->
<bindings>
    <customBinding>
        <binding name="binaryHttpBinding">
            <binaryMessageEncoding/>
            <httpTransport maxReceivedMessageSize="2147483647"/>
        </binding>
    </customBinding>
</bindings>

<!-- Endpoint Address -->
<services>
    <service name="SilverlightApplication1.Web.OlapManager">
        <endpoint address="binary" binding="customBinding" bindingConfiguration="binaryHttpBinding" contract="Syncfusion.OlapSilverlight.Management.IOlapDataProvider"/>
    </service>
</services>
```

### 5.7 Connect WCF Service in Silverlight application

The user can connect the above WCF service using Channel Factory by CustomBinding (Or BasicHttpBinding) and End Point Address values.

The below code snippet demonstrates how to connect the WCF service:

#### C#

```csharp
Binding customBinding = new CustomBinding(new BinaryMessageEncodingBindingElement(), new HttpTransportBindingElement { MaxReceivedMessageSize = 2147483647 });
EndpointAddress address = new EndpointAddress(new Uri(App.Current.Host.Source.ToString() + "../../Services/OlapManager.svc/binary"));
ChannelFactory<IOlapDataProvider> clientChannel = new ChannelFactory<IO
```

<!-- tags: [Syncfusion Winforms, WCF Service, Silverlight, CustomBinding, BasicHttpBinding, ChannelFactory, OlapDataProvider, OlapReport, SerializableDictionary] keywords: [WCF, Silverlight, CustomBinding, BinaryMessageEncoding, HttpTransportBinding, MaxReceivedMessageSize, EndPointAddress, ChannelFactory, IOlapDataProvider, OlapReport, SerializableDictionary, ServiceAddress, MaxFileSize] -->
```