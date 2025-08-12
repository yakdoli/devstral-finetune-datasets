```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_119.jpeg
document_name: Olap Common
page_number: 119
page_id: Olap Common#page_119
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:49Z
fidelity: lossless
-->

### Essential OlapCommon

The `Essential OlapCommon` namespace provides essential methods to interact with OLAP cubes and their schemas. Below are the function definitions that demonstrate how to retrieve various components of an OLAP cube:

```vb
    Public Function GetChildMembers(ByVal memberUniqueName As String, ByVal cubeName As String) As MemberCollection
        Throw New NotImplementedException()
    End Function

    Public Function GetCubeSchema(ByVal cubeName As String) As CubeSchema
        Throw New NotImplementedException()
    End Function

    Public Function GetCubes() As CubeInfoCollection
        Throw New NotImplementedException()
    End Function

    Public Function GetLevelMembers(ByVal levelUniqueName As String, ByVal cubeName As String) As MemberCollection
        Throw New NotImplementedException()
    End Function

#End Region
End Class
```

## Include Custom Binding in Web.Config

11. Include the custom binding and the service endpoint address in the Web.Config file under the ServiceModel section. The following is an example configuration snippet:

```xml
[Web.Config]
<!--Binding-->
<bindings>
    <customBinding>
        <binding name="binaryHttpBinding">
            <binaryMessageEncoding />
            <httpTransport maxReceivedMessageSize="2147483647" />
        </binding>
    </customBinding>
</bindings>
```

This configuration ensures that the service can handle the required bindings and endpoint configurations effectively.

## API Reference

### Methods

#### GetChildMembers
```vb
Public Function GetChildMembers(ByVal memberUniqueName As String, ByVal cubeName As String) As MemberCollection
```
- **Parameters**:
  - `memberUniqueName`: The unique name of the member.
  - `cubeName`: The name of the cube.

#### GetCubeSchema
```vb
Public Function GetCubeSchema(ByVal cubeName As String) As CubeSchema
```
- **Parameters**:
  - `cubeName`: The name of the cube.

#### GetCubes
```vb
Public Function GetCubes() As CubeInfoCollection
```

#### GetLevelMembers
```vb
Public Function GetLevelMembers(ByVal levelUniqueName As String, ByVal cubeName As String) As MemberCollection
```
- **Parameters**:
  - `levelUniqueName`: The unique name of the level.
  - `cubeName`: The name of the cube.

## Code Examples

### Web.Config Configuration Example
```xml
<bindings>
    <customBinding>
        <binding name="binaryHttpBinding">
            <binaryMessageEncoding />
            <httpTransport maxReceivedMessageSize="2147483647" />
        </binding>
    </customBinding>
</bindings>
```

### VB.NET Example
```vb
Public Function GetCubeSchema(cubeName As String) As CubeSchema
    Dim cubeSchema As CubeSchema
    ' Implementation logic here
    Return cubeSchema
End Function
```

## Conclusion

This section provides guidance on integrating essential OLAP functionalities and configuring custom bindings in a Web.Config file. The methods outlined above are fundamental for interacting with OLAP cubes and their schema information.

<!-- tags: [Syncfusion, WinForms, OlapCommon, Web.Config, binding, OLAP, cube] keywords: [GetChildMembers, GetCubeSchema, GetCubes, GetLevelMembers, customBinding, binaryHttpBinding, maxReceivedMessageSize] -->
```