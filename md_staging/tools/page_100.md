```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_100.jpeg
document_name: tools
page_number: 100
page_id: tools#page_100
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:20:39Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```vb
' Get the path of subKey.
rootKey = Registry.CurrentUser.OpenSubKey("Config")
' Retrieve the data associated with the subKey.
selRad = CStr(rootKey.GetValue("PersistType"))
If selRad Is Nothing Then
    selRad = "XML"
End If
Dim app As AppStateSerializer = GetSerializer(selRad)
If Not app Is Nothing Then
' Retrieve the saved layout state of CommandBar objects using AppStateSerializer class.
    Me.commandBarController1.LoadCommandBarState(app)
End If
End Sub
```

## Serialization can be accomplished using the `AppStateSerializer` class.

### [C#]

```csharp
private AppStateSerializer GetSerializer(string str)
{
    AppStateSerializer state;
    switch (str)
    {
        //XML file is used to read/write the layout information
        case "XML":
            state = new AppStateSerializer(SerializeMode.XMLFile, @"C:\StateInfo");
            break;

        //Binary file is used to read/write the layout information
        case "Binary Format":
            state = new AppStateSerializer(SerializeMode.BinaryFile, @"C:\StateInfo");
            break;

        //Win32 windowsRegistry is used to read/write the layout information
        case "Windows Registry":
            Microsoft.Win32.RegistryKey rootKey = Microsoft.Win32.Registry.CurrentUser.CreateSubKey(@"Software\CommandBar\State");
            state = new AppStateSerializer(SerializeMode.WindowsRegistry, rootKey);
            break;

        //Isolated storage is used to read/write the layout information
        case "Isolated Storage":
            state = new 
    }
}
```

<!-- tags: [Syncfusion, Winforms, serialization, AppStateSerializer, CommandBar, registry] keywords: [AppStateSerializer, SerializeMode, XMLFile, binary format, Windows Registry, isolated storage] -->
```