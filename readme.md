# Object-oriented programming

## Abstraction
- Abstraction is a process where you show only “relevant” data and “hide” unnecessary details of an object from the user.

```
A car in itself is a well-defined object, which is composed of several other smaller objects like a gearing system, steering mechanism, engine, which are again have their own subsystems. 
But for humans car is a one single object.
```

## Encapsulation

The idea of encapsulation is to keep classes separated and prevent them from having tightly coupled with each other.

- Binding the data with the code that manipulates it.
- It keeps the data and the code safe from external interference

Similarly, same concept of encapsulation can be applied to code. Encapsulated code should have following characteristics:

- Everyone knows how to access it.
- Can be easily used regardless of implementation details.
- There shouldn’t any side effects of the code, to the rest of the application.

```
A example of encapsulation is the class of java.util.Hashtable. User only knows that he can store data in the form of key/value pair in a Hashtable and that he can retrieve that data in the various ways. But the actual implementation like, how and where this data is actually stored, is hidden from the user. User can simply use Hashtable wherever he wants to store Key/Value pairs without bothering about its implementation.
Same as Dict() in Python etc...
```

## Inheritance

A class that is used as the basis for inheritance is called a superclass or base class. A class that inherits from a superclass is called a subclass or derived class. The terms parent class and child class are also acceptable terms to use respectively. A child inherits visible properties and methods from its parent while adding additional properties and methods of its own.

- Inheritance is the mechanism by which an object acquires the some/all properties of another object.
- It supports the concept of hierarchical classification.

## Polymorphism
Polymorphism means to process objects differently based on their data type.
In other words it means, one method with multiple implementation, for a certain class of action. And which implementation to be used is decided at runtime depending upon the situation (i.e., data type of the object)
This can be implemented by designing a generic interface, which provides generic methods for a certain class of action and there can be multiple classes, which provides the implementation of these generic methods.

> __Overloading__ in simple words means more than one method having the same method name that behaves differently based on the arguments passed while calling the method. This called static because, which method to be invoked is decided at the time of compilation

> __Overriding__ means a derived class is implementing a method of its super class. The call to overriden method is resolved at runtime, thus called runtime polymorphism

# SOLID

## S — Single Responsibility Principle(S.R.P)
- A class should have one, and only one, reason to change.

## O — Open-Closed Principle
- You should be able to extend a class’s behavior, without modifying it.

This principle is the foundation for building code that is maintainable and reusable.
Open for extension
Closed for modification

## L — Liskov Substitution Principle
- Derived classes must be substitutable for their base classes.

What is wanted here is something like the following substitution property: If
for each object o1 of type S there is an object o2 of type T such that for all
programs P defined in terms of T, the behavior of P is unchanged when o1 is
substituted for o2 then S is a subtype of T.

When we are using abstraction(Open-Closed Principle), we want the methods to behave the same for each derived class, and not differently.

## I — Interface Segregation Principle
- Make fine grained interfaces that are client specific.
Clients should not be forced to implement interfaces they do not use.

By breaking down interfaces, we favor Composition instead of Inheritance, and Decoupling over Coupling. We favor composition by separating by roles(responsibilities) and Decoupling by not coupling derivative classes with unneeded responsibilities inside a monolith.

## D — Dependency Inversion Principle
- Depend on abstractions, not on concretions.

A. High level modules should not depend upon low level modules. Both should depend upon abstractions.

B. Abstractions should not depend upon details. Details should depend upon abstractions.

By depending on higher-level abstractions, we can easily change one instance with another instance in order to change the behavior. Dependency Inversion increases the reusability and flexibility of our code.

# DRY (Don`t Repeat Yourself)
Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

# YAGNI (You Ain’t Gonna Need It)
- Always implement things when you actually need them, never when you just foresee that you may need them.

In some ways, you can think of YAGNI as being similar to Just-In-Time manufacturing.  Rather than ordering a bunch of parts based on what you think you might need, wait for actual customer orders and ensure your process is lean enough that you can pull orders through you supply chain quickly enough to satisfy your customers. 
Remember, features are expensive, both to develop and maintain, and for users to learn and navigate around.  Features that aren’t actually necessary are a huge source of waste.
> “The cheapest, fastest, and most reliable components of a computer system are those that aren’t there.” – Gordon Bell

# KISS (Keep it Simple, Stupid)-PEP20
The more complex something is, the more ways there are for it to fail, and the more difficult it is to explain to someone else who needs to understand it. 

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

-PEP20
```

# Code reuse

# Extensibility

# Tools

## Testing

- WebTest(http://webtest.readthedocs.io)
- pytest and Tox

## Documentation

- The Sphinx tool (http://www.sphinx-doc.org/)
- ReadTheDocs (RTD) (https://docs.readthedocs.io )
- Coveralls (https://coveralls.io/).

## CI/CD

- Travis-CI (https://travis-ci.org/)