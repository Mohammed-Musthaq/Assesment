@echo off
REM Navigate to the project directory
cd /d "C:\Users\MOHAMAD_SHARUK\Automation\Assessment"

REM Create and activate a virtual environment
python -m venv venv
call venv\Scripts\activate

REM Install required packages
pip install -r requirements.txt

REM Run the Behave tests
behave

REM Deactivate the virtual environment
deactivate
