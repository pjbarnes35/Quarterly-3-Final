import sqlite3

# Connect to the database
conn = sqlite3.connect('class.db')
cursor = conn.cursor()

# create a list of dictionaries with the questions and answers for Business Applications Development
questions = [
{
        "id": 1,
        "question": "Which programming language is commonly used for web development?",
        "option1": "A. Java",
        "option2": "B. Python",
        "option3": "C. C++",
        "option4": "D. HTML/CSS/JavaScript",
        "correct_answer": "D"
},
{
        "id": 2,
        "question": "What does API stand for?",
        "option1": "A. Application Program Interface",
        "option2": "B. Advanced Programming Interface",
        "option3": "C. Application Process Integration",
        "option4": "D. Automated Program Interaction",
        "correct_answer": "A"
},
{
        "id": 3,
        "question": "What is the difference between front-end and back-end development?",
        "option1": "A. Front-end focuses on user interface, while back-end focuses on server-side logic",
        "option2": "B. Front-end is for mobile apps, while back-end is for web apps",
        "option3": "C. Front-end uses Python, while back-end uses JavaScript",
        "option4": "D. Front-end is for design, while back-end is for marketing",
        "correct_answer": "A"
},
{
        "id": 4,
        "question": "What is an API?",
        "option1": "A. Automated Program Interaction",
        "option2": "B. Application Program Interface",
        "option3": "C. Advanced Programming Interface",
        "option4": "D. Application Process Integration",
        "correct_answer": "B"
},
{
        "id": 5,
        "question": "What is the purpose of version control systems like Git?",
        "option1": "A. Managing customer relationships",
        "option2": "B. Tracking changes to code and collaborating with others",
        "option3": "C. Analyzing market trends",
        "option4": "D. Automating business processes",
        "correct_answer": "B"
},
{
    "id": 6,
    "question": "Which database management system is commonly used for relational databases?",
    "option1": "A. MongoDB",
    "option2": "B. SQLite",
    "option3": "C. Redis",
    "option4": "D. MySQL",
    "correct_answer": "D"
},
{
    "id": 7,
    "question": "What is the primary purpose of a RESTful API?",
    "option1": "A. Enforcing security protocols",
    "option2": "B. Providing a standardized interface for web services",
    "option3": "C. Optimizing database queries",
    "option4": "D. Generating dynamic web content",
    "correct_answer": "B"
},
{
    "id": 8,
    "question": "What is the role of a front-end framework like React or Angular?",
    "option1": "A. Managing server-side operations",
    "option2": "B. Optimizing database performance",
    "option3": "C. Simplifying the development of user interfaces",
    "option4": "D. Interacting with hardware components",
    "correct_answer": "C"
},
{
    "id": 9,
    "question": "What is the purpose of unit testing in software development?",
    "option1": "A. Identifying and fixing security vulnerabilities",
    "option2": "B. Ensuring that individual components of a program work correctly",
    "option3": "C. Monitoring system performance over time",
    "option4": "D. Implementing user interface designs",
    "correct_answer": "B"
},
{
    "id": 10,
    "question": "What is the difference between synchronous and asynchronous programming?",
    "option1": "A. Synchronous programming allows multiple tasks to run simultaneously, while asynchronous programming requires tasks to be executed sequentially",
    "option2": "B. Synchronous programming waits for tasks to complete before moving on to the next, while asynchronous programming continues to execute tasks without waiting for them to finish",
    "option3": "C. Synchronous programming is more efficient for CPU-bound tasks, while asynchronous programming is more efficient for I/O-bound tasks",
    "option4": "D. Synchronous programming is used for front-end development, while asynchronous programming is used for back-end development",
    "correct_answer": "B"
} 
]


