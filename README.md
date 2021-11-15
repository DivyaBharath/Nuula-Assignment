# Nuula Data Engineer Assignment

## Overview

Please note: **\*The following is a hypothetical scenario\***.

DataExtract is an internal tool used by our development team to pull data and run various risk rules. At the moment DataExtract connects to a pipeline which outputs XML files to a message bus. Our team is building out a pipeline which would extract the `/Data/Nuula/Errors`, `/Data/DataExtract900jer/Messages` and `/Data/DataExtract900jer/Rules` objects from the raw xmls into a relational database.

Please write a simple parser that takes a file path to a directory of these files, extracts these objects from the XMLs, and outputs a single xlsx file (for all files), where each of the objects is represented in it's own table.

## Evaluation Criteria

- Design Patterns (25%)
- Code Clarity (25%)
- Unit Testing (25%)
- Correctness (25%)

## Submission

- Please submit your versioned code (repo) via a link to your choice of service (Github, Bitbucket etc).
- You may use any programming language of choice.
- Submission should contain instruction on how to generate the excel output.
- Please submit your assignment in 5 days.

## Note

We will be reviewing the solution with you, so while solving the problem, give some thought to what sort of software architecture would support this business problem.
