import sqlite3
import pandas as pd

def run_analytics():
    # 1. Connect to an in-memory database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    print("Creating academic_scores table...")
    # 2. Create a table for student test scores
    cursor.execute('''
        CREATE TABLE academic_scores (
            student_name TEXT,
            subject TEXT,
            exam_date TEXT,
            score INTEGER
        )
    ''')
    
    # 3. Insert real, multi-variable evaluation data
    records = [
        ('Aiden', 'Mathematics', '2025-08-15', 82),
        ('Aiden', 'Mathematics', '2025-09-15', 85),
        ('Aiden', 'Mathematics', '2025-10-15', 78),
        ('Priya', 'Mathematics', '2025-08-15', 95),
        ('Priya', 'Mathematics', '2025-09-15', 92),
        ('Priya', 'Mathematics', '2025-10-15', 98),
        ('Carlos', 'Mathematics', '2025-08-15', 70),
        ('Carlos', 'Mathematics', '2025-09-15', 75),
        ('Carlos', 'Mathematics', '2025-10-15', 88),
        ('Aiden', 'Science', '2025-08-15', 88),
        ('Priya', 'Science', '2025-08-15', 91),
        ('Carlos', 'Science', '2025-08-15', 85)
    ]
    cursor.executemany('INSERT INTO academic_scores VALUES (?, ?, ?, ?)', records)
    conn.commit()
    
    print("\n========================================================")
    print("ANALYSIS 1: Ranking Students Within Each Subject")
    print("========================================================")
    # Highlights who performed best per subject category
    query1 = '''
        SELECT 
            subject,
            student_name,
            score,
            RANK() OVER (PARTITION BY subject ORDER BY score DESC) as subject_rank
        FROM academic_scores
        WHERE exam_date = '2025-08-15';
    '''
    print(pd.read_sql_query(query1, conn).to_string(index=False))
    
    print("\n========================================================")
    print("ANALYSIS 2: Tracking Score Progressions (LAG Function)")
    print("========================================================")
    # Compares the current score against the student's previous test score
    query2 = '''
        SELECT 
            student_name,
            subject,
            exam_date,
            score,
            LAG(score, 1) OVER (PARTITION BY student_name, subject ORDER BY exam_date) as previous_score,
            score - LAG(score, 1) OVER (PARTITION BY student_name, subject ORDER BY exam_date) as score_delta
        FROM academic_scores
        WHERE subject = 'Mathematics';
    '''
    print(pd.read_sql_query(query2, conn).to_string(index=False))

    print("\n========================================================")
    print("ANALYSIS 3: Cumulative Academic Performance (Running Total)")
    print("========================================================")
    # Calculates a rolling total of points earned over time per student
    query3 = '''
        SELECT 
            student_name,
            subject,
            exam_date,
            score,
            SUM(score) OVER (PARTITION BY student_name ORDER BY exam_date) as cumulative_points
        FROM academic_scores
        WHERE subject = 'Mathematics';
    '''
    print(pd.read_sql_query(query3, conn).to_string(index=False))
    
    conn.close()

if __name__ == "__main__":
    run_analytics()