```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_051.jpeg
document_name: chart
page_number: 051
page_id: chart#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:18:18Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the creation and management ofPopulationData class in Windows Forms.
- Highlights the use of properties and constructors in object-oriented programming.
- Provides examples in both C# and VB.NET syntaxes.

## Content

### PopulationData Class

The PopulationData class is designed to store and manage data related to city names and their respective populations. Below is the implementation in both C# and VB.NET.

#### C# Implementation

```csharp
{
    private string city;

    public string City
    {
        get { return city; }
        set { city = value; }
    }

    private double population;

    public double Population
    {
        get { return population; }
        set { population = value; }
    }

    public PopulationData(string city, double population)
    {
        this.city = city;
        this.population = population;
    }
}
```

#### VB.NET Implementation

```vb
[VB.NET]

Class PopulationData
    Private m_city As String

    Public Property City() As String
        Get
            Return m_city
        End Get
        Set(ByVal value As String)
            m_city = value
        End Set
    End Property
End Class
```

## API Reference

### Namespace
- `System`
- `System.Collections.Generic`
- `System.Text`

### Class Members
- **`City`**
  - Type: `string`
  - Description: Represents the name of the city.
  - Getter: Retrieves the city name.
  - Setter: Assigns a new city name.

- **`Population`**
  - Type: `double`
  - Description: Represents the population of the city.
  - Getter: Retrieves the population value.
  - Setter: Assigns a new population value.

- **`PopulationData (Constructor)`**
  - Parameters:
    - `string city`: The name of the city.
    - `double population`: The population of the city.
  - Description: Initializes a new instance of the PopulationData class with the specified city name and population.

## Code Examples

### Example: Creating and Using PopulationData

#### C# Example
```csharp
PopulationData cityData = new PopulationData("New York", 8537673);
Console.WriteLine("City: " + cityData.City); // Output: City: New York
Console.WriteLine("Population: " + cityData.Population); // Output: Population: 8537673
cityData.City = "Los Angeles";
cityData.Population = 3971883;
Console.WriteLine("Updated City: " + cityData.City); // Output: Updated City: Los Angeles
Console.WriteLine("Updated Population: " + cityData.Population); // Output: Updated Population: 3971883
```

#### VB.NET Example
```vb
Dim cityData As New PopulationData("New York", 8537673)
Console.WriteLine("City: " & cityData.City) ' Output: City: New York
Console.WriteLine("Population: " & cityData.Population) ' Output: Population: 8537673
cityData.City = "Los Angeles"
cityData.Population = 3971883
Console.WriteLine("Updated City: " & cityData.City) ' Output: Updated City: Los Angeles
Console.WriteLine("Updated Population: " & cityData.Population) ' Output: Updated Population: 3971883
```

## Page-level Navigation/TOC
- Essential Chart for Windows Forms
  - PopulationData Class
    - C# Implementation
    - VB.NET Implementation
  - API Reference
    - Class Members
  - Code Examples

### Cross References
- See also: [Essential Chart Documentation](#)
- [Windows Forms Programming Guide](#)

## RAG Annotations
<!-- tags: [chart, windows forms, object-oriented-programming, population-data, namespaces, classes, properties, methods] keywords: [PopulationData, City, Population, constructor, getter, setter, C#, VB.NET] -->
```
