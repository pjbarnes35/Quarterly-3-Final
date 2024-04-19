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

# use select query to check if your data properly populated the table
cursor.execute('''SELECT * FROM BusinessApplicationsDevelopment''')

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the fetched rows
for row in rows:
   print(row)

# # List of questions for Finance class
# finance_questions = [
#     {
#         "id": 1,
#         "question": "What is the primary goal of financial management?",
#         "option1": "A. Maximizing profits",
#         "option2": "B. Minimizing expenses",
#         "option3": "C. Maximizing shareholder wealth",
#         "option4": "D. Increasing market share",
#         "correct_answer": "C"
#     },
#     {
#         "id": 2,
#         "question": "What is the formula for calculating Return on Investment (ROI)?",
#         "option1": "A. Net Profit / Total Assets",
#         "option2": "B. Net Profit / Total Equity",
#         "option3": "C. Net Profit / Total Revenue",
#         "option4": "D. Net Profit / Investment Cost",
#         "correct_answer": "D"
#     },
#     {
#         "id": 3,
#         "question": "What does GDP stand for?",
#         "option1": "A. Gross Domestic Product",
#         "option2": "B. Gross Domestic Profit",
#         "option3": "C. Government Development Plan",
#         "option4": "D. Gross Dollar Price",
#         "correct_answer": "A"
#     },
#     {
#         "id": 4,
#         "question": "What is the role of the Securities and Exchange Commission (SEC)?",
#         "option1": "A. Protecting consumers from fraud",
#         "option2": "B. Regulating the stock market",
#         "option3": "C. Managing international trade agreements",
#         "option4": "D. Setting interest rates",
#         "correct_answer": "B"
#     },
#     {
#         "id": 5,
#         "question": "What is a balance sheet used for?",
#         "option1": "A. Recording daily transactions",
#         "option2": "B. Evaluating profitability",
#         "option3": "C. Summarizing a company's financial position",
#         "option4": "D. Projecting future revenue",
#         "correct_answer": "C"
#     },
#     {
#         "id": 6,
#         "question": "What is the difference between equity and debt financing?",
#         "option1": "A. Equity involves borrowing money, while debt involves selling ownership stake",
#         "option2": "B. Equity represents ownership in a company, while debt represents borrowed funds",
#         "option3": "C. Equity financing is more risky than debt financing",
#         "option4": "D. Debt financing offers higher returns than equity financing",
#         "correct_answer": "B"
#     },
#     {
#         "id": 7,
#         "question": "What is the role of the Federal Reserve in the economy?",
#         "option1": "A. Regulating international trade",
#         "option2": "B. Managing fiscal policy",
#         "option3": "C. Controlling inflation and interest rates",
#         "option4": "D. Setting tax rates",
#         "correct_answer": "C"
#     },
#     {
#         "id": 8,
#         "question": "What is the purpose of financial ratios?",
#         "option1": "A. Comparing a company's financial performance over time",
#         "option2": "B. Evaluating a company's liquidity, profitability, and solvency",
#         "option3": "C. Predicting future stock prices",
#         "option4": "D. Assessing market trends",
#         "correct_answer": "B"
#     },
#     {
#         "id": 9,
#         "question": "What is the difference between capital expenditure and operating expenditure?",
#         "option1": "A. Capital expenditure is for short-term expenses, while operating expenditure is for long-term investments",
#         "option2": "B. Capital expenditure is for acquiring fixed assets, while operating expenditure is for day-to-day expenses",
#         "option3": "C. Operating expenditure is financed through equity, while capital expenditure is financed through debt",
#         "option4": "D. Capital expenditure is tax-deductible, while operating expenditure is not",
#         "correct_answer": "B"
#     },
#     {
#         "id": 10,
#         "question": "What is the concept of present value in finance?",
#         "option1": "A. The value of money in the future compared to its value today",
#         "option2": "B. The total amount of money an investment will generate over its lifetime",
#         "option3": "C. The amount of money needed to start a business",
#         "option4": "D. The value of a company's stock on the open market",
#         "correct_answer": "A"
#     }
# ]
# # Insert questions into the Finance table
# for question in finance_questions:
#     cursor.execute('''INSERT INTO Finance (id, question, option1, option2, option3, option4, correct_answer)
#                       VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
#                                                          question['option2'], question['option3'], question['option4'],
#                                                          question['correct_answer']))
#     conn.commit()