# Insert questions into the Business Applications Development table
for question in questions:
   pass
   cursor.execute('''INSERT INTO BusinessApplicationsDevelopment (id, question, option1, option2, option3, option4, correct_answer)
                     VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
                                                        question['option2'], question['option3'], question['option4'],
                                                        question['correct_answer']))
   conn.commit()

# use select query to check if your data properly populated the table
cursor.execute('''SELECT * FROM BusinessApplicationsDevelopment''')

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the fetched rows
for row in rows:
   print(row)

# List of questions for Finance class
finance_questions = [
{
        "id": 1,
        "question": "What is the primary goal of financial management?",
        "option1": "A. Maximizing profits",
        "option2": "B. Minimizing expenses",
        "option3": "C. Maximizing shareholder wealth",
        "option4": "D. Increasing market share",
        "correct_answer": "C"
},
{
        "id": 2,
        "question": "What is the formula for calculating Return on Investment (ROI)?",
        "option1": "A. Net Profit / Total Assets",
        "option2": "B. Net Profit / Total Equity",
        "option3": "C. Net Profit / Total Revenue",
        "option4": "D. Net Profit / Investment Cost",
        "correct_answer": "D"
},
{
        "id": 3,
        "question": "What does GDP stand for?",
        "option1": "A. Gross Domestic Product",
        "option2": "B. Gross Domestic Profit",
        "option3": "C. Government Development Plan",
        "option4": "D. Gross Dollar Price",
        "correct_answer": "A"
},
{
        "id": 4,
        "question": "What is the role of the Securities and Exchange Commission (SEC)?",
        "option1": "A. Protecting consumers from fraud",
        "option2": "B. Regulating the stock market",
        "option3": "C. Managing international trade agreements",
        "option4": "D. Setting interest rates",
        "correct_answer": "B"
},
{
        "id": 5,
        "question": "What is a balance sheet used for?",
        "option1": "A. Recording daily transactions",
        "option2": "B. Evaluating profitability",
        "option3": "C. Summarizing a company's financial position",
        "option4": "D. Projecting future revenue",
        "correct_answer": "C"
},
{
        "id": 6,
        "question": "What is the difference between equity and debt financing?",
        "option1": "A. Equity involves borrowing money, while debt involves selling ownership stake",
        "option2": "B. Equity represents ownership in a company, while debt represents borrowed funds",
        "option3": "C. Equity financing is more risky than debt financing",
        "option4": "D. Debt financing offers higher returns than equity financing",
        "correct_answer": "B"
},
{
        "id": 7,
        "question": "What is the role of the Federal Reserve in the economy?",
        "option1": "A. Regulating international trade",
        "option2": "B. Managing fiscal policy",
        "option3": "C. Controlling inflation and interest rates",
        "option4": "D. Setting tax rates",
        "correct_answer": "C"
},
{
        "id": 8,
        "question": "What is the purpose of financial ratios?",
        "option1": "A. Comparing a company's financial performance over time",
        "option2": "B. Evaluating a company's liquidity, profitability, and solvency",
        "option3": "C. Predicting future stock prices",
        "option4": "D. Assessing market trends",
        "correct_answer": "B"
},
{
        "id": 9,
        "question": "What is the difference between capital expenditure and operating expenditure?",
        "option1": "A. Capital expenditure is for short-term expenses, while operating expenditure is for long-term investments",
        "option2": "B. Capital expenditure is for acquiring fixed assets, while operating expenditure is for day-to-day expenses",
        "option3": "C. Operating expenditure is financed through equity, while capital expenditure is financed through debt",
        "option4": "D. Capital expenditure is tax-deductible, while operating expenditure is not",
        "correct_answer": "B"
},
{
        "id": 10,
        "question": "What is the concept of present value in finance?",
        "option1": "A. The value of money in the future compared to its value today",
        "option2": "B. The total amount of money an investment will generate over its lifetime",
        "option3": "C. The amount of money needed to start a business",
        "option4": "D. The value of a company's stock on the open market",
        "correct_answer": "A"
}
]
# Insert questions into the Finance table
for question in finance_questions:
    cursor.execute('''INSERT INTO Finance (id, question, option1, option2, option3, option4, correct_answer)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
                                                         question['option2'], question['option3'], question['option4'],
                                                         question['correct_answer']))
    conn.commit()

