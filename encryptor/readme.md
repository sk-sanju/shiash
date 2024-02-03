
<h1>Tailored Outcome and its protected data Methodology through data integrity<h1>








Preface
<h2>TABLE OF CONTENTS</h2>

1. SOFTWARE DEVELOPMENT LIFE CYCLE
2. PLATFORM KNOWLEDGE
3. DOMAIN KNOWLEDGE
4. ABOUT PROJECT
4.1 ABSTRACT
4.2 SCOPE OF THE PROJECT
4.3 EXISTING SYSTEM
 	4.3.1 DISADVANTAGES
     4.4 PROPOSED SYSTEM
 		4.4.1 ADVANTAGES
5. BOTTOM LINE AND FUTURE ENHANCEMENT
6. HARDWARE AND SOFTWARE REQUIREMENTS








<h2>1. SDLC (Software Development Life Cycle)</h2>

The Software Development Life Cycle is a systematic process for building software that ensures the quality and correctness of the software built. SDLC process aims to produce high-quality software which meets customer expectations. The software development should be completed within the pre-defined time frame and cost.

SDLC Phases
The entire SDLC process is divided into the following stages:
 
●	Phase 1: Requirement collection and analysis
●	Phase 2: Feasibility study
●	Phase 3: Design
●	Phase 4: Coding
●	Phase 5: Testing
●	Phase 6: Installation/Deployment
●	Phase 7: Maintenance

<h2>2. Platform Knowledge</h2>

<h3>Introduction to Python:</h3>

Python is developed by Guido van Rossum. Guido van Rossum started implementing Python in 1989. Python is a facile programming language so even if you are new to programming, you can learn python without facing any issues. Python is a general-purpose programming language that is becoming ever more popular for data science. Companies worldwide are using Python to harvest insights from their data and gain a competitive edge. Python specifically for data science. To store and manipulate data, and helpful data science tools to begin conducting your own analyses. 

<h3>What is Python?</h3>

Python is an interpreted, high-level, general purpose programming language. It is dynamically typed and collected. Python is an interpreted language and not a compiled one, although compilation is a step. Python code, written in .py file is first compiled to what is called byte code which is stored with a .pyc or .pyo format. Instead of translating source code to machine code like C++, Python code it translated to byte code. This byte code is a low-level set of instructions that can be executed by an interpreter.  One popular advantage of interpreted languages is that they are platform-independent. As long as the Python byte code and the Virtual Machine have the same version, Python byte code can be executed on any platform (Windows, MacOS, etc).Dynamic typing is another advantage. In static-typed languages like C++, you have to declare the variable type and any discrepancy like adding a string and an integer is checked during compile time. In older programming languages, memory allocation was quite manual. Many times when you use variables that are no longer in use or referenced anywhere else in the program, they need to be cleaned from the memory. Garbage Collector does that for you.
 


<h2>3. Domain Knowledge</h2>

<h3>OVERVIEW:</h3>
A security system identifies and mitigates the system vulnerabilities, by either removing them, or restricting access to them, to a very small group. The competition between inventing new security measures to protect data and inventing hacking techniques in conjunction with discovering and leveraging pre-existing vulnerabilities is infinite. Therefore, securing data and resources is becoming more and more challenging day by day. Nevertheless, there exist several different techniques to secure the data being transferred over a network and also that on a user machine. Specializes in securing data in motion through the use of the patented REL-ID based mutual authentication scheme. SSL is one such tool to secure data sent over a network, using cipher text. Using SSL data is kept confidential and message integrity is maintained. 
However, recently there have been network security breaches, including the famous “HEARTBLEED” bug. But, the question that remains is “what if the user machine itself is hacked? .it can be used to ensure that the end user is secured as well as the tunnel. It also uses techniques of authentication to assure to each end user that it is communicating with an authorized user and not a fake one. Such security measures are used to secure data in motion, meaning data that has been shared between computers. They may prove to be of minimum value, if the operating system on which it resides is compromised. It is therefore crucial to understand and remove the security flaws in the operating system itself. We, on the other hand, are trying to secure data at rest, by coming up with various approaches, one of which is application white listing.
 Hardening is a technique to reduce vulnerabilities of the existing operating system. It aims to eliminate security risks in an operating system. This is done by turning off all those services of the operating system which are not used are risky and allowing only those which are secure for user’s data. Thus, this environment becomes a kind of locked down or reduce version of a fully-fledged operating system. Operating system hardening is a technique which allows us a security on the machine level. A hardened operating system can be considered as a smaller version of an otherwise compromised operating system. Secondly, we implement a technique called as application white-listing. It is the technique of preparing a list of all applications that are safe to execute. All applications that excluded from this list are disallowed to spawn.