# # List of questions for Business Intelligence and Analytics Capstone course
# analytics_questions = [
#     {
#         "id": 1,
#         "question": "What is predictive modeling?",
#         "options": [
#             "A. A statistical technique used to predict future events or outcomes",
#             "B. A method for organizing and analyzing large datasets",
#             "C. A process for creating data visualizations",
#             "D. An approach to optimizing business processes"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 2,
#         "question": "What is clustering analysis?",
#         "options": [
#             "A. A technique for classifying data into groups based on similarity",
#             "B. A method for calculating statistical correlations",
#             "C. A process for identifying outliers in a dataset",
#             "D. An approach to detecting patterns in time-series data"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 3,
#         "question": "What is text mining?",
#         "options": [
#             "A. Analyzing unstructured text data to extract meaningful insights",
#             "B. Identifying trends in numerical datasets",
#             "C. Classifying data into predefined categories",
#             "D. Forecasting future events based on historical data"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 4,
#         "question": "What is sentiment analysis?",
#         "options": [
#             "A. Evaluating the emotional tone of text data",
#             "B. Analyzing financial markets",
#             "C. Assessing the performance of predictive models",
#             "D. Measuring customer satisfaction"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 5,
#         "question": "What is time series forecasting?",
#         "options": [
#             "A. Predicting future values based on past observations in sequential data",
#             "B. Analyzing cross-sectional data at a single point in time",
#             "C. Estimating the impact of variables on an outcome",
#             "D. Forecasting trends using regression analysis"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 6,
#         "question": "What is association rule mining?",
#         "options": [
#             "A. Identifying patterns in transactional data",
#             "B. Analyzing variance in experimental designs",
#             "C. Predicting outcomes using decision trees",
#             "D. Calculating probabilities in Bayesian statistics"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 7,
#         "question": "What is anomaly detection?",
#         "options": [
#             "A. Identifying unusual patterns or outliers in data",
#             "B. Predicting future events based on past observations",
#             "C. Classifying data into distinct categories",
#             "D. Estimating unknown parameters in a model"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 8,
#         "question": "What is regression analysis?",
#         "options": [
#             "A. Modeling the relationship between variables in numerical data",
#             "B. Identifying clusters in multidimensional datasets",
#             "C. Calculating probabilities based on observed frequencies",
#             "D. Forecasting future events based on historical data"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 9,
#         "question": "What is machine learning?",
#         "options": [
#             "A. A branch of artificial intelligence that enables computers to learn from data",
#             "B. A method for optimizing business processes",
#             "C. A technique for analyzing financial markets",
#             "D. An approach to database management"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 10,
#         "question": "What is optimization?",
#         "options": [
#             "A. Finding the best solution to a problem under given constraints",
#             "B. Predicting future events based on historical data",
#             "C. Analyzing patterns in large datasets",
#             "D. Testing hypotheses using statistical methods"
#         ],
#         "correct_answer": "A"
#     }
# ]

# # use a loop to insert questions into the AnalyticsCapstone table
# for question in analytics_questions:
#     cursor.execute('''INSERT INTO AnalyticsCapstone (id, question, option1, option2, option3, option4, correct_answer)
#                       VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
#                                                          question['option2'], question['option3'], question['option4'],
#                                                          question['correct_answer']))
#     conn.commit()

