from flask import Flask, jsonify, request, render_template
import pandas as pd
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Your JSON data
raw_data = [
    {
        "EmployeeID": "200001",
        "Age": "31.0",
        "AvgDailyHours": ["9.5","8.5", "7.1", "6.5", 4.2],
        "Department": "Research & Development",
        "Education": "5",
        "EducationField": "Human Resources",
        "Gender": "Female",
        "HasFlexibleTimings": "No",
        "IsIndividualContributor": "Yes",
        "JobInvolvement": "2",
        "JobRole": "Research Director",
        "JobSatisfaction": "3",
        "LeavesTaken": ["4.0","8.0", "5.0", "4.0", "5.0"],
        "MaritalStatus": "Single",
        "MicromanagedAtWork": "5.0",
        "MonthlyIncome": "166667",
        "NumCompaniesWorked": "1",
        "PercentSalaryHike": "11",
        "PerformanceRating": ["3", "4", "2", "8", "5", "9",],
        "RelationshipSatisfaction": "3",
        "RemoteWorkSatistfaction": "Very High",
        "SelfMotivationLevel": ["1", "5", "3", "4",],
        "TotalWorkingYears": "6.0",
        "TrainingTimesLastYear": "6",
        "WorkLifeBalance": "3",
        "WorkLoadLevel": "High",
        "YearsAtCompany": "1.0",
        "YearsSinceLastPromotion": "1.0",
        "YearsWithCurrManager": "1.0"
    },
    {
        "EmployeeID": "200002",
        "Age": "52.0",
        "AvgDailyHours": ["7.5","6.5", "7.1", "8.5", 4.2],
        "Department": "Human Resources",
        "Education": "3",
        "EducationField": "Marketing",
        "Gender": "Female",
        "HasFlexibleTimings": "No",
        "IsIndividualContributor": "No",
        "JobInvolvement": "3",
        "JobRole": "Research Director",
        "JobSatisfaction": "2",
        "LeavesTaken": ["7.0","8.0", "2.0", "1.0", "2.0"],
        "MaritalStatus": "Married",
        "MicromanagedAtWork": "1.0",
        "MonthlyIncome": "216667",
        "NumCompaniesWorked": "1",
        "PercentSalaryHike": "23",
        "PerformanceRating": ["4", "8", "2", "6", "4", "3",],
        "RelationshipSatisfaction": "1",
        "RemoteWorkSatistfaction": "Medium",
        "SelfMotivationLevel": ["2", "3", "3", "2",],
        "TotalWorkingYears": "10.0",
        "TrainingTimesLastYear": "4",
        "WorkLifeBalance": "3",
        "WorkLoadLevel": "Low",
        "YearsAtCompany": "1.0",
        "YearsSinceLastPromotion": "1.0",
        "YearsWithCurrManager": "1.0"
    },
    {
        "EmployeeID": "200003",
        "Age": "20.0",
        "AvgDailyHours": ["5.5","6.5", "7.1", "8.5", 8.2],
        "Department": "Sales",
        "Education": "4",
        "EducationField": "Technical Degree",
        "Gender": "Male",
        "HasFlexibleTimings": "Yes",
        "IsIndividualContributor": "No",
        "JobInvolvement": "4",
        "JobRole": "Healthcare Representative",
        "JobSatisfaction": "4",
        "LeavesTaken": ["2.0","4.0", "3.0", "3.0", "1.0"],
        "MaritalStatus": "Married",
        "MicromanagedAtWork": "5.0",
        "MonthlyIncome": "25000",
        "NumCompaniesWorked": "1",
        "PercentSalaryHike": "14",
        "PerformanceRating": ["5", "7", "8", "7", "8", "9",],
        "RelationshipSatisfaction": "1",
        "RemoteWorkSatistfaction": "Low",
        "SelfMotivationLevel": ["1", "5", "8", "7",],
        "TotalWorkingYears": "1.0",
        "TrainingTimesLastYear": "0",
        "WorkLifeBalance": "3",
        "WorkLoadLevel": "Low",
        "YearsAtCompany": "0.0",
        "YearsSinceLastPromotion": "0.0",
        "YearsWithCurrManager": "0.0"
    }
]


# Function to parse the data
def parse_data(raw_data):
    parsed_data = []
    for entry in raw_data:
        employee_data = {}
        for key, value in entry.items():
            if isinstance(value, list):
                employee_data[key] = [str(v) for v in value]
            else:
                employee_data[key] = str(value)
        parsed_data.append(employee_data)
    return parsed_data


# Parse the data
data = parse_data(raw_data)

# Convert to DataFrame for easier manipulation
df = pd.DataFrame(data)

@app.route('/employees', methods=['GET'])
def get_employees():
    employee_id = request.args.get('id')
    if employee_id:
        # Filter data based on Employee ID
        filtered_data = df[df['EmployeeID'] == employee_id].to_dict(orient='records')
        return jsonify(filtered_data)
    return jsonify(data)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
