```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_690.jpeg
document_name: grid
page_number: 690
page_id: grid#page_690
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:34:41Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes the creation of a strongly typed collection using the CollectionBase class.
- Explains the implementation of Generic Collection for non-type-specific collections.
- Introduces .NET 2.0 framework's generic collections and their advantages.

## Content

### Figure 274: Creating a Strongly Typed Collection by using the CollectionBase Class

```markdown
| Products: 3 Items |
| --- | --- |
| ProductName | QuantityPerUnit |
| --- | --- |
| Chai | 10 boxes x 20 bags |
| Aniseed Syrup | 12 - 550 ml bottles |
| Sir Rodney's Marmalade | 30 gift boxes |
```

**Note**: For more details, refer the following browser sample:

```shell
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Custom Collections\Collection Base Demo
```

#### **4.3.4.2.3.4.2 Generic Collection**

This section deals with the implementation of **Generic Collection**. Generics refer to those classes, structure, methods, and interfaces that have place holders for the types they can contain or use. A generic collection class uses type parameters as place holders for the type of objects it stores, for the type of its fields, and the parameter types for its methods. The actual types are assigned to these place holders while creating the instances.

It provides a standard way to create a non-type-specific collection. Hence, we can get the immediate benefit of type safety without having to derive from a base collection type and implement type-specific members. Through generics, it is possible to have a single array class to store a list of Players or even a list of Products.

The .NET 2.0 framework provides a number of generic collections to work with. The generic collection classes have been defined in the `System.Collections.Generic` namespace. Some of them are listed below:

- **List\<T\>** is the generic version of `ArrayList` based on the generic interface `IList`.
- **BindingList\<T\>** is the generic collection based on `IBindingList`.
- **BindingListView\<T\>** is a generic collection based on `IBindingListView`.

where `T` is the placeholder for the type parameter.

## Code Examples

The following is an example of how to create and use a `List<T>`:

```csharp
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Create a list of Products
        List<Product> products = new List<Product>();

        // Add Products to the list
        products.Add(new Product { ProductName = "Chai", QuantityPerUnit = "10 boxes x 20 bags" });
        products.Add(new Product { ProductName = "Aniseed Syrup", QuantityPerUnit = "12 - 550 ml bottles" });
        products.Add(new Product { ProductName = "Sir Rodney's Marmalade", QuantityPerUnit = "30 gift boxes" });

        // Display the products
        foreach (var product in products)
        {
            Console.WriteLine($"Product Name: {product.ProductName}, Quantity Per Unit: {product.QuantityPerUnit}");
        }
    }
}

public class Product
{
    public string ProductName { get; set; }
    public string QuantityPerUnit { get; set; }
}
```

## API Reference

### List<T>
- **Namespace**: System.Collections.Generic
- **Usage**: Based on the generic interface `IList`.

### BindingList<T>
- **Namespace**: System.Collections.Generic
- **Usage**: Based on `IBindingList`.

### BindingListView<T>
- **Namespace**: System.Collections.Generic
- **Usage**: Based on `IBindingListView`.

## RAG Annotations

<!-- tags: [Syncfusion, Winforms, Generic Collection, .NET 2.0, CollectionBase, List<T>, BindingList<T>, BindingListView<T>, Strongly Typed Collection] keywords: [generic collections, type safety, non-type-specific collections, ArrayList, IBindingList, IBindingListView, Product, QuantityPerUnit] -->
```