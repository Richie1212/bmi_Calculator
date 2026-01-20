
BMI Calculator Application

A Streamlit-based web application that calculates Body Mass Index (BMI) and provides
health status insights based on the calculated BMI value.

Module Overview:
    This application provides users with a simple and interactive interface to:
    - Input personal information (name, age, weight, height)
    - Calculate BMI using the standard formula: (weight in pounds * 703) / (height in inches)²
    - Receive categorized health status feedback based on BMI ranges
    - View BMI classification categories
    - Access application information and contact details

Features:
    - User-friendly input fields for personal data collection
    - Real-time BMI calculation and display with 2 decimal precision
    - BMI categorization with personalized health recommendations:
        * Underweight (BMI < 18.5)
        * Normal weight (BMI 18.5 - 24.9)
        * Overweight (BMI 25 - 29.9)
        * Obesity Class I (BMI 30 - 34.9)
        * Obesity Class II (BMI 35 - 39.9)
        * Obesity Class III (BMI ≥ 40)
    - Reference guide displaying all BMI categories
    - Reset functionality to clear all inputs
    - About section with application description
    - Contact information for user inquiries

Dependencies:
    - streamlit: Web application framework for building interactive data applications

Functions:
    - BMI Calculation: (weight * 703) / (height ** 2)

UI Components:
    - Title: "BMI Calculator"
    - Input Section: Two-column layout for efficient data entry
    - Results Section: Displays calculated BMI score
    - Category Report: Shows BMI classification and health recommendations
    - Reference Guide: Lists all BMI categories and ranges
    - Action Buttons: Reset, About, and Contact functionalities
    - Disclaimer: Medical advice notice with styled text

Disclaimer:
    This application provides general BMI calculations and should not be used as a
    substitute for professional medical advice. Users should consult healthcare
    professionals for personalized health assessments.

Author: richardsyeb23@gmail.com
Framework: Streamlit
