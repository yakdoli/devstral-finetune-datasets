```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_120.jpeg
document_name: Olap Common
page_number: 120
page_id: Olap Common#page_120
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:57Z
fidelity: lossless
-->

# Essential OlapCommon

```xml
</bindings>
<!--Endpoint Address-->
<services>
  <service name="SilverlightApplication1.Web.OlapManager" >
    <endpoint address="binary" binding="customBinding" bindingConfiguration="binaryHttpBinding" contract="Syncfusion.OlapSilverlight.Manager.IOlapDataProvider" />
  </service>
</services>
```

## Setting Up the Service

12. Add the `System.ServiceModel` assembly as a reference for the Silverlight project.

13. Add the following namespace in MainPage.xaml.cs:

- System.ServiceModel
- System.ServiceModel.Channels
- Syncfusion.OlapSilverlight.Reports
- Syncfusion.Silverlight.Grid
- Syncfusion.OlapSilverlight.Manager
- Syncfusion.OlapSilverlight.Engine

14. Instantiate the service from MainPage.xaml.cs which is in the Silverlight Project.

15. Declare the `IOlapDataProvider` for service instantiation.

### Code Example

#### C#

```csharp
// Declaring the IOlapDataProvider for service instantiation.
IOlapDataProvider DataProvider = null;
```

#### VB

```vb
'Declaring the IOlapDataProvider for service instantiation.
Dim DataProvider As IOlapDataProvider = Nothing
```

16. Specify the custom binding and instantiate the `DataProvider` from the `ChannelFactory`.

### Code Example

#### C#

```csharp
private void InitializeConnection()
{
    System.ServiceModel.Channels.Binding customBinding = new CustomBi
    ...
}
```

## Copyright Notice

© 2013 Syncfusion. All rights reserved.
```