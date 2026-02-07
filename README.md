# BMI Calculator Application

## Overview

A professional web application built with Streamlit that calculates Body Mass Index (BMI) and provides evidence-based health insights. The application offers an intuitive interface for users to assess their BMI category and receive personalized health recommendations.

**Live Application:** [https://bmimod.streamlit.app/](https://bmimod.streamlit.app/)

---

## Table of Contents

1. [Features](#features)
2. [Technical Specifications](#technical-specifications)
3. [BMI Categories](#bmi-categories)
4. [User Interface](#user-interface)
5. [Calculation Method](#calculation-method)
6. [Dependencies](#dependencies)
7. [Medical Disclaimer](#medical-disclaimer)
8. [Contact Information](#contact-information)

---

## Features

### Core Functionality
- **Real-time BMI calculation** with two-decimal precision
- **Personalized health status** categorization based on WHO standards
- **Interactive data entry** with user-friendly input validation
- **Comprehensive reference guide** displaying all BMI classification ranges
- **Reset functionality** for quick data clearing
- **Responsive design** optimized for desktop and mobile devices

### User Experience
- Clean, intuitive two-column layout for efficient data entry
- Instant feedback with color-coded health status indicators
- Educational content explaining BMI categories
- Professional styling with medical-grade accuracy
- Accessible interface following web accessibility standards

---

## Technical Specifications

### Framework
- **Streamlit:** Python-based web application framework for interactive data applications
- **Python:** Backend logic and calculation engine

### Architecture
- Single-page application (SPA) design
- Real-time state management
- Modular component structure
- Session-based data handling

---

## BMI Categories

The application classifies BMI results according to the following medical standards:

| Category | BMI Range | Health Implications |
|----------|-----------|---------------------|
| **Underweight** | < 18.5 | May indicate malnutrition or underlying health conditions |
| **Normal Weight** | 18.5 – 24.9 | Healthy weight range associated with lowest health risks |
| **Overweight** | 25.0 – 29.9 | Increased risk of cardiovascular disease and diabetes |
| **Obesity Class I** | 30.0 – 34.9 | Moderate risk of obesity-related health conditions |
| **Obesity Class II** | 35.0 – 39.9 | High risk of serious health complications |
| **Obesity Class III** | ≥ 40.0 | Very high risk; immediate medical consultation recommended |

### Personalized Recommendations

Each BMI category includes:
- Health status assessment
- Risk factor identification
- Actionable lifestyle recommendations
- Guidance on when to seek professional medical advice

---

## User Interface

### Input Section
**Two-Column Layout for Efficient Data Entry:**
- **Personal Information:**
  - Name (text input)
  - Age (numeric input)
- **Body Measurements:**
  - Weight in pounds (numeric input)
  - Height in inches (numeric input)

### Results Display
- **BMI Score:** Prominently displayed with two-decimal precision
- **Category Classification:** Clear indication of health status
- **Color-Coded Feedback:** Visual cues for quick interpretation
- **Health Recommendations:** Tailored advice based on BMI category

### Reference Section
- **BMI Categories Table:** Complete classification guide
- **Range Explanations:** Detailed descriptions of each category
- **Health Impact Information:** Evidence-based health implications

### Action Buttons
- **Calculate BMI:** Primary action button
- **Reset:** Clear all input fields
- **About:** Application information and methodology
- **Contact:** Developer contact details

---

## Calculation Method

### Standard BMI Formula

```
BMI = (Weight in pounds × 703) / (Height in inches)²
```

**Example Calculation:**
```
Weight: 150 lbs
Height: 65 inches (5'5")
BMI = (150 × 703) / (65 × 65)
BMI = 105,450 / 4,225
BMI = 24.97
Category: Normal Weight
```

### Input Validation
- Positive numeric values required for weight and height
- Range checks to ensure physiologically realistic inputs
- Error handling for invalid or missing data
- Automatic decimal rounding to two places

---

## Dependencies

### Required Libraries

```python
streamlit>=1.0.0
```

### Installation

```bash
pip install streamlit
```

### Running the Application

```bash
streamlit run bmi_calculator.py
```

---

## Medical Disclaimer

**Important Notice:**

This BMI Calculator is designed for **educational and informational purposes only**. It should not be used as a substitute for professional medical advice, diagnosis, or treatment.

### Limitations of BMI
- BMI does not account for muscle mass, bone density, or body composition
- May not be accurate for athletes, elderly individuals, or pregnant women
- Does not measure body fat distribution or overall health status
- Should be used as one indicator among many health metrics

### Medical Consultation
Users are strongly encouraged to consult with qualified healthcare professionals for:
- Personalized health assessments
- Weight management strategies
- Nutrition and exercise planning
- Diagnosis and treatment of medical conditions

**Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.**

---

## Contact Information

### Developer
**Author:** richardsyeb23@gmail.com

### Support
For technical issues, feature requests, or general inquiries:
- **Email:** richardsyeb23@gmail.com
- **Application URL:** [https://bmimod.streamlit.app/](https://bmimod.streamlit.app/)

### Version Information
- **Framework:** Streamlit
- **Language:** Python
- **License:** MIT (or specify your license)

---

## Acknowledgments

This application follows BMI classification guidelines established by:
- World Health Organization (WHO)
- National Institutes of Health (NIH)
- Centers for Disease Control and Prevention (CDC)

---

**© 2026 BMI Calculator Application. All rights reserved.**

*Developed with Streamlit framework for interactive health analytics.*
