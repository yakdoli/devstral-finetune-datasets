```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_306.jpeg
document_name: tools
page_number: 306
page_id: tools#page_306
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:05:59Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

The history list of AutoComplete control can be saved in the following formats:

- Binary Format
- XML Format
- IsolatedStorage medium
- MemoryStream
- PersistState property

The AutoComplete control has a fully built-in serialization feature that provides automatic serialization of the AutoComplete's history list. The serialization mechanism is implemented using the standardized `Syncfusion.Windows.Forms.AppStateSerializer` component that acts as a central coordinator for all the Essential Tools components and provides the option to read/write to different media such as the default Isolated Storage, XML file, XML stream, Binary file, Binary stream, and the Windows Registry.

### Persisting AutoComplete's data in default storage

The data of AutoComplete's control can be persisted by setting the `AutoSerialize` property to `true`. This information is stored in the Isolated storage.

| AutoComplete Property | Description |
|------------------------|-------------|
| AutoSerialize          | Specifies whether AutoComplete control can persist its data. |

**C#:**
```csharp
this.autoComplete1.AutoSerialize = true;
```

**VB.NET:**
```vb
Me.autoComplete1.AutoSerialize = True
```

The AutoComplete control has built-in support for serialization that can be enabled or disabled using the `AutoSerialize` property.

The default serialization option is Isolated storage and the `System.IO.IsolatedStorage` routines normally store application specific encrypted entries under the 'C:\Documents and Settings\[USER name]\Local Settings\Application Data\IsolatedStorage\' folder. All of the Essential Tools framework components use the `Syncfusion.Runtime.Serialization.AppStateSerializer` class in the Shared library for Read/Write. The `AppStateSerializer` is fully documented and can be initialized for different persistence mediums such as XML / Binary files, XML / Binary streams, and the Win32 Registry using its API.
```


<!-- tags: [syncfusion-sdk, winforms, autofcomplete, serialization, appstateserializer] keywords: [history list, persistence, isolated storage, binary format, xml format, state serializer, windows registry] -->
```