<h2>4. About the project:</h2>
<h3>4.1 Abstract:</h3>
Cloud computing provides dependability and availability while also ensuring data integrity. It's critical to comprehend how encryption can be employed to safeguard data integrity in a cloud environment. For instance, as part of its virtualization infrastructure, a corporation can demand the development and use of encryption keys for data security rotating algorithms. When migrating your data to the cloud, data integrity is a crucial issue. You must make sure that data is constantly available and that it won't become corrupted no matter how many times it is copied. When you want to save your data even if the cloud provider goes offline for a day or if documents are compromised by hackers or system faults, data integrity in the cloud is a crucial component. Usually in any organization the data which contain more sensitive information is being handled with care. They used to cipher-text the data which is been transferred in online that too in cloud storages to avoid intruders to access the data, so it becomes mandatory for any organization to safe guard their data. More than safeguarding the data, data integrity is an important fact which is used in getting data accurately and handles consistency of data. It also maintains the design, implementation and usage of any system which stores, process or retrieves data. In our model we mainly focus on cipher and decipher of the data in a more effective way, so that there is no possible for intruders to get the data. To make it happen we use Data Encryption Standard (DES), it supports functionality to save a file in an encrypted format which can only be accessed by supporting the correct password, which is stored as the key. With the help of same key we can able to decrypt the same file. This makes the system more secure than any other schemas.


<h3>4.2 Scope of the project: </h3>
The process of encrypting and decrypting file is mandatory in any organization to help them to prevent their data from hacking. That too in the field like nonmetallic industry we have many sensitive information’s which are been kept secret to avoid the data leakage with their competitors. Data Encryption Standard (DES), which describes the round keys generation procedure and allows for data encryption and decryption with the same key, is the fundamental advantage in our model. For years, the Data Encryption Standard, a symmetric-key encryption technique, has been used in both military and commercial applications. Data is encrypted and decrypted using 56-bit keys. The Data Encryption Standard is a communication protocol that uses complex mathematical operations. It is used for electronic data encryption, decryption, and message veracity verification. As it is mandatory in our Non metallic industry to maintain secure of the data which is to be processed and maintained for future process, this kind of cryptosystem is mandatory. 

<h3>4.3 Existing system: </h3>
With attribute-based encryption, it is possible to decide whether or not to decode data depending on certain attributes and policies. Content-based, role-based, and multi-authority access policies are the three primary types of attribute-based encryption. Attribute-Based is a broader type of encryption which has a flexible policy-based access controls that are mathematically (i.e., cryptographically) enforced. Data can now be encrypted so that it can be decrypted by anyone with credentials that satisfy an arbitrary attribute-based access control policy, as opposed to just being encrypted to a particular user. Any string can be used as an attribute in ABE solutions. Aspects can also have numerical values, and policies can include ranges over these values. Depending on the intended use, a certain set of properties will be employed. When exchanging sensitive information, the recipient must be confident that the communication has arrived intact from the intended sender and has not been altered accidentally or unintentionally. Active and passive threats to data integrity are two distinct categories. Threats of the passive variety exist as a result of unintentional data modifications. Active threats allow an attacker to modify data with malice in their hearts.

<h4>4.3.1 Disadvantages: </h4>
•	Lack of a useful attribute access that could be used in realistic circumstances.
•	Key generation is really important which becomes more disadvantages in this model.
•	Dealing with a high number of authorized users is very taxing because their public keys are needed for encryption.
•	This system permits the exercise of control over the decoding of cipher text extremely loosely. Given that the data owner must continue to rely on the key allocator's job.
•	The tree structure prevents the many parties from working together.

<h3>4.4 Proposed system: </h3>
In our process we have worked on the model which is a non metallic industry, where the data are to be secured, so that it can secure from the intruders. Here we secure data like customers details and their unique product details, more than that the data which is used for the production process is to be secured because to maintain a secrete in their production. If data leakage happens then it would lead to a loss in their business because of their competitors. Here we have resolved it through our Data Encryption Standard (DES). Each stage of the DES process, which consists of numerous phases, is referred to as a round. The amount of rounds changes depending on the size of the key being utilized. A 128-bit key, for instance, needs 10 rounds, a 192-bit key, 12 rounds, and so on. So this makes DES more secure and worked out fine with our model.

<h4>4.4.1 Advantages: </h4>
•	Des offers the benefit of having a better level of security than the conventional DES implementation. Additionally, it employs fewer round numbers, which makes it more resistant to attacks.
•	The primary benefit of DES is its compact size, which makes it simple to use and program.
•	Our algorithm is royalty-free so it can be accessible to both the private and public sectors.
•	It doesn’t require any input features which are used to be scaled.


<h2>5. BOTTOM LINE AND FUTURE ENHANCEMENT: </h2>
Thus as our model depicts the usage of customized product and some data which should be kept in a secret way should be secured. Here we have used the data integrity process. DES is a strong data structure that by minimizing the amount of pointless communication between threads, it can assist you in doing highly concurrent computations. DES is accustomed to storing data in a data structure, which makes it easier for the program to access that data. The future objective is to ensure that DES can manage all forms of data while utilizing the newest, most effective data storage techniques.


<h2>6. HARDWARE AND SOFTWARE REQUIREMENTS</h2>

<h3>Hardware requirements:</h3>

●	Processor:		 Intel(R) Core(TM) i5-8350U CPU
●	Speed:			 1.6 GHz and Above
●	RAM:			 6 GB and Above
●	Hard Disk:		 125 GB
●	Monitor:		 15’’ LED SVGA
●	Input Devices:		 Keyboard, Mouse
Software requirements:
●	Operating system:	 Windows 11
●	Coding Language: 	 PYTHON - DJANGO
●	IDE:                             VISUAL STUDIO CODE
●	Database:		 SQLite 3 
