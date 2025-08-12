```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_106.jpeg
document_name: Olap Common
page_number: 106
page_id: Olap Common#page_106
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:13Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Connect WCF Service by an additional Binding Type in Silverlight application.
- OLAP Silverlight controls can be bound to BasicHttpBinding support.
- Incorrect specification of endpoint address will lead to Initialize Component Error.
- Include BasicHttpBinding configuration in Web.Config file for proper service binding.

## Content

### 5.21 Connect WCF Service by an additional Binding Type in Silverlight application

OLAP Silverlight controls can be bound to BasicHttpBinding support.

**Note:** Incorrect specification of endpoint address will lead to Initialize Component Error. The endpoint address should be set with respect to the type of bindings.

#### Use case Scenario

User can create Web service using the BasicHttpBinding feature and bind the service to OLAP Silverlight controls.

#### BasicHttpBinding

The following are steps to create a BasicHttpBinding:

Include the Basic Http Binding and Service endpoint address in the Web.Config file as given in the following code:

```xml
[XML]
<!-- <Bindings> -->
<bindings>
    <basicHttpBinding>
        <binding name="binaryHttpBinding" maxBufferSize="2147483647" maxReceivedMessageSize="2147483647">
            <readerQuotas maxDepth="2147483647" />
            <security mode="None" />
        </binding>
    </basicHttpBinding>
</bindings>

<!-- <Endpoint Address> -->
<services>
    <service behaviorConfiguration="Services.OlapManagerBehavior" name="Services.OlapManager">
        <endpoint address="basic" binding="basicHttpBinding" bindingConfiguration="binaryHttpBinding" contract="Syncfusion.OlapSilverlight.Manager.IOlapDataProvider" />
    </service>
</services>
```

### Page-level Navigation/TOC (if applicable)
- Connect WCF Service by an additional Binding Type in Silverlight application

## Cross References
- See also: BasicHttpBinding, OLAP Silverlight controls, Web.Config configuration

<!-- tags: [product, module, control, api, version?] keywords: [unclear] -->
```