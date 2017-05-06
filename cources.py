import random
import json
from random import randint

courses = [ "Using Databases with Python",
 
   "HTML, CSS, and Javascript for Web Developers",
 
   "Introduction to HTML5",
 
   "Using Python to Access Web Data",
 
   "Multiplatform Mobile App Development with Web Technologies",
 
   "Front-End Web UI Frameworks and Tools",
 
   "Capstone: Retrieving, Processing, and Visualizing Data with Python",
 
   "Introduction to Web Development",
 
   "Single Page Web Applications with AngularJS",
 
   "Powerful Tools for Teaching and Learning: Web 2.0 Tools",
 
   "Responsive Web Design",
 
   "Web Application Development: Basic Concepts",
 
   "Web Connectivity and Security in Embedded Systems",
 
   "Web Application Development with JavaScript and MongoDB",
 
   "Ruby on Rails Web Services and Integration with MongoDB",
 
   "Designing Highly Scalable Web Apps on Google Cloud Platform",
 
   "Programming Foundations with JavaScript, HTML and CSS",
 
   "Script Writing: Write a Pilot Episode for a TV or Web Series (Project-Centered Course)",
 
   "Web Design for Everybody Capstone",
 
   "Responsive Website Tutorial and Examples",
 
   "Full Stack Web Development Specialization Capstone Project",
 
   "How To Create a Website in a Weekend! (Project-Centered Course)",
 
   "Responsive Website Basics: Code with HTML, CSS, and JavaScript ",
 
   "Multimodal Literacies: Communication and Learning in the Era of Digital Media ",
 
   "Ruby on Rails: An Introduction",
 
   "HTML, CSS and JavaScript",
 
   "Internet History, Technology, and Security",
 
   "Design Principles: an Introduction",
 
   "Responsive Website Development and Design Capstone ",
 
   "The fundamentals of hotel distribution",
 
   "Interactivity with JavaScript",
 
   "Introduction to CSS3",
 
   "Social Media Data Analytics",
 
   "Game Development for Modern Platforms",
 
   "CODAPPS: Coding mobile apps for entrepreneurs",
 
   "Introduction to Meteor.js Development ",
 
   "Introduction to User Experience Design ",
 
   "Getting started with Augmented Reality",
 
   "Advanced Styling with Responsive Design",
 
   "Front-End JavaScript Frameworks: AngularJS",
 
   "Java Programming: Solving Problems with Software",
 
   "Networks: Friends, Money, and Bytes",
 
   "Programming for Everybody (Getting Started with Python)",
 
   "Python Data Structures",
 
   "Information Design",
 
   "Software Security ",
 
   "A developer's guide to the Internet of Things (IoT)",
 
   "Server-side Development with NodeJS",
 
   "Parallel programming",
 
   "Functional Program Design in Scala",
 
   "Programming Mobile Applications for Android Handheld Systems: Part 2",
 
   "Creative Programming for Digital Media & Mobile Apps",
 
   "Java Programming: Principles of Software Design",
 
   "Object Oriented Programming in Java",
 
   "Algorithmic Toolbox",
 
   "Data Structures",
 
   "Big Data Analysis with Scala and Spark",
 
   "Algorithms on Graphs",
 
   "Rails with Active Record and Action Pack",
 
   "An Introduction to Interactive Programming in Python (Part 1)",
 
   "Cryptography I",
 
   "Bitcoin and Cryptocurrency Technologies",
 
   "Google Cloud Platform Fundamentals",
 
   "Cybersecurity and Its Ten Domains",
 
   "Cloud Computing Applications, Part 1: Cloud Systems and Infrastructure",
 
   "Cloud Networking",
 
   "Information Security: Context and Introduction",
 
   "Usable Security",
 
   "Cryptography",
 
   "Interfacing with the Raspberry Pi",
 
   "Cloud Computing Applications, Part 2: Big Data and Applications in the Cloud",
 
   "Big Data, Cloud Computing, & CDN Emerging Technologies",
 
   "International Cyber Conflicts",
 
   "Networks Illustrated: Principles without Calculus",
 
   "Cybersecurity and the Internet of Things",
 
   "Architecting Smart IoT Devices",
 
   "Wireless Communication Emerging Technologies",
 
   "Hardware Security",
 
   "Computing, Storage and Security with Google Cloud Platform",
 
   "Internet of Things: Communication Technologies",
 
   "Introduction to Architecting Smart IoT Devices",
 
   "Cybersecurity and Mobility",
 
   "Configuration Management on Google Cloud Platform",
 
   "Securing Digital Democracy",
 
   "Internet Emerging Technologies",
 
  
   "Cybersecurity and the X-Factor",
 
   "Networking and Security in iOS Applications",
 
   "System Validation (4): Modelling Software, Protocols, and other behaviour",
 
   "Emerging Technologies Capstone ",
 
   "The Business of Cybersecurity Capstone",
 
   "Cloud Computing Project",
 
   "Capstone MOOC for \"Android App Development\"",
 
   "iOS Project: Transreality Game",
 
   "Build Your Own iOS App",
 
   "Capstone: Photo Tourist Web Application",
 
   "Introduction To Swift Programming",
 
   "Build Your First Android App (Project-Centered Course)",
 
   "Programming Mobile Applications for Android Handheld Systems: Part 1",
 
   "Android App Components - Intents, Activities, and Broadcast Receivers",
 
   "Programming Languages, Part B",
 
   "Programming Languages, Part A",
 
   "Java for Android",
 
  
   "Control of Mobile Robots",
 
   "iOS App Development Basics",
 
   "Foundations of Objective-C App Development",
 
   "Engineering Maintainable Android Apps",
 
   "Android App Components - Services, Local IPC, and Content Providers",
 
   "Smartphone Emerging Technologies",
 
   "Programming Languages, Part C",
 
   "App Design and Development for iOS",
 
   "Best Practices for iOS User Interface Design",
 
   "Toward the Future of iOS Development with Swift",
 
   "Agile Development in Practice (Project-centered Course)",
 
   "Interaction Design Capstone Project",
 
   "Game Design Document: Define the Art & Concepts",
 
   "Brand New Brand",
 
   "Software Product Management Capstone",
 
   "Evaluating User Interfaces",
 
   "System Validation (3): Requirements by modal formulas",
 
   "System Validation (2): Model process behaviour",
 
   "World Design for Video Games",
 
   "System Validation: Automata and behavioural equivalences",
 
   "Prototyping and Design",
 
   "Input and Interaction",
 
   "Project Management Project",
 
   "User Research and Design",
 
   "Story and Narrative Development for Video Games",
 
   "Reviews & Metrics for Software Improvements",
 
   "Running Product Design Sprints",
 
   "Character Design for Video Games",
 
   "Designing, Running, and Analyzing Experiments",
 
   "Testing with Agile",
 
   "Introduction to UI Design",
 
   "Managing an Agile Team",
 
   "User Experience: Research & Prototyping",
 
   "Agile Planning for Software Products",
 
   "Principles of Game Design",
 
   "Data Warehouse Concepts, Design, and Data Integration",
 
   "Client Needs and Software Requirements ",
 
   "Introduction to Imagemaking",
 
   "Development of Real-Time Systems",
 
   "Introduction to Game Design",
 
   "Software Processes and Agile Practices",
 
   "Getting Started: Agile Meets Design Thinking",
 
   "Introduction to Software Product Management",
 
   "Digital Systems: From Logic Gates to Processors",
 
   "Introduction to Typography",
 
   "Human-Centered Design: an Introduction",
 
   "Introduction to the Internet of Things and Embedded Systems",
 
   "Gamification",
 
   "Fundamentals of Graphic Design",
 
   "Computer Architecture",
 
   "Applied Plotting, Charting & Data Representation in Python",
 
   "Algorithms, Part I",
 
   "Divide and Conquer, Sorting and Searching, and Randomized Algorithms",
 
   "Algorithms, Part II",
 
   "Computational Neuroscience",
 
   "Discrete Mathematics",
 
   "Cloud Computing Concepts, Part 1",
 
   "Build a Modern Computer from First Principles: From Nand to Tetris (Project-Centered Course)",
 
   "Fundamentals of Digital Image and Video Processing",
 
   "Probabilistic Graphical Models 1: Representation",
 
   "Computational Investing, Part I",
 
   "Graph Search, Shortest Paths, and Data Structures",
 
   "Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming",
 
   "Discrete Optimization",
 
   "An Introduction to Interactive Programming in Python (Part 2)",
 
   "Algorithmic Thinking (Part 1)",
 
   "Introduction to Genomic Technologies",
 
   "Data Structures and Performance",
 
   "Interactive Computer Graphics",
 
   "Algorithms on Strings",
 
   "Finding Hidden Messages in DNA (Bioinformatics I)",
 
   "Advanced Data Structures in Java",
 
   "Advanced Algorithms and Complexity",
 
   "Shortest Paths Revisited, NP-Complete Problems and What To Do About Them",
 
   "Cloud Computing Concepts: Part 2",
 
   "Big Data, Genes, and Medicine",
 
   "Principles of Computing (Part 1)",
 
   "Approximation Algorithms Part I",
 
   "Algorithmic Thinking (Part 2)",
 
   "Principles of Computing (Part 2)",
 
   "Genome Sequencing (Bioinformatics II)",
 
   "Comparing Genes, Proteins, and Genomes (Bioinformatics III)",
 
   "Approximation Algorithms Part II",
 
   "Global Warming II: Create Your Own Models in Python",
 
   "Molecular Evolution (Bioinformatics IV)",
 
   "Finding Mutations in DNA and Proteins (Bioinformatics VI)",
 
   "Genome Assembly Programming Challenge",
 
   "The Fundamentals of Computing Capstone Exam",
 
   "Bioinformatics Capstone: Big Data in Biology",
 
   "Digital Signal Processing",
 
   "Introduction to Natural Language Processing",
 
   "Basic Modeling for Discrete Optimization",
 
   "Functional Programming in Scala Capstone",
 
   "Business Intelligence Concepts, Tools, and Applications",
 
   "Hands-on Text Mining and Analytics",
 
   "Software Architecture for the Internet of Things",
 
   "Build a Modern Computer from First Principles: Nand to Tetris Part II (project-centered course)",
 
   "C++ For C Programmers, Part B",
 
   "Advanced R Programming",
 
   "Mastering the Software Engineering Interview",
 
   "Cluster Analysis in Data Mining",
 
   "Fundamentals of Computer Architecture",
 
   "Data Manipulation at Scale: Systems and Algorithms",
 
   "Java Programming: Arrays, Lists, and Structured Data",
 
   "Pattern Discovery in Data Mining",
 
   "Data Processing Using Python",
 
   "The R Programming Environment",
 
   "Audio Signal Processing for Music Applications",
 
   "Image and Video Processing: From Mars to Hollywood with a Stop at the Hospital",
 
   "The Raspberry Pi Platform and Python Programming for the Raspberry Pi",
 
   "The Finite Element Method for Problems in Physics",
 
   "Introduction to Game Development",
 
   "Embedded Hardware and Operating Systems",
 
   "Database Management Essentials",
 
   "The Arduino Platform and C Programming",
 
   "Code Yourself! An Introduction to Programming",
 
   "Software Defined Networking",
 
   "C++ For C Programmers, Part A",
 
   "Python Programming: A Concise Introduction",
 
   "Introduction to Logic",
 
   "Learn to Program: The Fundamentals",
 
   "Functional Programming Principles in Scala",
 
   "Introduction to Programming with MATLAB",
 
   "Introduction to Data Science in Python",
]
dataset={}
i=1
while i<=1000:
	recomendation_by_user={}
	no=randint(3,9)
	while no>1:
		a=random.choice(courses)
		recomendation_by_user[a]=round(random.uniform(3.0,5.0),1)
		no-=1
	dataset[str(i)]=recomendation_by_user
	i+=1

print json.dumps(dataset, indent=2)

