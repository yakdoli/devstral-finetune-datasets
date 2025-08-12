```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_819.jpeg
document_name: grid
page_number: 819
page_id: grid#page_819
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:42:25Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to set up a `ListltemReference` relation between a data table and a strong typed collection.
- Explains the difference between `ForeignKeyReference` and `ListltemReference`.
- Provides steps to create the `Countries` collection and its associated `Country` objects.
- Includes an example of defining a relation descriptor and adding it to the main data table.

## Content

### Note: For more details, refer the following browser sample:
```plaintext
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Relations And Hierarchy\Employee Territory Order Demo
```

#### 4.3.4.3.5.4 Listltem Reference Relation

**ListltemReference** is an object reference relation for looking up values from a strong typed collection. Like `ForeignKeyReference`, it is also an n:1 relation where multiple records in the parent table can reference the same record in the related table. One difference between the `ForeignKeyReference` and `ListltemReference` is that the former uses a key to look up the values where as the later uses an object to look up the values in a nested collection.

#### Steps to setup ListltemReference relation

This section sets up a `ListltemReference` relation between a data table and the collection **Countries**. The data table represents the Parent Table of the relation and the **Countries** collection serves as the related child list where in the values can be looked up using an object of the child list. The collection derives from `ArrayList` in which every item is a `Country` object having two properties, `CountryCode` and `Name`. It also defines a method named `CreateDefaultCollection()` that returns an instance of itself populated with a set of values.

This relation kind can be set up by defining a relation descriptor with its attributes carrying the relation details and adding this descriptor to the Relations collection of the main table.

The following steps demonstrate this process.

#### 1. Create a collection named **Countries** in which each entry stores a **Country** object.

##### Code Example

```csharp
[C#]

// Countries Collection.
[Serializable]
public class CountriesCollection : ArrayList
{
    public new Country this[int index]
    {
        
```

## API Reference (if applicable)
- **ListltemReference**: An object reference relation used for looking up values from a strong typed collection.
- **Country**: Represents a country object with properties `CountryCode` and `Name`.
- **CountriesCollection**: A custom collection class deriving from `ArrayList` to store `Country` objects.

### Code Examples (multi-language supported)

#### C# Code Example for Countries Collection
```csharp
[C#]

// Countries Collection.
[Serializable]
public class CountriesCollection : ArrayList
{
    public new Country this[int index]
    {
        
```

### Cross References
- Refer to the Employee Territory Order Demo for a practical example implementation.

<!-- tags: [Syncfusion, WinForms, Grid, ListltemReference, Relation] keywords: [Countries, CountryCollection, Country, ListltemReference, ArrayList, CreateDefaultCollection] -->
```