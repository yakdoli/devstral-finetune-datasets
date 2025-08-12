```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_101.jpeg
document_name: tools
page_number: 101
page_id: tools#page_101
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:21:26Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```csharp
AppStateSerializer(SerializeMode.IsolatedStorage, "StateInfo", System.IO.IsolatedStorage.IsolatedStorageScope.User);
break;

default:
state = null;
break;
}
return (state);
```

```vb.net
[VB.NET]

Private Function GetSerializer(ByVal str As String) As AppStateSerializer
    Dim state As AppStateSerializer
    Select Case str

    ' XML file is used to read/write the layout information
    Case "XML"
        state = New AppStateSerializer(SerializeMode.XMLFile, "C:\StateInfo")

    ' Binary file is used to read/write the layout information
    Case "Binary Format"
        state = New AppStateSerializer(SerializeMode.BinaryFile, "C:\StateInfo")

    ' Win32 windowsRegistry is used to read/write the layout information
    Case "Windows Registry"
        Dim rootKey As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.CurrentUser.CreateSubKey("Software\CommandBar\State")
        state = New AppStateSerializer(SerializeMode.WindowsRegistry, rootKey)

    ' Isolated storage is used to read/write the layout information
    Case "Isolated Storage"
        state = New AppStateSerializer(SerializeMode.IsolatedStorage, "StateInfo", System.IO.IsolatedStorage.IsolatedStorageScope.User)
    Case Else
        state = Nothing
        End Select
    Return (state)
End Function
```

### Form Closing Event Example

8. In the Form Closing event, use the following code snippet.

```csharp
state.Save();
```

## Cross References
- **API Reference Section:** Function `AppStateSerializer` (serialized mode: IsolatedStorage, binaryFile, windowsRegistry, etc.)
- **Code Examples Section:** Refer to above code snippets for implementation details.

<!-- tags: [Syncfusion Winforms, Essential Tools, Form Closing Event, AppStateSerializer, IsolatedStorage, BinaryFile, WindowsRegistry, XMLFile] keywords: [serialize mode, state info, isolated storage, binary format, windows registry, XML file, layout information, form closing event, AppStateSerializer] -->
```