# List of questions for Business Intelligence and Analytics Capstone course
analytics_questions = [
{
    "id": 1,
    "question": "What is the primary goal of financial management?",
    "option1": "A. Maximizing profits",
    "option2": "B. Minimizing expenses",
    "option3": "C. Maximizing shareholder wealth",
    "option4": "D. Increasing market share",
    "correct_answer": "C"
},
{
    "id": 2,
    "question": "What is the formula for calculating Return on Investment (ROI)?",
    "option1": "A. Net Profit / Total Assets",
    "option2": "B. Net Profit / Total Equity",
    "option3": "C. Net Profit / Total Revenue",
    "option4": "D. Net Profit / Investment Cost",
    "correct_answer": "D"
},
{
    "id": 3,
    "question": "What does GDP stand for?",
    "option1": "A. Gross Domestic Product",
    "option2": "B. Gross Domestic Profit",
    "option3": "C. Government Development Plan",
    "option4": "D. Gross Dollar Price",
    "correct_answer": "A"
},
{
    "id": 4,
    "question": "What is the role of the Securities and Exchange Commission (SEC)?",
    "option1": "A. Protecting consumers from fraud",
    "option2": "B. Regulating the stock market",
    "option3": "C. Managing international trade agreements",
    "option4": "D. Setting interest rates",
    "correct_answer": "B"
},
{
    "id": 5,
    "question": "What is a balance sheet used for?",
    "option1": "A. Recording daily transactions",
    "option2": "B. Evaluating profitability",
    "option3": "C. Summarizing a company's financial position",
    "option4": "D. Projecting future revenue",
    "correct_answer": "C"
},
{
    "id": 6,
    "question": "What is the difference between equity and debt financing?",
    "option1": "A. Equity involves borrowing money, while debt involves selling ownership stake",
    "option2": "B. Equity represents ownership in a company, while debt represents borrowed funds",
    "option3": "C. Equity financing is more risky than debt financing",
    "option4": "D. Debt financing offers higher returns than equity financing",
    "correct_answer": "B"
},
{
    "id": 7,
    "question": "What is the role of the Federal Reserve in the economy?",
    "option1": "A. Regulating international trade",
    "option2": "B. Managing fiscal policy",
    "option3": "C. Controlling inflation and interest rates",
    "option4": "D. Setting tax rates",
    "correct_answer": "C"
},
{
    "id": 8,
    "question": "What is the purpose of financial ratios?",
    "option1": "A. Comparing a company's financial performance over time",
    "option2": "B. Evaluating a company's liquidity, profitability, and solvency",
    "option3": "C. Predicting future stock prices",
    "option4": "D. Assessing market trends",
    "correct_answer": "B"
},
{
    "id": 9,
    "question": "What is the difference between capital expenditure and operating expenditure?",
    "option1": "A. Capital expenditure is for short-term expenses, while operating expenditure is for long-term investments",
    "option2": "B. Capital expenditure is for acquiring fixed assets, while operating expenditure is for day-to-day expenses",
    "option3": "C. Operating expenditure is financed through equity, while capital expenditure is financed through debt",
    "option4": "D. Capital expenditure is tax-deductible, while operating expenditure is not",
    "correct_answer": "B"
},
{
    "id": 10,
    "question": "What is the concept of present value in finance?",
    "option1": "A. The value of money in the future compared to its value today",
    "option2": "B. The total amount of money an investment will generate over its lifetime",
    "option3": "C. The amount of money needed to start a business",
    "option4": "D. The value of a company's stock on the open market",
    "correct_answer": "A"
}
]

