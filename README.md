# Exercise Badges

![](https://byob.yarr.is/SK-Subroto/fau-made-template-ss24/score_ex1) ![](https://byob.yarr.is/SK-Subroto/fau-made-template-ss24/score_ex2) ![](https://byob.yarr.is/SK-Subroto/fau-made-template-ss24/score_ex3) ![](https://byob.yarr.is/SK-Subroto/fau-made-template-ss24/score_ex4) ![](https://byob.yarr.is/SK-Subroto/fau-made-template-ss24/score_ex5)

# Impact of Weather on Library visit in Chicago

The main goal of this data engineering project is to integrate and analyze **visitor and weather data for Chicago to establish the city's suitability for library visitors**. By examining trends in visitor counts from the Chicago library dataset from 2018 and the city's weather patterns, the project aims to determine if Chicago's infrastructure and climate support a conducive and enjoyable environment for library visitors.
The project is using two dataset: [Weather Data of Chicago](https://bulk.meteostat.net/v2/hourly/72534.csv.gz), and [Library Visitor Data in Chicago](https://data.cityofchicago.org/api/views/i7zz-iiza/rows.csv).

## Project Structure

```bash
project/             
├── analysis-report.pdf             
├── data-report.pdf               
├── pipeline.py                    
├── pipeline.sh                    
├── project-plan.md          
├── requirement.txt                
└── test_pipeline.py             
└── test.sh             
```

**Important files of the project and their roles:**

- `project/data-report.pdf`: This PDF describe the dataset that we used for the project, describe the main purpose of this project.
- `project/pipeline.py`: It will run an automated pipeline that creates an SQLite database named `MADE.sqlite` that contains two tables representing two open data sources of the project.
- `project/test.sh`: A bash script that will execute the component and system-level testing for the project by calling two other Python scripts, `project/test_pipeline.py`.
- `project/analysis-report.pdf`: This PDF describe final finding of the project, providing a comprehensive exploration of all aspects.

**Project Pipeline using GitHub Action:** <br>

A project pipeline has been implemented using a GitHub action defined in [.github/workflows/pipeline-test.yml](.github/workflows/pipeline-test.yml). This pipeline is triggered whenever changes are made to the `project/` directory and pushed to the GitHub repository, or when a pull request is created and merged into the `main` branch. The `pipeline-test.yml` workflow executes the `project/test.sh` test script, and in case of any failures, it sends an error message

## Project Setup

1. Clone this git repository
```bash
git clone https://github.com/SK-Subroto/fau-made-template-ss24
```
2. Go to project directory
```bash
cd project
```
3. Install [Python](https://www.python.org/). Then create a virtual environment inside the repo and activate it.
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1 
```
4. Install the required Python packages for the project.
```bash
pip install -r requirements.txt
```
5. Run the project
```bash
python pipeline.py
```
6. Run the test script
```bash
chmod +x test.sh
sh test.sh
```

## Exercises (not part of the project)
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervalls, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv`
2. `./exercises/exercise2.jv`
3. `./exercises/exercise3.jv`
4. `./exercises/exercise4.jv`
5. `./exercises/exercise5.jv`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`).
