### **Plagiarism Detection System Design Document**

---

#### **Project Overview**

This project aims to develop a plagiarism detection system that integrates with Microsoft Teams, where teachers can assign work, and students upload their completed assignments as PDF files. The system will authenticate users and direct them to respective dashboards (student, teacher, or developer). It will also retrieve and pre-process the assignment files, run plagiarism detection, and generate reports for students and teachers. Logs and suspicious activities will be available for developers.

---

### **Table of Contents**
1. **Introduction**
2. **Goals and Objectives**
3. **System Architecture**
   - Overview
   - Modules
4. **Functional Requirements**
5. **Non-Functional Requirements**
6. **System Flow**
7. **Technological Stack**
8. **Security Considerations**
9. **Testing & Validation**
10. **Conclusion**

---

### **1. Introduction**

The plagiarism detection system will automate the process of checking students’ assignments for plagiarism and generate detailed reports for both teachers and students. The system will feature user authentication, a user-specific dashboard interface, retrieval, pre-processing, and plagiarism detection modules.

---

### **2. Goals and Objectives**
- **Automate plagiarism detection** for assignments submitted via Microsoft Teams.
- Provide **distinct dashboards** for students, teachers, and developers.
- **Pre-process files** to extract relevant content while discarding irrelevant information.
- **Generate reports** for students and teachers highlighting plagiarism patterns.
- Enable **teachers to give feedback** and flag suspicious submissions.
- Ensure **developers have access to logs** and can monitor the system for errors or suspicious activities.
- Facilitate **scalable, efficient, and secure** file handling and comparison.

---

### **3. System Architecture**

#### **3.1 Overview**

The system architecture comprises several interconnected modules, each designed to handle specific tasks such as user authentication, file retrieval, pre-processing, plagiarism detection, and reporting. Each user role (student, teacher, developer) has access to its own dashboard, which provides tailored functionality.

#### **3.2 Modules**

1. **Authentication Module**:  
   Directs users to role-specific dashboards (student, teacher, or developer) based on their credentials.

2. **Student Dashboard**:
   - Upload assignments (PDF).
   - View plagiarism reports.

3. **Teacher Dashboard**:
   - Run retrieval module.
   - Grade assignments.
   - Run plagiarism tests.
   - Provide feedback and flag suspicious submissions.
   - View comparison of previous plagiarism results.

4. **Developer Dashboard**:
   - View logs (errors, suspicious activities).
   - Monitor system performance.

5. **Retrieval Module**:
   - Fetches student submissions from a specified assignment.
   - Stores assignments locally or in a central repository.

6. **Pre-processing Module**:
   - Sorts files by name.
   - Converts files into a readable format (e.g., text or JSON).
   - Removes unnecessary data.
   - Adds tags to differentiate files.

7. **Plagiarism Detection Module**:
   - Compares current submissions against each other and (if enabled) against previous assignments.
   - Generates plagiarism reports, including:
     - **Student-specific reports**: Highlights plagiarized sections.
     - **Teacher report**: Summarizes overall plagiarism status across students.

8. **Reporting Module**:
   - Sends generated reports via email.
   - Uploads reports to dashboards for access by students and teachers.

---

### **4. Functional Requirements**

1. **User Authentication**:
   - Users must log in with appropriate credentials to access the system.
   - Based on the user role (student, teacher, or developer), the system redirects them to the corresponding dashboard.

2. **File Handling**:
   - Students can upload PDF assignments.
   - Teachers can trigger retrieval of all submitted assignments for a specific task.

3. **Pre-processing**:
   - Convert PDF files into readable formats (text or JSON).
   - Organize files based on metadata (student name, assignment ID).

4. **Plagiarism Detection**:
   - Compare files for similarity.
   - Option to compare current assignments with previous submissions.

5. **Reporting**:
   - Generate and send individual reports to students.
   - Generate a consolidated report for teachers summarizing plagiarism results.

6. **Developer Logs**:
   - Log system errors.
   - Record suspicious activity.

---

### **5. Non-Functional Requirements**

1. **Performance**:
   - The system should handle large numbers of assignments without significant delays.
   - Plagiarism detection should be optimized for speed and accuracy.

2. **Scalability**:
   - The architecture should allow for easy scaling to accommodate more users and assignments.

3. **Security**:
   - Ensure secure file uploads, user authentication, and access to reports.
   - Encrypt sensitive information.

4. **Reliability**:
   - Ensure uptime of the system and accurate plagiarism detection results.

---

### **6. System Flow**

#### **Step-by-Step Flow**:
1. **Teacher assigns work** in Microsoft Teams.
2. **Students upload PDF files** via their dashboard.
3. **Authentication Module** verifies user credentials and redirects:
   - **Student**: Option to upload files and view results.
   - **Teacher**: Option to run retrieval, review plagiarism results, grade, and provide feedback.
   - **Developer**: Access to logs and error reports.
4. **Teacher triggers Retrieval Module**, fetching all submissions from storage.
5. **Pre-processing Module** sorts files, converts formats, cleans unnecessary data, and tags files.
6. **Plagiarism Detection Module** compares assignments, generates plagiarism reports for students and teachers.
7. **Reports** are sent via email and uploaded to dashboards.
8. **Developer dashboard** logs errors and suspicious activities.

---

### **7. Technological Stack**

- **Front-End**:
  - HTML/CSS/JavaScript
  - React.js or Angular.js (for interactive dashboards)

- **Back-End**:
  - Python/Django or Flask (for the main logic)
  - Node.js (for API handling)

- **Storage**:
  - Local storage for small-scale deployments.
  - AWS S3 or Azure Blob Storage for scalable cloud-based storage.

- **Database**:
  - MongoDB or PostgreSQL for storing metadata, user information, and plagiarism reports.

- **Plagiarism Detection**:
  - Cosine similarity, LCS (Longest Common Subsequence), or third-party APIs for similarity detection.

- **Authentication**:
  - OAuth2 for secure login and user role-based access.

- **Email Service**:
  - AWS SES, SendGrid, or SMTP for sending reports.

---

### **8. Security Considerations**

- **Authentication & Authorization**:
  - Use secure token-based authentication (e.g., OAuth2).
  - Role-based access control (RBAC) for dashboard access.

- **Data Encryption**:
  - Encrypt sensitive data in transit (using HTTPS) and at rest (using AES or similar algorithms).

- **Input Validation**:
  - Sanitize uploaded files to prevent malicious file uploads.

---

### **9. Testing & Validation**

1. **Unit Tests**:
   - Ensure each module (authentication, file upload, pre-processing, plagiarism detection) works independently.

2. **Integration Tests**:
   - Test the system flow from file upload to report generation to ensure smooth transitions between modules.

3. **Performance Testing**:
   - Test system performance under load (e.g., large batch submissions).

4. **Security Testing**:
   - Penetration testing for vulnerabilities.
   - Validation of access control and data encryption.

---

### **10. Conclusion**

This design document outlines the architecture and flow of the plagiarism detection system, covering all essential modules, user interactions, and technical details. By implementing this system, teachers can efficiently check for plagiarism, provide feedback, and monitor submissions, while developers maintain system health through logging and monitoring.

---