# use a loop to insert questions into the AnalyticsCapstone table
for question in analytics_questions:
    cursor.execute('''INSERT INTO AnalyticsCapstone (id, question, option1, option2, option3, option4, correct_answer)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
                                                         question['option2'], question['option3'], question['option4'],
                                                         question['correct_answer']))
    conn.commit()

# List of questions for Business Strategy course
business_strategy_questions = [
    {
    "id": 1,
    "question": "What is competitive advantage?",
    "option1": "A. The unique position a company occupies in its industry",
    "option2": "B. The amount of market share a company has",
    "option3": "C. The level of profitability a company achieves",
    "option4": "D. The number of products a company offers",
    "correct_answer": "A"
},
{
    "id": 2,
    "question": "What is strategic planning?",
    "option1": "A. The process of setting short-term goals and objectives",
    "option2": "B. The development of long-term plans to achieve organizational goals",
    "option3": "C. The analysis of competitors' strengths and weaknesses",
    "option4": "D. The implementation of tactical initiatives",
    "correct_answer": "B"
},
{
    "id": 3,
    "question": "What is SWOT analysis?",
    "option1": "A. Assessing a company's strengths, weaknesses, opportunities, and threats",
    "option2": "B. Calculating return on investment",
    "option3": "C. Identifying key performance indicators",
    "option4": "D. Analyzing market segmentation",
    "correct_answer": "A"
},
{
    "id": 4,
    "question": "What is market segmentation?",
    "option1": "A. Dividing a market into distinct groups of buyers with different needs, characteristics, or behaviors",
    "option2": "B. Analyzing customer satisfaction levels",
    "option3": "C. Forecasting future market trends",
    "option4": "D. Developing pricing strategies",
    "correct_answer": "A"
},
{
    "id": 5,
    "question": "What is differentiation strategy?",
    "option1": "A. Creating unique products or services that offer superior value to customers",
    "option2": "B. Selling products at the lowest possible price",
    "option3": "C. Expanding into new geographic markets",
    "option4": "D. Developing a niche market",
    "correct_answer": "A"
},
{
    "id": 6,
    "question": "What is cost leadership?",
    "option1": "A. Becoming the lowest-cost producer in an industry",
    "option2": "B. Differentiating products based on quality and features",
    "option3": "C. Pursuing growth through mergers and acquisitions",
    "option4": "D. Focusing on a narrow market segment",
    "correct_answer": "A"
},
{
    "id": 7,
    "question": "What is blue ocean strategy?",
    "option1": "A. Creating uncontested market space by offering innovative products or services",
    "option2": "B. Expanding market share through aggressive pricing tactics",
    "option3": "C. Achieving growth through strategic alliances",
    "option4": "D. Targeting high-value customers with premium offerings",
    "correct_answer": "A"
},
{
    "id": 8,
    "question": "What is strategic alignment?",
    "option1": "A. Ensuring that organizational goals and activities are coordinated and supportive",
    "option2": "B. Managing risk through diversification",
    "option3": "C. Identifying opportunities for international expansion",
    "option4": "D. Implementing technology to improve operational efficiency",
    "correct_answer": "A"
},
{
    "id": 9,
    "question": "What is corporate governance?",
    "option1": "A. The system of rules, practices, and processes by which a company is directed and controlled",
    "option2": "B. The process of managing",
    "correct_answer": "A"
},
{
    "id": 10,
    "question": "What is the role of a mission statement in business strategy?",
    "option1": "A. Communicating the company's purpose and values to stakeholders",
    "option2": "B. Setting financial targets and performance metrics",
    "option3": "C. Analyzing market trends and competitive forces",
    "option4": "D. Identifying opportunities for cost reduction",
    "correct_answer": "A"
}
]

# for loop to insert questions into the BusinessStrategy table
for question in business_strategy_questions:
    cursor.execute('''INSERT INTO BusinessStrategy (id, question, option1, option2, option3, option4, correct_answer)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
                                                         question['option2'], question['option3'], question['option4'],
                                                         question['correct_answer']))
    conn.commit()

