import numpy as np

class StudentPerformanceAnalyzer:
    def __init__(self):
        np.random.seed(42)
        self.students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
        self.subjects = ['Math', 'Science', 'English', 'History']
        
        self.marks = np.random.randint(50, 100, size=(5, 4))

    def basic_stats(self):
        print("=== BASIC STATISTICS ===")
        total_marks = np.sum(self.marks)
        average_marks = np.mean(self.marks)
        std_dev = np.std(self.marks)

        print(f"Total Marks (All Students & Subjects): {total_marks}")
        print(f"Average Marks: {average_marks:.2f}")
        print(f"Standard Deviation: {std_dev:.2f}")

    def student_analysis(self):
        print("\n=== STUDENT PERFORMANCE ===")
        for i, student in enumerate(self.students):
            total = np.sum(self.marks[i])
            avg = np.mean(self.marks[i])
            print(f"{student}: Total = {total}, Average = {avg:.2f}")

    def subject_analysis(self):
        print("\n=== SUBJECT PERFORMANCE ===")
        for j, subject in enumerate(self.subjects):
            scores = self.marks[:, j]
            print(f"{subject}: Avg = {np.mean(scores):.2f}, Max = {np.max(scores)}, Min = {np.min(scores)}")

    def top_and_consistent_students(self):
        print("\n=== TOP AND CONSISTENT STUDENTS ===")
        total_scores = np.sum(self.marks, axis=1)
        std_scores = np.std(self.marks, axis=1)

        top_student = self.students[np.argmax(total_scores)]
        consistent_student = self.students[np.argmin(std_scores)]

        print(f"Top Performer: {top_student} (Total = {np.max(total_scores)})")
        print(f"Most Consistent: {consistent_student} (Std Dev = {np.min(std_scores):.2f})")

    def subject_correlation(self):
        print("\n=== SUBJECT CORRELATIONS ===")
        correlation_matrix = np.corrcoef(self.marks.T)
        for i in range(len(self.subjects)):
            for j in range(i + 1, len(self.subjects)):
                print(f"{self.subjects[i]} vs {self.subjects[j]}: {correlation_matrix[i, j]:.2f}")

    def forecast_performance(self):
        print("\n=== PERFORMANCE FORECASTING (Trend Simulation) ===")
    
        exams = np.array([1, 2, 3, 4])
        for i, student in enumerate(self.students):
            marks = self.marks[i]
            coeffs = np.polyfit(exams, marks, 1)
            next_exam = np.polyval(coeffs, 5)
            print(f"{student} Forecasted Avg in Exam 5: {next_exam:.2f}")

    def run_full_analysis(self):
        print("STUDENT PERFORMANCE DASHBOARD")
        print("=" * 40)
        self.basic_stats()
        self.student_analysis()
        self.subject_analysis()
        self.top_and_consistent_students()
        self.subject_correlation()
        self.forecast_performance()
        print("\nRAW DATA:\n", self.marks)

analyzer = StudentPerformanceAnalyzer()
analyzer.run_full_analysis()
