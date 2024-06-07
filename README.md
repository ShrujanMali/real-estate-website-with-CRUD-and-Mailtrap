# Real-estate-website-with-CRUD-and-Mailtrap

## Overview

This project is a web application initially developed as a blog application and then converted into a property listing platform using Flask. Users can list their properties for sale, rent, or purchase, and perform CRUD (Create, Read, Update, Delete) operations on their listings. Additionally, there is a "Contact Us" page where users can send inquiries, which are handled using the Mailtrap email service.


## Technology used
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,flask,github,vscode,git,bootstrap,js,html,css" />
  </a>
</p>


## Features

    Property Listings: Users can list properties by providing details such as title, address, email, description, owner, type of transaction (sell, rent, buy), property type (bungalow, shop, flat), and date posted.
    CRUD Operations: Users can create, view, update, and delete property listings.
    Contact Us Form: Users can submit inquiries with their name, email, address, and description. These inquiries are sent to the admin via Mailtrap.

## Detailed Functionality

1. Property Listings
  Users can fill out a form to list a property with the following details:
            Title
            Address
            Email
            Description
            Owner
            Transaction type (sell, rent, buy)
            Property type (bungalow, shop, flat)
            Date posted
        The properties are displayed in a list where each property can be viewed in detail, updated, or deleted.

2.    CRUD Operations
        Create: Fill out the form to add a new property listing.
        Read: View detailed information about each property.
        Update: Edit the details of an existing property listing.
        Delete: Remove a property listing from the database.

3. Contact Us Form
        Users can submit inquiries through the contact form with the following details:
            Name
            Email
            Address
            Description
        Upon submission, the inquiry is sent to the admin using the Mailtrap email service.
