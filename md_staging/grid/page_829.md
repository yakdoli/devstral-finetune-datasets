```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_829.jpeg
document_name: grid
page_number: 829
page_id: grid#page_829
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:42:23Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
{
    if (f3 != value)
    {
        f3 = value;
        RaisePropertyChanged("Field3");
    }
}
```

```csharp
void RaisePropertyChanged(string name)
{
    if (PropertyChanged != null)
        PropertyChanged(this, new PropertyChangedEventArgs(name));
}
```

```csharp
public event PropertyChangedEventHandler PropertyChanged;
```
<!-- tags: [winforms, essentialgrid, propertychanged, event, bindings, synchronization] keywords: [winforms, essentialgrid, propertychanged, RaisePropertyChanged, EventArgs] -->
```