# List of questions for Communications course
comm_questions = [
    {
    "id": 1,
    "question": "What is the purpose of a business report?",
    "option1": "A. Presenting financial statements to shareholders",
    "option2": "B. Providing information and analysis to support decision-making",
    "option3": "C. Communicating marketing messages to customers",
    "option4": "D. Documenting employee performance",
    "correct_answer": "B"
},
{
    "id": 2,
    "question": "What is the difference between formal and informal communication?",
    "option1": "A. Formal communication follows established channels and protocols, while informal communication is casual and spontaneous",
    "option2": "B. Formal communication is written, while informal communication is verbal",
    "option3": "C. Formal communication is used for internal communication, while informal communication is used for external communication",
    "option4": "D. Formal communication is mandatory, while informal communication is optional",
    "correct_answer": "A"
},
{
    "id": 3,
    "question": "What is active listening?",
    "option1": "A. Paying full attention to the speaker and providing feedback to confirm understanding",
    "option2": "B. Interrupting the speaker to ask questions or share opinions",
    "option3": "C. Focusing on one's own thoughts and ideas instead of listening to others",
    "option4": "D. Reacting emotionally to the speaker's message without considering its content",
    "correct_answer": "A"
},
{
    "id": 4,
    "question": "What is the purpose of a business presentation?",
    "option1": "A. Sharing information with stakeholders",
    "option2": "B. Persuading others to take a specific action",
    "option3": "C. Providing updates on project progress",
    "option4": "D. All of the above",
    "correct_answer": "D"
},
{
    "id": 5,
    "question": "What is the role of body language in communication?",
    "option1": "A. Reinforcing spoken messages and conveying emotions",
    "option2": "B. Providing additional information not included in the verbal message",
    "option3": "C. Interpreting data and presenting findings",
    "option4": "D. Ensuring that messages are received and understood by the intended audience",
    "correct_answer": "A"
},
{
    "id": 6,
    "question": "What is the purpose of a business proposal?",
    "option1": "A. Soliciting feedback from stakeholders",
    "option2": "B. Outlining a plan for addressing a specific business need",
    "option3": "C. Reporting on the results of a research project",
    "option4": "D. Providing a summary of key findings and recommendations",
    "correct_answer": "B"
},
{
    "id": 7,
    "question": "What is the difference between persuasion and manipulation?",
    "option1": "A. Persuasion involves influencing others through reasoning and evidence, while manipulation involves deceiving others for personal gain",
    "option2": "B. Persuasion focuses on building trust and rapport, while manipulation relies on coercion and intimidation",
    "option3": "C. Persuasion is ethical, while manipulation is unethical",
    "option4": "D. Persuasion leads to mutually beneficial outcomes, while manipulation leads to one-sided outcomes",
    "correct_answer": "A"
},
{
    "id": 8,
    "question": "What is the purpose of a business memo?",
    "option1": "A. Providing feedback on employee performance",
    "option2": "B. Documenting decisions and agreements reached in meetings",
    "option3": "C. Sharing updates on project progress",
    "option4": "D. Soliciting input from team members",
    "correct_answer": "B"
},
{
    "id": 9,
    "question": "What is the difference between formal and informal writing?",
    "option1": "A. Formal writing follows standard conventions and is structured, while informal writing is casual and conversational",
    "option2": "B. Formal writing is used for internal communication, while informal writing is used for external communication",
    "option3": "C. Formal writing is mandatory, while informal writing is optional",
    "option4": "D. Formal writing is professional, while informal writing is personal",
    "correct_answer": "A"
},
{
    "id": 10,
    "question": "What is the purpose of a business email?",
    "option1": "A. Sending meeting invitations and scheduling appointments",
    "option2": "B. Sharing information and collaborating with colleagues",
    "option3": "C. Communicating with customers and clients",
    "option4": "D. All of the above",
    "correct_answer": "D"
}
]

# Insert questions into the Business Communications table
for question in comm_questions:
    cursor.execute('''INSERT INTO BusinessCommunication (id, question, option1, option2, option3, option4, correct_answer)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
                                                         question['option2'], question['option3'], question['option4'],
                                                         question['correct_answer']))
    conn.commit()

#Fetch and display data from each table
tables = ['BusinessStrategy', 'BusinessApplicationsDevelopment', 'Finance', 'AnalyticsCapstone', 'BusinessCommunication']
for table in tables:
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    print(f"Contents of {table} table:")
    for row in rows:
        print(row)
    print()