# # List of questions for Business Strategy course
# business_strategy_questions = [
#     {
#         "id": 1,
#         "question": "What is competitive advantage?",
#         "options": [
#             "A. The unique position a company occupies in its industry",
#             "B. The amount of market share a company has",
#             "C. The level of profitability a company achieves",
#             "D. The number of products a company offers"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 2,
#         "question": "What is strategic planning?",
#         "options": [
#             "A. The process of setting short-term goals and objectives",
#             "B. The development of long-term plans to achieve organizational goals",
#             "C. The analysis of competitors' strengths and weaknesses",
#             "D. The implementation of tactical initiatives"
#         ],
#         "correct_answer": "B"
#     },
#     {
#         "id": 3,
#         "question": "What is SWOT analysis?",
#         "options": [
#             "A. Assessing a company's strengths, weaknesses, opportunities, and threats",
#             "B. Calculating return on investment",
#             "C. Identifying key performance indicators",
#             "D. Analyzing market segmentation"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 4,
#         "question": "What is market segmentation?",
#         "options": [
#             "A. Dividing a market into distinct groups of buyers with different needs, characteristics, or behaviors",
#             "B. Analyzing customer satisfaction levels",
#             "C. Forecasting future market trends",
#             "D. Developing pricing strategies"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 5,
#         "question": "What is differentiation strategy?",
#         "options": [
#             "A. Creating unique products or services that offer superior value to customers",
#             "B. Selling products at the lowest possible price",
#             "C. Expanding into new geographic markets",
#             "D. Developing a niche market"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 6,
#         "question": "What is cost leadership?",
#         "options": [
#             "A. Becoming the lowest-cost producer in an industry",
#             "B. Differentiating products based on quality and features",
#             "C. Pursuing growth through mergers and acquisitions",
#             "D. Focusing on a narrow market segment"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 7,
#         "question": "What is blue ocean strategy?",
#         "options": [
#             "A. Creating uncontested market space by offering innovative products or services",
#             "B. Expanding market share through aggressive pricing tactics",
#             "C. Achieving growth through strategic alliances",
#             "D. Targeting high-value customers with premium offerings"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 8,
#         "question": "What is strategic alignment?",
#         "options": [
#             "A. Ensuring that organizational goals and activities are coordinated and supportive",
#             "B. Managing risk through diversification",
#             "C. Identifying opportunities for international expansion",
#             "D. Implementing technology to improve operational efficiency"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 9,
#         "question": "What is corporate governance?",
#         "options": [
#             "A. The system of rules, practices, and processes by which a company is directed and controlled",
#             "B. The process of managing"
#         ],
#         "correct_answer": "A"
#     },
#     {
#         "id": 10,
#         "question": "What is the role of a mission statement in business strategy?",
#         "options": [
#             "A. Communicating the company's purpose and values to stakeholders",
#             "B. Setting financial targets and performance metrics",
#             "C. Analyzing market trends and competitive forces",
#             "D. Identifying opportunities for cost reduction"
#         ],
#         "correct_answer": "A"
#     }
# ]

# # for loop to insert questions into the BusinessStrategy table
# for question in business_strategy_questions:
#     cursor.execute('''INSERT INTO BusinessStrategy (id, question, option1, option2, option3, option4, correct_answer)
#                       VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
#                                                          question['option2'], question['option3'], question['option4'],
#                                                          question['correct_answer']))
#     conn.commit()

