```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_190.jpeg
document_name: tools
page_number: 190
page_id: tools#page_190
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:22:04Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains the support for persisting dock state in the DockingManager.
- Describes the use of AppStateSerializer for serialization.
- Details the methods LoadDockState and SaveDockState for managing persisted states.

## Content

### DockingManager State Serialization

The DockingManager has built-in support for dock state serialization that can be enabled or disabled using the `PersistState` property. When the `PersistState` property is set to `True`, closing the form and hosting the docking windows will force the DockingManager to capture the current docking layout and serialize it using the Essential Studio `AppStateSerializer` serialization.

#### PersistState Property Example

```csharp
this.dockingManager1.PersistState = true;
```

```vb
Me.dockingManager1.PersistState = True
```

#### Serialization Mechanism

The default serialization option is isolated storage and the `System.IO.IsolatedStorage` routines normally store application-specific encrypted entries under the `'C:\Documents and Settings\[USER name]\Local Settings\Application Data\IsolatedStorage'` folder. All of the Essential Tools framework components use the `Syncfusion.Runtime.Serialization.AppStateSerializer` class in the Shared library for Read/Write. The `AppStateSerializer` is fully documented and can be initialized for different persistence mediums such as XML / Binary files, XML / Binary streams, and the Win32 Registry using its API.

#### Auto Serialization Implementation

The default auto serialization implementation for the DockingManager uses a single instance of the `AppStateSerializer` that you can access through the `AppStateSerializer.GetSingleton()` method and reinitialize if necessary. But this single reinitialization should be done within the application's `Main` method before the first instance gets a chance to be created. Another option would be to use a custom instance of the `AppStateSerializer` and pass this to application-level invocations of the DockingManager's `LoadDockState` / `SaveDockState` routines.

### LoadDockState and SaveDockState Methods

#### LoadDockState

| Methods                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| LoadDockState            | Reads the persisted dock state from the Isolated Storage.                |
| LoadDockState (Overloaded)| Reads a previously serialized dock state using the `AppStateSerializer` object. Parameter is, |

---

## API Reference

For additional information on the `AppStateSerializer` class, its methods, and detailed documentation, please refer to the Syncfusion documentation.

## Code Examples

Examples of how to use the `PersistState` property and the `LoadDockState` and `SaveDockState` methods can be found in the Syncfusion WinForms samples or documentation.

## See also
- Syncfusion Documentation
- `AppStateSerializer` Class
- Persisting Application State
- DockingManager Documentation

<!-- tags: [DockingManager, AppStateSerializer, Serialization, PersistState, LoadDockState, SaveDockState, WinForms, Syncfusion] keywords: [DockingManager, serialization, persist state, XML, binary files, isolated storage, SaveDockState, LoadDockState, AppStateSerializer] -->
```