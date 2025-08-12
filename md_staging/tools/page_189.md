```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_189.jpeg
document_name: tools
page_number: 189
page_id: tools#page_189
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:21:15Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains the use of `AutoSizeMode` in resizing user interface elements.
- Demonstrates implementing auto-sizing in C# and VB.NET.
- Describes the concept of **Dock State Persistence** and how it can be saved in various formats.

## Content

### AutoSizeMode

| AutoSizeMode | Description |
|--------------|-------------|
|      | size itself to fit its contents. |
| AutoSizeMode | Specifies the mode by which the user interface element automatically resizes itself. |

#### C#

```csharp
this.dockingClientPanel1.AutoSize = true;
this.dockingClientPanel1.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
```

#### VB.NET

```vbnet
Me.dockingClientPanel1.AutoSize = True
Me.dockingClientPanel1.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink
```

### 3.4.3.7.2 Dock State Persistence

The docking behavior can be saved in the following formats:

- Binary Format
- XML Format
- IsolatedStorage medium
- MemoryStream
- PersistState property

The docking windows framework has a fully built-in serialization feature that provides automatic serialization of the form's docking state. In addition to this automatic dock state persistence during application termination and start, multiple intermediate docking states can be saved or loaded anytime using the programmatic API. The serialization mechanism is implemented using the standardized `Syncfusion.Windows.Forms.AppStateSerializer` component that acts as a central coordinator of all the Essential Tools components and provides the option to read/write to different media such as the default Isolated Storage, XML file, XML stream, Binary file, Binary stream and the Windows Registry.

#### Persisting Dock State in default storage

The dock state of a control can be persisted by setting the `PersistState` property of Docking manager. This information is stored in the Isolated storage.

| DockingClientPanel Property | Description |
|-----------------------------|-------------|
| PersistState               | Gets or sets a value indicating whether the application's docking window state should be |

## API Reference

### Properties
- **PersistState**: Indicates whether the application's docking window state should be persisted.

## Code Examples

### Auto-Sizing Example in C#

```csharp
this.dockingClientPanel1.AutoSize = true;
this.dockingClientPanel1.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
```

### Auto-Sizing Example in VB.NET

```vbnet
Me.dockingClientPanel1.AutoSize = True
Me.dockingClientPanel1.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink
```

## RAG Annotations
<!-- tags: [Dock State Persistence, AutoSizeMode, Syncfusion Winforms, Serialization, AppStateSerializer, IsolatedStorage, XML, Binary File] keywords: [AutoSizeMode, GrowAndShrink, PersistState, DockingClientPanel, AppStateSerializer, IsolatedStorage, Windows Forms, Syncfusion] -->
```