# # List of questions for Communications course
# comm_questions = [
#     {
#         "id": 1,
#         "question": "What is the purpose of a business report?",
#         "options": ["A. Presenting financial statements to shareholders", "B. Providing information and analysis to support decision-making", "C. Communicating marketing messages to customers", "D. Documenting employee performance"],
#         "correct_answer": "B"
#     },
#     {
#         "id": 2,
#         "question": "What is the difference between formal and informal communication?",
#         "options": ["A. Formal communication follows established channels and protocols, while informal communication is casual and spontaneous", "B. Formal communication is written, while informal communication is verbal", "C. Formal communication is used for internal communication, while informal communication is used for external communication", "D. Formal communication is mandatory, while informal communication is optional"],
#         "correct_answer": "A"
#     },
#     {
#         "id": 3,
#         "question": "What is active listening?",
#         "options": ["A. Paying full attention to the speaker and providing feedback to confirm understanding", "B. Interrupting the speaker to ask questions or share opinions", "C. Focusing on one's own thoughts and ideas instead of listening to others", "D. Reacting emotionally to the speaker's message without considering its content"],
#         "correct_answer": "A"
#     },
#     {
#         "id": 4,
#         "question": "What is the purpose of a business presentation?",
#         "options": ["A. Sharing information with stakeholders", "B. Persuading others to take a specific action", "C. Providing updates on project progress", "D. All of the above"],
#         "correct_answer": "D"
#     },
#     {
#         "id": 5,
#         "question": "What is the role of body language in communication?",
#         "options": ["A. Reinforcing spoken messages and conveying emotions", "B. Providing additional information not included in the verbal message", "C. Interpreting data and presenting findings", "D. Ensuring that messages are received and understood by the intended audience"],
#         "correct_answer": "A"
#     },
#     {
#         "id": 6,
#         "question": "What is the purpose of a business proposal?",
#         "options": ["A. Soliciting feedback from stakeholders", "B. Outlining a plan for addressing a specific business need", "C. Reporting on the results of a research project", "D. Providing a summary of key findings and recommendations"],
#         "correct_answer": "B"
#     },
#     {
#         "id": 7,
#         "question": "What is the difference between persuasion and manipulation?",
#         "options": ["A. Persuasion involves influencing others through reasoning and evidence, while manipulation involves deceiving others for personal gain", "B. Persuasion focuses on building trust and rapport, while manipulation relies on coercion and intimidation", "C. Persuasion is ethical, while manipulation is unethical", "D. Persuasion leads to mutually beneficial outcomes, while manipulation leads to one-sided outcomes"],
#         "correct_answer": "A"
#     },
#     {
#         "id": 8,
#         "question": "What is the purpose of a business memo?",
#         "options": ["A. Providing feedback on employee performance", "B. Documenting decisions and agreements reached in meetings", "C. Sharing updates on project progress", "D. Soliciting input from team members"],
#         "correct_answer": "B"
#     },
#     {
#         "id": 9,
#         "question": "What is the difference between formal and informal writing?",
#         "options": ["A. Formal writing follows standard conventions and is structured, while informal writing is casual and conversational", "B. Formal writing is used for internal communication, while informal writing is used for external communication", "C. Formal writing is mandatory, while informal writing is optional", "D. Formal writing is professional, while informal writing is personal"],
#         "correct_answer": "A"
#     },
#     {
#         "id": 10,
#         "question": "What is the purpose of a business email?",
#         "options": ["A. Sending meeting invitations and scheduling appointments", "B. Sharing information and collaborating with colleagues", "C. Communicating with customers and clients", "D. All of the above"],
#         "correct_answer": "D"
#     }
# ]

# # Insert questions into the Business Communications table
# for question in comm_questions:
#     cursor.execute('''INSERT INTO BusinessCommunication (id, question, option1, option2, option3, option4, correct_answer)
#                       VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
#                                                          question['option2'], question['option3'], question['option4'],
#                                                          question['correct_answer']))
#     conn.commit()

#Fetch and display data from each table
tables = ['BusinessStrategy', 'BusinessApplicationsDevelopment', 'Finance', 'AnalyticsCapstone', 'BusinessCommunication']
for table in tables:
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    print(f"Contents of {table} table:")
    for row in rows:
        print(row)
    print()

# def add_new_question(table, id, question, option1, option2, option3, option4, correct_answer):
#     try:
#         # Connect to the database
#         conn = sqlite3.connect('class.db')
#         cursor = conn.cursor()

#         # Insert the new question into the specified category table(add 1 to previous id )
#         cursor.execute(f"INSERT INTO {table} (id, question, option1, option2, option3, option4, correct_answer) "
#                        "VALUES (?, ?, ?, ?, ?, ?, ?)",
#                        (id, question, option1, option2, option3, option4, correct_answer))
        
#         # Commit the changes and close the connection
#         conn.commit()
        # conn.close()
        
#         print("New question added successfully!")

#     except sqlite3.Error as error:
#         print("Error adding new question:", error)