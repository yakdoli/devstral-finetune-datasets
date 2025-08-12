```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_099.jpeg
document_name: tools
page_number: 099
page_id: tools#page_099
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:20:19Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```vb.net
Imports Syncfusion.Runtime.Serialization
Imports System.IO
Imports System.Xml
Imports Microsoft.Win32
Imports Syncfusion.Windows.Forms.Tools
```

### Declaring Instances of RegistryKey and MemoryStream Classes

#### C#

```csharp
RegistryKey rootKey;
private string selRad;
private MemoryStream memstream;
```

#### VB.NET

```vb.net
Private rootKey As RegistryKey
Private selRad As String
Private memstream As MemoryStream
```

### Loading the Form and Handling State Persistence

#### C#

```csharp
private void Form1_Load(object sender, System.EventArgs e)
{
    // Get the path of subKey.
    rootKey = Registry.CurrentUser.OpenSubKey("Config");
    // Retrieve the data associated with the subKey.
    selRad = (string)rootKey.GetValue("PersistType");
    if (selRad == null) selRad = "XML";
    AppStateSerializer app = GetSerializer(selRad);
    if (app != null)
    {
        // Retrieve the saved layout state of CommandBar objects using AppStateSerializer class.
        this.commandBarController1.LoadCommandBarState(app);
    }
}
```

#### VB.NET

```vb.net
Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    ' Code to be added as per the context.
End Sub
```

## API Reference

### Properties and Methods
- **commandBarController1.LoadCommandBarState(app):** Loads the saved layout state of CommandBar objects.
- **Registry.CurrentUser.OpenSubKey("Config"):** Opens a subkey in the current user registry hive.
- **rootKey.GetValue("PersistType"):** Retrieves the value associated with the "PersistType" key.

## Code Examples

### C#

```csharp
// Example of loading command bar state
private void Form1_Load(object sender, EventArgs e)
{
    rootKey = Registry.CurrentUser.OpenSubKey("Config");
    selRad = (string)rootKey.GetValue("PersistType");
    if (selRad == null) selRad = "XML";
    AppStateSerializer app = GetSerializer(selRad);
    if (app != null)
    {
        this.commandBarController1.LoadCommandBarState(app);
    }
}
```

### VB.NET

```vb.net
' Example of loading command bar state
Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    rootKey = Registry.CurrentUser.OpenSubKey("Config")
    selRad = CType(rootKey.GetValue("PersistType"), String)
    If selRad Is Nothing Then selRad = "XML"
    Dim app As AppStateSerializer = GetSerializer(selRad)
    If app IsNot Nothing Then
        Me.commandBarController1.LoadCommandBarState(app)
    End If
End Sub
```

## Cross References

- **Registry Settings:** Chapter on managing application settings.
- **CommandBar State Persistence:** Section on saving and restoring CommandBar layouts.

<!-- tags: [WinForms, RegistryKey, MemoryStream, AppStateSerializer, CommandBar, StatePersistence, Evergreen, 11.4.0.26] keywords: [registry, memory stream, state persistence, command bar, form load, serialization, xml, config key, app state] -->
```